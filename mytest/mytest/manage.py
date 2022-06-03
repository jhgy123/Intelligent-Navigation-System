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
