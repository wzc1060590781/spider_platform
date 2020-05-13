#起始页单独url
# con={
#     "name":"xian_xq",
#     "url":"http://zwfw.shaanxi.gov.cn/icity/govservice/newsnotice?s=1",
#     "url_from":"one",
#     "method":"splash",
#     "headers":{},
#     "params":{},
#     "extract":[{
#         "name":"xian_xq",
#         "path":'//*[@id="zwdt-sheng-info"]/li/a/@href',
#         "method":'xpath',
#         "key":"urls",
#         "type":"list",
#         "value":"",
#         "pipe":"redis"
#         }]
#     }

#起始页列表url
# con={
#     "name":"xian_xq",
#     "url":["http://zwfw.shaanxi.gov.cn/icity/govservice/newsnotice?s=5","http://zwfw.shaanxi.gov.cn/icity/govservice/newsnotice?s=6"],
#     "url_from":"list",
#     "method":"splash",
#     "headers":{},
#     "params":{},
#     "pipe":"redis",
#     "redis_name":"xian_xq",
#     "extract":[{
#         "name":"xian_xq",
#         "path":'//*[@id="zwdt-sheng-info"]/li/a/@href',
#         "method":'xpath',
#         "key":"urls",
#         "type":"list",
#         "value":"",
#         "pipe":"redis"
#         }]
#     }

# con={
#     #爬虫名称
#     "name":"xian_xq",
#     #起始url
#     "url":'http://zwfw.shaanxi.gov.cn//icity/icity/publishdetail?id=4a799699a650414f9573b297e25036d8',
#     #url怎么获取
#     "url_from":"redis",
#     #redis键
#     "redis_key":"xian_xq",
#     #拼接url前部
#     "url_host":"http://zwfw.shaanxi.gov.cn/",
#     #下载方法/GET/POST/splash
#     "method":"splash",
#     #请求头
#     "headers":{},
#     #url参数
#     "params":{},
#     #保存方法
#     "pipe":"mongo",
#     #monggo库
#     "mongo_name":"xian_xinwen",
#     #mongo表
#     "mongo_table":"table1",
#     #提取
#     "extract":[{
#         "name":"xian_xq",
#         #xpath路径
#         "path":'//*[@id="detailTitle"]/text()',
#         #提取方法/xpath/json/属性选择器
#         "method":'xpath',
#         #表名
#         "key":"titile",
#         "type":"str",
#         "value":"",
#         },
#         {
#             "name":"xian",
#             "path":'//*[@id="contentDetail"]/p/text()',
#             "method":'xpath',
#             "key":"contont",
#             "type":"str",
#             "value":""
#         },
#         {
#
#         #xpath路径
#         "path":'',
#         #提取方法/xpath/json/属性选择器
#         "method":'con_url',
#         #表名
#         "key":"url",
#         "type":"str",
#         "value":"",
#         },
#     ]
#     }

con1 = {
    "spider_name":"yangguang",
    "start_url":{
        "url_from":"list",
        "redis_key":"yangguang",
        "url_host":"my_http://zwfw.shaanxi.gov.cn/",
        "url":["http://wz.sun0769.com/political/index/politicsNewest"]
    },
    "method":"get",
    "headers": {},
    # url参数
    "params": {},
    "data":{},
    "save":{
        "pipe":"mongo",
        "mongo_name":"yangguang",
        "mongo_collection":"table1",
    },
    "extract":[{
        "name":"title",
        #xpath路径
        "path":'/html/body/div[2]/div[2]/div[4]/div[1]/ul/li[1]/span[3]/a/text()',
        #提取方法/xpath/json/属性选择器
        "method":'xpath',
        },
        {
        "name":"status",
        #xpath路径
        "path":'/html/body/div[2]/div[2]/div[4]/div[1]/ul/li[1]/span[2]/text()',
        #提取方法/xpath/json/属性选择器
        "method":'xpath',
        }
    ]
}
con = {
    "spider_name":"yangguang",
    "start_url":{
        "url_from":"list",
        "redis_key":"yangguang",
        "url_host":"my_http://zwfw.shaanxi.gov.cn/",
        "url":["http://wz.sun0769.com/political/index/politicsNewest"]
    },
    "host":"http://wz.sun0769.com/political",
    "method":"get",
    "headers": {},
    # url参数
    "params": {},
    "data":{},
    "save":{
        "pipe":"mongo",
        "mongo_name":"yangguang",
        "mongo_collection":"table1",
    },
    "extract":[
        {
            "form":"block_list",
            "method":"xpath",
            "path":"/html/body/div[2]/div[3]/ul[2]/li",
            "sub_data":[{
                "name":"title",
                #xpath路径
                "path":'./span[3]/a/text()',
                #提取方法/xpath/json/属性选择器
                "method":'xpath',
            },
            {
                "name":"status",
                #xpath路径
                "path":'./span[2]/text()',
                #提取方法/xpath/json/属性选择器
                "method":'xpath',
            },
            {
                "name": "time",
                # xpath路径
                "path": './span[5]/text()',
                # 提取方法/xpath/json/属性选择器
                "method": 'xpath',
            }
        ]
        },
        {
            "form":"url",
            "path":"//a[contains(@class,'prov_rota')]/@href"

        }
    ]
}
