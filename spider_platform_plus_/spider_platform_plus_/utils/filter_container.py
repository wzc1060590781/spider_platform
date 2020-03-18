import redis

from spider_platform_plus_.conf import settings


class RedisFilterContainer():

    def __init__(self,redis_key=settings.REDIS_SET_NAME):
        self._redis = redis.StrictRedis(host=settings.REDIS_SET_HOST, port=settings.REDIS_SET_PORT ,db=settings.REDIS_SET_DB)
        self._name = redis_key

    def add_fp(self, fp):
        '''往去重容器添加一个指纹'''
        self._redis.sadd(self._name, fp)

    def delete_fp(self,fp):
        '''删除fp'''
        self._redis.srem(self._name,fp)

    def exists(self, fp):
        '''判断指纹是否在去重容器中'''
        return self._redis.sismember(self._name, fp)