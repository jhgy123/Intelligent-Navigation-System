#!/usr/bin/env python
"""Django's command-is_transit utility for administrative tasks."""
import os
import sys




def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mytest.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#########redis最近站点搜索#############################3
# from pandas import read_csv
# import redis
# # 创建连接对象
# r = redis.Redis(host='localhost', port=6379, db=0)
# filename = './dataset/昆明市站点.csv'
# names = ['名称','经度','纬度','是否中转']
# data3 = read_csv(filename,names = names,encoding='gbk')
# # print(data3)
# # print(len(data))
# station_name = data3.iloc[:,0]
# print(station_name)
# station_latitude = data3.iloc[:,1]
# # print(station_latitude)
# station_longtitude = data3.iloc[:,2]
# for i in range(1,len(data3)):
#     # print([station_latitude[i], station_longtitude[i], station_name[i]])
#     r.geoadd('SubwayStation', [station_latitude[i], station_longtitude[i], station_name[i]])
#
#
#
# filename2 = './dataset/昆明市商圈信息.csv'
# names2 = ['名称','经度','纬度']
# data2 = read_csv(filename2,names = names2,encoding='gbk')
# print(len(data2))
# station_name2 = data2.iloc[:,0]
# station_latitude2 = data2.iloc[:,1]
# station_longtitude2 = data2.iloc[:,2]
# for i in range(1,len(data2)):
#     r.geoadd('Building', [station_latitude2[i], station_longtitude2[i], station_name2[i]])

import redis
# 创建连接对象
r = redis.Redis(host='localhost', port=6379, db=0)

# 执行具体操作

def NearbyMetroStation(str):
    building = r.geopos("Building", str)
    #print(building)
    subwaystation = r.georadius("SubwayStation", building[0][0], building[0][1], 3, "km",True)
    min = 0x0ffffffff
    for index in range(len(subwaystation)):
        locals = subwaystation[index][0].decode('utf-8')
        if subwaystation[index][1] < min:
            min = subwaystation[index][1]
            station = locals
    return station
result = NearbyMetroStation("黄瓜营眼镜烧烤(望城美食城店)")

print(result)
result = NearbyMetroStation("昆明医科大学第二附属医院")
print(result)
result2 = r.geopos("SubwayStation", result)
print(result2)
###################### 导入地铁站点数据###################################
# from fetch_api.models import Station
# from pandas import read_csv
# #使用Pandas导入csv数据
# filename = './dataset/昆明市站点.csv'
# names = ['名称','经度','纬度','是否中转']
# data = read_csv(filename,names = names,encoding='gbk')
# print(data)
# station_name=data.iloc[:, 0]
# station_latitude=data.iloc[:, 1]
# station_longitude=data.iloc[:, 2]
# station_transit= data.iloc[:, 3]
# print(type(station_name[1]))
# print(type(station_latitude[1]))
# print(type(station_longitude[1]))
# print(type(station_transit[1]))
# for i in range(1,len(data)):
#     Station(station_id=i, station_name=station_name[i], latitude=station_latitude[i], longitude=station_longitude[i], is_transit=station_transit[i]).save()


#######################导入地铁关系数据#################################
# from fetch_api.models import Station
# from pandas import read_csv
# #使用Pandas导入csv数据
# filename = './dataset/站点距离信息.csv'
# names = ['名称1','名称2','距离(km)']
# data = read_csv(filename,names = names,encoding='gbk')
# start=data.iloc[:,0]
# print(start)
# end=data.iloc[:,1]
# cost=data.iloc[:,2]
# print(type(start[1]))
# for i in range(2,len(data)):
#     staion1 = Station.nodes.get(station_name=start[i])
#     staion2 = Station.nodes.get(station_name=end[i])
#     staion1.cost.connect(staion2, {'pathcost': float(cost[i])})  # 增加关系
#     staion2.cost.connect(staion1, {'pathcost': float(cost[i])})  # 增加关系
# print(type(pd))

# import redis
# # 创建连接对象
# r = redis.Redis(host='localhost', port=6379, db=0)

