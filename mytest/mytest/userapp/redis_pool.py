import django_redis
CACHE = django_redis.get_redis_connection()
