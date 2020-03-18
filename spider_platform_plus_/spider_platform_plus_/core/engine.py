#引擎
import time
from multiprocessing.dummy import Pool

from spider_platform_plus_.config import con
from spider_platform_plus_.core.downloader import Downloader
from spider_platform_plus_.core.extract import Extract
from spider_platform_plus_.core.scheduler import Scheduler
from spider_platform_plus_.my_http.request import Request
from spider_platform_plus_.pipe import Pipe, MongoPip
from spider_platform_plus_.utils.parse_conf import get_db_type, get_mongo_name, get_mongo_collection, get_spider_name
from spider_platform_plus_.utils.queue import RedisQueue
from spider_platform_plus_.utils.status_collector import StatsCollector


class Engine():
    def __init__(self, con, *args, **kwargs):
        self.con=con
        self.downloader = Downloader()
        self.scheduler = Scheduler(con)
        self.extract = Extract(con)
        self.collector = StatsCollector(get_spider_name(con))
        self.pool = Pool()
        self.is_running = False
        if get_db_type(con) == "mongo":
            db_name = get_mongo_name(con)
            collection = get_mongo_collection(con)
            self.pipe = MongoPip(db_name,collection)

    def _start_request(self):
        headers = con.get("headers")
        params = con.get("params")
        data = con.get("data")
        start_url_dict = con.get('start_url')
        if start_url_dict:
            if start_url_dict.get("url_from") == "list":
                for url in start_url_dict.get('url'):
                    request = Request(url, headers=headers, params=params, data=data)
                    self.scheduler.add_request(request)
                    # self.collector.incr(self.collector.request_nums_key)

    def _execute_request_response(self):
        request = self.scheduler.get_request()
        print(request.url)
        if request is None:
            print("request为空")
            return
        response = self.downloader.get_response(request)
        self.collector.incr(self.collector.response_nums_key)
        for result in self.extract.tiqu(response):
            if isinstance(result,Request):
                # print(request.url)
                self.scheduler.add_request(result)
                # self.collector.incr(self.collector.request_nums_key)
            else:
                print(result)
                self.pipe.save(result)
        # self.collector.incr(self.collector.response_nums_key)

    def start_engine(self):
        self._start_request()
        for i in range(1):
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