# 执行具体操作
# r.set('foo', 'bar')  # 给key设置value
# print(r.get('foo'))  # 根据key获取value
# 打印：b'bar'

# from django.core.cache import cache
#
# cache.set("key", 1, timeout=30)
# print(cache.get("key", default="默认值"))

# neo4j使用测试
from fetch_api.models import Station

# test = Station(station_id=1, station_name='我的站点7', latitude='00', longitude='00').save()

# test = Station(station_id='0243', station_name='我的站点8', latitude='10', longitude='10').save()
# test = Station(station_id='xxx', station_name='我的站点5', latitude='20', longitude='20').save()
# test = Station(station_id='iiji', station_name='我的站点6', latitude='30', longitude='30').save()
# # test2 = Station(station_id='000w', station_name='我的站点1', latitude='11', longitude='22').save()
# staion1=Station.nodes.get(station_name='我的站点7')
# staion1.delete()
# staion2=Station.nodes.get(station_name='我的站点7')
# staion1.cost.disconnect(staion2) #删除关系
# staion2.cost.disconnect(staion1) #删除关系
# staion1.cost.connect(staion2,{'pathcost':80.6})#增加关系
# staion2.cost.connect(staion1,{'pathcost':80.6})#增加关系

# all_nodes = Station.nodes.all()
# print(all_nodes)
# 执行cypher语句

#################最短路径###############################

from neomodel import db
# #创建图
# db.cypher_query(query='''CALL gds.graph.create(
#     'myGraph',
#     'Station',
#     'FRIEND',
#     {
#         relationshipProperties: 'pathcost'
#     }
# )''')
#################最短路径###############################
# results= db.cypher_query(query='''MATCH (source:Station {station_name: $s})
# WITH source
# MATCH (target:Station {station_name: $t})
# CALL gds.shortestPath.dijkstra.stream('myGraph', {
#     sourceNode: source,
#     targetNode: target,
#     relationshipWeightProperty: 'pathcost'
# })
# YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
# RETURN
#     index,
#     gds.util.asNode(sourceNode).station_name AS sourceNodeName,
#     gds.util.asNode(targetNode).station_name AS targetNodeName,
#     totalCost,
#     [nodeId IN nodeIds | gds.util.asNode(nodeId).station_name] AS nodeNames,
#     costs,
#     nodes(path) as path
# ORDER BY index''',params={'s':'巫家坝','t':'塔密'})
# print(results[0][0][3])


# def fetch_shortestPath(sourceStation_name, targetStation_name):
#     results = db.cypher_query(query='''MATCH (source:Station {station_name: $s})
#     WITH source
#     MATCH (target:Station {station_name: $t})
#     CALL gds.shortestPath.dijkstra.stream('myGraph', {
#         sourceNode: source,
#         targetNode: target,
#         relationshipWeightProperty: 'pathcost'
#     })
#     YIELD index, sourceNode, targetNode, totalCost, nodeIds, costs, path
#     RETURN
#         index,
#         gds.util.asNode(sourceNode).station_name AS sourceNodeName,
#         gds.util.asNode(targetNode).station_name AS targetNodeName,
#         totalCost,
#         [nodeId IN nodeIds | gds.util.asNode(nodeId).station_name] AS nodeNames,
#         costs,
#         nodes(path) as path
#     ORDER BY index''', params={'s': sourceStation_name, 't': targetStation_name})
#     return results
#
# results=fetch_shortestPath('驼峰街','昆明南火车站')
# print(results[0][0][6])#经过的站点所有信息
# print(results[0][0][6][1])#经过的站点中起点的下一站信息
# print(results[0][0][4])#经过的站点所有名字
# print(results[0][0])#
# print(results[0][0][3])#返回总路径长度



# Replace Jim's country relationship with a new one
# staion1.cost.replace(staion1)
# Remove all of Jim's country relationships
# staion1.cost.disconnect_all()
# print(staion1.cost.is_connected(staion1))
# print(staion2.cost.is_connected(staion1))
