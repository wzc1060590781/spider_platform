#下载器
import requests
from spider_platform_plus_.my_http.response import Response

class Downloader(object):
    '''根据请求对象(Request)，发起HTTP、HTTPS网络请求，拿到HTTP、HTTPS响应，构建响应对象(Response)并返回'''
    def get_response(self, request):
        '''
        实现结构请求对象，发送请求，获取响应
        :param request: 请求对象
        :return: resposne对象
        '''
        if request.method.upper() == "GET":
            resp = requests.get(request.url, headers=request.headers, params=request.params)
        elif request.method.upper() == "POST":
            resp = requests.post(request.url, headers=request.headers, params=request.params, data=request.data)
        elif request.method.upper() == "SPLASH":
            request.url = 'my_http://117.51.136.240:8050/render.html?url={0}'.format(request.url)
            resp = requests.get(request.url,headers=request.headers,params=request.params,data=request.data)
        else:
            raise Exception("不支持的请求方法：<{}>".format(request.method))
        # logger.info("<{} {}>".format(resp.status_code, resp.request.url))
        return Response(url=resp.url, body=resp.content, headers=resp.headers, status_code=resp.status_code)
