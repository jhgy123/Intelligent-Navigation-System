from django.test import TestCase

# Create your tests here.


# import redis
# # 创建连接对象
# r = redis.Redis(host='localhost', port=6379, db=0)
#
# # 执行具体操作
# r.set('foo', 'bar')  # 给key设置value
# print(r.get('foo'))  # 根据key获取value
# # 打印：b'bar'
#
# from django.core.cache import cache
#
# cache.set("key", 1, timeout=30)
# print(cache.get("key", default="默认值"))

# neo4j使用测试
# from fetch_api.models import Station
#
# test = Station(station_name='我的站点', latitude='4944964', longitude='455').save()
# all_nodes = Station.nodes.all()
# print(all_nodes)

#最短路径查询
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