#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import re

# 获取client
from docutils.parsers import null

url = 'http://test2app.caichufang.com/auth/client'
client = requests.post(url)
# print(client.text)
client = client.json()
# 提取client,通过json提取
client = client['data']['client']
# 提取client，通过正则提取
# t = re.findall()
print(client)

# 登录app,
url_0 = 'http://test2app.caichufang.com/auth/token'
body = {
    'client': client,
    'username': '13627058973',
    'password': '123456',
    'captcha': ''
}

logon = requests.post(url_0, data=body)
print(logon.text)
