#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import pprint

login_url = 'http://test2app.caichufang.com/auth/token'
body = {
    'client': "dc57jcu43yj5swtf53948fpj7lvqo0x4",
    'username': '17688896421',
    'password': '123456',
    'captcha': ''
}
s = requests.session()
r = s.post(login_url, data=body)
print(r.json())
token = r.json()['data']['token']

firm_url = 'http://test2app.caichufang.com/purchaser/details.json'
r1 = s.post(firm_url)
print(r1.json())


url = "http://test2app.caichufang.com/cart/addGoodsTCart.json"
headers = {
    "token": token,
    "username": "17688896421",
    "Content-Type": "application/json"
}
param = {
    "content": {
        "goodsId": "870eq48s6f6u",
        "quantity": 0
    }
}
a = json.dumps(param)
response = requests.post(url, headers=headers, data=a)
print(response.text)

