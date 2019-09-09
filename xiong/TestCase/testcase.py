#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
from busines.Login import Login
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')

    # 登录成功的情况
    def test_001(self):
        log = Login()
        # 正确账户密码登录
        log.login('hack_ai_buster', '1qaz2wsx#EDC')
        # 获取用于断言判断的登录后用户
        data = log.get_text('class', 'hd_login_name')
        # 进行断言判断
        self.assertEqual('hd_login_name', data)

    # 验证账号密码都不输入的 直接点击登录的情况
    def test_002(self):
        log = Login()
        # 账号密码都不输入的情况下
        log.login('', '')
        # 获取用于断言判断的登录后用户
        data = log.get_text('id', 'error_tips')
        # 进行断言判断
        self.assertEqual('请输入账号和密码', data)  # 前面是预期结果，后面是代码返回的实际结果

    # 输入账号，不输入密码
    def test_003(self):
        log = Login()
        # 输入账号，不输入密码
        log.login('aaaa', '')
        # 获取用于断言判断的登录后用户
        data = log.get_text('id', 'error_tips')
        # 进行断言判断
        self.assertEqual('请输入密码', data)

    # 输入账号,不输入密码(断言失败）
    # def test_004(self):
    #     log = Login()
    #     #输入账号，不输入密码
    #     log.login('aaaa', '')
    #     #获取用于断言判断的登录后用户
    #     data = log.get_text('id', 'error_tips')
    #     #进行断言判断
    #     self.assertEquals('请输入密码111', data)


if __name__ == '__main__':
    unittest.main()
