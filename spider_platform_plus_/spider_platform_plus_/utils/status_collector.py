import redis

from spider_platform_plus_.conf.default_settings import REDIS_QUEUE_HOST, REDIS_QUEUE_PORT, REDIS_QUEUE_DB


class StatsCollector(object):

    def __init__(self, spider_name,host=REDIS_QUEUE_HOST, port=REDIS_QUEUE_PORT, \
                 db=REDIS_QUEUE_DB, password=None):

        self.redis = redis.StrictRedis(host=host, port=port, db=db, password=password)
        self.request_nums_key = spider_name + "_request_nums"
        # 存储响应数量的键
        self.response_nums_key = spider_name + "_response_nums"


    def incr(self, key):
        '''给键对应的值增加1，不存在会自动创建，并且值为1，'''
        self.redis.incr(key)

    def decr(self,key):
        '''给键对应的值增-1'''
        self.redis.decr(key)

    def get(self, key):
        '''获取键对应的值，不存在是为0，存在则获取并转化为int类型'''
        ret = self.redis.get(key)
        if not ret:
            ret = 0
        else:
            ret = int(ret)
        return ret

    def clear(self):
        '''程序结束后清空所有的值'''
        self.redis.delete(self.request_nums_key, self.response_nums_key)

    @property
    def request_nums(self):
        '''获取请求数量'''
        return self.get(self.request_nums_key)

    @property
    def response_nums(self):
        '''获取响应数量'''
        return self.get(self.response_nums_key)


