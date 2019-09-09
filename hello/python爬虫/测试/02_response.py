#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json
import requests
from lxml import etree

url = "https://dian.ysbang.cn/index.html#%2Fsupplierstore.html%3FproviderId%3D42"

data = {"platform": "pc",
        "version": "pc4.15.0",
        "classify_id": "",
        "factoryNames": "",
        "mustStockAvailable": 0,
        "onSale": "",
        "operationtype": 2,
        "page": 1,
        "pagesize": 60,
        "platform": "pc",
        "provider_id": 42,
        "searchkey": "",
        "sort": "默认",
        "tagId": "",
        "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
              "Safari/537.36 Chrome 73",
        "version": "pc4.15.0"
        }

headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9",
           "Connection": "keep-alive",
           "Content-Length": "335",
           "Content-Type": "application/json;charset=UTF-8",
           "Cookie": "_ga=GA1.2.1102168922.1554175937; Token=ca0dd8e550d5440fae4ecab9065ced8d",
           "Host": "dian.ysbang.cn",
           "Origin": "https://dian.ysbang.cn",
           "Referer": "https://dian.ysbang.cn/supplierstore.html?v=0.033553484649122334&providerId=42",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/73.0.3683.86 Safari/537.36",
           "X-Requested-With": "XMLHttpRequest"}

response = requests.get(url, data=data, headers=headers)

# 新建一个html文件 并打开
# with open("采处方.html","w",encoding="utf-8") as f:
#    f.write(response.content.decode())
# response.encoding ="utf-8"
json_str = response.content.decode()

print(json_str)
