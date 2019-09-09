#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import urllib.request
import json
import requests
import xlwt,xlrd


# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
print(type(response.status_code),response.status_code)


