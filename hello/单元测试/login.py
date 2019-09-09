#!/usr/bin/env python
# -*- coding:utf-8 -*-


def login_check(username, password):
    if username is None:
        return '{"code":0,"msg":"账号不能为空"}'

    if password is None:
        return '{"code":0,"msg":"密码不能为空"}'

    if username == 'python' and password == "test":
        return '{"code":1,"msg":"登录成功"}'

    else:
        return '{"code":0,"mes":"账号或者密码不正确"}'


S = login_check("python", "test")
print(S)

number = '1202247993797'
kd = 'yoda'
url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html' % (number, kd)
print(url)
