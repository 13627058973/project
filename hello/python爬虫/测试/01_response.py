#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests

url = "https://www.caichufang.com/esearch/goods-list.html"

data = {"pageNo": "1",
        "key": "RECOMMEND", "goodsAvailable": "false", "allInActivity": "false", "value": "1",
        "afterKey": "",
        "allInActivity": "false",
        "factoryIds": [],
        "goodsAvailable": "false",
        "goodsClassIds": [],
        "key": "RECOMMEND",
        "newGoods": "false",
        "pageNo": "1",
        "storeIds": []
        }

headers = {"authority": "www.caichufang.com",
           "method": "POST",
           "path": "/index/goodsClassList.json",
           "scheme": "https",
           "accept": "application/json, text/plain, */*",
           "accept-encoding": "gzip, deflate, br",
           "accept-language": "zh-CN,zh;q=0.9",
           "content-length": "2",
           "content-type": "application/json",
           "cookie": "SESSION=4a02c12a-d495-444e-8ccd-024939cdfbbb; "
                     "SERVERID=08b6fa607352e9ab3aa82a650dfdd1ad|1555234038|1555221893",
           "origin": "https://www.caichufang.com",
           "referer": "https://www.caichufang.com/esearch/goods-list.html?pageNo=1&key=RECOMMEND&goodsAvailable=false"
                      "&allInActivity=false&value=1&newGoods=false&goodsClassIds=&storeIds=&factoryIds=",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/73.0.3683.86 Safari/537.36"}

response = requests.get(url, data=data, headers=headers)

print(response.content.decode())

print(type(response.content.decode()))
