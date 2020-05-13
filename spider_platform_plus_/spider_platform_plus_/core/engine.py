#引擎
import time
from multiprocessing.dummy import Pool

from spider_platform_plus_.config import con
from spider_platform_plus_.core.downloader import Downloader
from spider_platform_plus_.core.extract import Extract
from spider_platform_plus_.core.scheduler import Scheduler
from spider_platform_plus_.my_http.request import Request
from spider_platform_plus_.pipe import Pipe, MongoPip

# from spider_platform_plus_.utils.parse_conf import db_type, mongo_name, mongo_collection, spider_name, Config
from spider_platform_plus_.utils.parse_conf import Config
from spider_platform_plus_.utils.queue import RedisQueue
from spider_platform_plus_.utils.status_collector import StatsCollector


class Engine():
    def __init__(self, con, *args, **kwargs):
        self.con=Config(con)
        self.downloader = Downloader()
        self.scheduler = Scheduler(con)
        self.extract = Extract(con)
        self.collector = StatsCollector(self.con.spider_name)
        self.pool = Pool()
        self.is_running = False
        if self.con.db_type == "mongo":
            db_name = self.con.mongo_name
            collection = self.con.mongo_collection
            self.pipe = MongoPip(db_name,collection)

    def _start_request(self):
        headers = self.con.headers
        params = self.con.params
        data = self.con.data
        method = self.con.method
        start_url_dict = con.get('start_url')
        if start_url_dict:
            if start_url_dict.get("url_from") == "list":
                for url in start_url_dict.get('url'):
                    request = Request(url, headers=headers, params=params, data=data,method=method)
                    self.scheduler.add_request(request)
                    # self.collector.incr(self.collector.request_nums_key)

    def _execute_request_response(self):
        request = self.scheduler.get_request()
        print(request.url)
        if request is None:
            print("request为空")
            return
        response = self.downloader.get_response(request)
        # print(response.body)
        self.collector.incr(self.collector.response_nums_key)
        for result in self.extract.tiqu(response):
            if isinstance(result,Request):
                # print(request.url)
                self.scheduler.add_request(result)
                # print(result.url)
                # self.collector.incr(self.collector.request_nums_key)
            else:
                print(result)
                self.pipe.save(result)
        # self.collector.incr(self.collector.response_nums_key)

    def start_engine(self):
        self._start_request()
        for i in range(5):
            self.pool.apply_async(self._execute_request_response, callback=self._callback)
        while True:
            # if self.collector.response_nums >= self.collector.request_nums:
                # self.is_running = False
                # break
            time.sleep(0.0001)

    def _callback(self, temp):
        self.pool.apply_async(self._execute_request_response, callback=self._callback)

if __name__ == '__main__':
    engin = Engine(con)
    engin.start_engine()



