#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
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

# neo4j使用测试
from fetch_api.models import Station

# test = Station(station_id='4568', station_name='我的站点7', latitude='00', longitude='00').save()
# test = Station(station_id='0243', station_name='我的站点8', latitude='10', longitude='10').save()
# test = Station(station_id='xxx', station_name='我的站点5', latitude='20', longitude='20').save()
# test = Station(station_id='iiji', station_name='我的站点6', latitude='30', longitude='30').save()
# # test2 = Station(station_id='000w', station_name='我的站点1', latitude='11', longitude='22').save()
# staion1=Station.nodes.get(station_name='我的站点5')
# staion2=Station.nodes.get(station_name='我的站点7')
# staion1.cost.disconnect(staion2) #删除关系
# staion2.cost.disconnect(staion1) #删除关系
# staion1.cost.connect(staion2,{'pathcost':80.6})#增加关系
# staion2.cost.connect(staion1,{'pathcost':80.6})#增加关系

# all_nodes = Station.nodes.all()
# print(all_nodes)
# 执行cypher语句

from neomodel import db
results= db.cypher_query(query='''MATCH (source:Station {station_name: $s})
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
ORDER BY index''',params={'s':'我的站点3','t':'我的站点8'})
print(results[0][0][3])
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

# results=fetch_shortestPath('我的站点3','我的站点8')
# print(results[0][0][3])
# Replace Jim's country relationship with a new one
# staion1.cost.replace(staion1)
# Remove all of Jim's country relationships
# staion1.cost.disconnect_all()
# print(staion1.cost.is_connected(staion1))
# print(staion2.cost.is_connected(staion1))
