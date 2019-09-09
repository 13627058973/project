#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from Commonlib.commonlib import Commonshare
import time


class Login(Commonshare):
    def login(self, user, pwd):
        # 跳转到一号店
        self.open_url('http://www.yhd.com')
        # 定位到登录按钮进行点击，点击之后进入一号店登录界面
        self.click('class', 'hd_login_link')
        # 定位并输入数据
        self.input_data('id', 'un', user)
        time.sleep(5)
        # 定位并输入密码
        self.input_data('id', 'pwd', pwd)
        time.sleep(5)
        # 点击登录按钮
        self.click('id', 'login_button')


if __name__ == '__main__':
    log = Login()
    log.login('hack_ai_buster', '1qaz2wsx#EDC')

