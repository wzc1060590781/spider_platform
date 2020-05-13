#解析
import urllib.parse

from bs4 import BeautifulSoup

from lxml import html

from spider_platform_plus_.my_http.request import Request


class Extract(object):
    '''根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回'''
    def __init__(self,cons):
        # 导入父构造
        self.cons = cons

    def tiqu(self,response):
        '''发起请求获取响应的方法'''
        # 1. 根据请求对象，发起请求，获取响应
        #    判断请求方法：
        method = self.cons.get("method")
        host = self.cons.get("host")
        for con in self.cons.get('extract'):
            if con.get("form") == "block_list":
                path = con.get("path")
                element_list = response.xpath(path)
                for element in element_list:
                    data = {}
                    for el in con.get("sub_data"):
                        path = el.get("path")
                        data[el.get("name")] = element.xpath(path)
                    yield data
            # data = {}
            if con.get("form") == "url":
                path = con.get("path")
                part_url = response.xpath(path)[0]
                headers = con.get("headers")
                params = con.get("params")
                request_data = con.get("data")
                url = urllib.parse.urljoin(host, part_url)
                print(url)
                yield Request(url,method=method)
            # else:
            #     pass
            # elif con.get('method') == 'con_url':
            #     con['value']=con_s['url']
            # else:
            #     # 如果方法不是get或者post，抛出一个异常
            #     raise Exception("不支持的请求方法")
        # return data