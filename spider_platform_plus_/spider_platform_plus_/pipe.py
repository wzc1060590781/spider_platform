import pymongo

from spider_platform_plus_.conf.default_settings import MONGO_PIP_HOST, MONGO_PIP_PORT


class Pipe(object):
    '''根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回'''
    def __init__(self, *args, **kwargs):
        # 导入父构造
        pass
    def save(self, con_s):
        '''发起请求获取响应的方法'''
        # 1. 根据请求对象，发起请求，获取响应
        #    判断请求方法：
        pass


class MongoPip(Pipe):
    def __init__(self,db_name,collection,host=MONGO_PIP_HOST,port=MONGO_PIP_PORT):
        super().__init__(self)
        self.mongo = pymongo.MongoClient()[db_name][collection]


    def save(self, data):
        self.mongo.insert(data)




        # print(con_s)
        # if con_s.get('pipe') == 'redis':
        #     for con_ex in con_s.get('extract'):
        #         pipe_name = con_s.get('redis_name')
        #         rq = RedisQueue(pipe_name)
        #         if con_ex.get('type') == "list":
        #             for ii in con_ex.get('value'):
        #                 print(ii)
        #                 rq.put(ii)
        #         print('保存总长度：' + str(rq.qsize()))
        # if con_s.get('pipe') == 'mongo':
        #     pipe_name = con_s.get('mongo_name')
        #     mongo_table = con_s.get('mongo_table')
        #
        #     myclient = pymongo.MongoClient(host='127.0.0.1', port=27017)
        #     mydb = myclient[pipe_name]  # 数据库使用
        #     mycol = mydb[mongo_table]  # 表（集合）使用
        #     pipe_value={}
        #     for con_ex in con_s.get('extract'):
        #         print(con_ex)
        #         print(type(con_ex))
        #         pipe_value[con_ex.get('key')]=con_ex.get('value')
        #     mycol.insert_one(pipe_value)
        #     for ii in mycol.find():
        #         print(ii)


