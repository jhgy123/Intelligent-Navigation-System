#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pandas import read_csv

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
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


import redis
# 创建连接对象
r = redis.Redis(host='localhost', port=6379, db=0)

#导入数据

filename = './dataset/昆明市站点.csv'
names = ['名称','经度','纬度']
data = read_csv(filename,names = names)
print(len(data))
station_name = data.iloc[:,0]
station_latitude = data.iloc[:,1]
station_longtitude = data.iloc[:,2]
for i in range(1,len(data)):
    r.geoadd('SubwayStation', [station_latitude[i], station_longtitude[i], station_name[i]])


filename2 = './dataset/昆明市商圈信息.csv'
names2 = ['名称','经度','纬度']
data2 = read_csv(filename2,names = names2,encoding='gbk')
print(len(data2))
station_name2 = data2.iloc[:,0]
station_latitude2 = data2.iloc[:,1]
station_longtitude2 = data2.iloc[:,2]
for i in range(1,len(data2)):
    r.geoadd('Building', [station_latitude2[i], station_longtitude2[i], station_name2[i]])
# 执行具体操作

def NearbyMetroStation(str):
    building = r.geopos("Building", str)
    #print(building)
    subwaystation = r.georadius("SubwayStation", building[0][0], building[0][1], 3300000, "km",True)
    min = 0x0ffffffff
    for index in range(len(subwaystation)):
        locals = subwaystation[index][0].decode('utf-8')
        if subwaystation[index][1] < min:
            min = subwaystation[index][1]
            station = locals
    return station
#result = NearbyMetroStation("ynu")
#print(result)
#result2 = r.geopos("SubwayStation", result)
#print(result2)
# 打印：b'bar'




