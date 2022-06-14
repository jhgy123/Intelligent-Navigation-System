from django.shortcuts import render, redirect
from django.urls import reverse
from neomodel import db
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import (
    count_nodes,
    fetch_nodes,
    fetch_node_details,
    fetch_countries,
    fetch_jurisdictions,
    fetch_data_source,
)


class GetNodesCount(APIView):
    def get(self, request):
        count_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'name': request.GET.get('q', ''),
            'country': request.GET.get('c', ''),
            'jurisdiction': request.GET.get('j', ''),
            'sourceID': request.GET.get('s', ''),
        }
        count = count_nodes(count_info)
        data = {
            'response': {
                'status': '200',
                'data': count,
            },
        }
        return Response(data)


class GetNodesData(APIView):
    def get(self, request):
        fetch_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'name': request.GET.get('q', ''),
            'country': request.GET.get('c', ''),
            'jurisdiction': request.GET.get('j', ''),
            'sourceID': request.GET.get('s', ''),
            'limit': 10,
            'page': int(request.GET.get('p', 1)),
        }
        nodes = fetch_nodes(fetch_info)
        data = {
            'response': {
                'status': '200',
                'rows': len(nodes),
                'data': nodes,
            },
        }
        return Response(data)


class GetNodeData(APIView):
    def get(self, request):
        node_info = {
            'node_type': request.GET.get('t', 'Entity'),
            'node_id': int(request.GET.get('id')),
        }
        node_details = fetch_node_details(node_info)
        data = {
            'response': {
                'status': '200',
                'data': node_details,
            },
        }
        return Response(data)


class GetCountries(APIView):
    def get(self, request):
        countries = fetch_countries()
        data = {
            'response': {
                'status': '200',
                'data': countries,
            },
        }
        return Response(data)


class GetJurisdictions(APIView):
    def get(self, request):
        jurisdictions = fetch_jurisdictions()
        data = {
            'response': {
                'status': '200',
                'data': jurisdictions,
            },
        }
        return Response(data)


class GetDataSource(APIView):
    def get(self, request):
        data_source = fetch_data_source()
        data = {
            'response': {
                'status': '200',
                'data': data_source,
            },
        }
        return Response(data)


######django views
#最短路径函数实现###
def fetch_shortestPath(sourceStation_name, targetStation_name):
    results = db.cypher_query(query='''MATCH (source:Station {station_name: $s})
    WITH source
    MATCH (target:Station {station_name: $t})
    CALL gds.shortestPath.dijkstra.stream('myGraph', {
        sourceNode: source,
        targetNode: target,
        relationshipWeightProperty: 'pathcost'
    })
    YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
    RETURN
        index,
        gds.util.asNode(sourceNode).station_name AS sourceNodeName,
        gds.util.asNode(targetNode).station_name AS targetNodeName,
        totalCost,
        [nodeId IN nodeIds | gds.util.asNode(nodeId).station_name] AS nodeNames,
        costs,
        nodes(path) as path
    ORDER BY index''', params={'s': sourceStation_name, 't': targetStation_name})
    return results

import redis
# 创建连接对象
r = redis.Redis(host='localhost', port=6379, db=0)

def NearbyMetroStation(str):
    building = r.geopos("Building", str)
    # print(building)
    subwaystation = r.georadius("SubwayStation", building[0][0], building[0][1], 3, "km",True)
    min = 0x0ffffffff
    for index in range(len(subwaystation)):
        locals = subwaystation[index][0].decode('utf-8')
        if subwaystation[index][1] < min:
            min = subwaystation[index][1]
            station = locals
    return station

# result = NearbyMetroStation("ynu")
# print(result)
# result2 = r.geopos("SubwayStation", result)
# print(result2)

def search(request):
    if request.method == "GET": #get请求处理
        data = {}
        return render(request, 'pathsearch.html', context=data)
    elif request.method == "POST": #post请求处理
        startname = request.POST.get('startname')
        endname = request.POST.get('endname')
        #test
        # startStationName=startname
        # endStationName = endname

        startStationName = NearbyMetroStation(startname)
        endStationName = NearbyMetroStation(endname)
        searchResult=fetch_shortestPath(startStationName, endStationName)
        paths=searchResult[0][0][4] #最短路径的经过站点名字
        data = {
            "paths": paths,
            "start": startStationName,
            "end": endStationName
        }
        return render(request, 'pathsearch.html', context=data)


