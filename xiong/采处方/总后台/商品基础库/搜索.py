#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from Commonlib.commonlib import Commonshare
# 导入下拉框select
from selenium.webdriver.support.select import Select
# 导入键盘操作
from selenium.webdriver.common.keys import Keys
import random


# 商品基础库(页面内容的搜索）

class Search_goods(Commonshare):
    def create_goods(self):
        self.driver.implicitly_wait(5)
        # 打开采处方
        self.open_url('http://test2admin.caichufang.com/admin/login.html')
        # 添加token 跳过登录
        # self.driver.add_cookie({'name': 'SESSION', 'value': '0b7b1da4260e3fd9b7890520f035c290|1568253708|1568253627'})
        # self.open_url('https://admin.caichufang.com/admin/index.html')
        self.input_data('id', 'userName', 'ccf_super_admin')
        self.input_data('id', 'userPwd', 'caichufang2017')
        self.input_data('id', 'loginCaptcha', '0809')
        self.click('xpath', '/html/body/div/div[2]/div/form/div[4]/input')
        # 获取商品基础库元素，并进行点击
        self.click('xpath', '/html/body/div/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[1]/div/a/div[2]')
        # 进入镶嵌页面iframe
        iframe = self.driver.find_element_by_name('inner')
        self.driver.switch_to_frame(iframe)
        # 进入输入框
        self.input_data('name', 'goodsBasicName', '脑络通')
        # 点击查询
        self.click('xpath', '/html/body/div[1]/div/form/div/div/div[2]/div/button[1]')
        # 定位一级分类 二级分类, 分类设置随机数
        a = random.randint(1, 14)
        goods_class_one = self.driver.find_element_by_id('oneClass')
        Select(goods_class_one).select_by_index(a)
        goods_class_one.click()
        goods_class_two = self.driver.find_elements_by_id('twoClass')
        for i in range(len(goods_class_two)):
            two_class = goods_class_two[i]
            print(two_class.text)
            b = random.randint(0, 3)
            Select(two_class).select_by_index(b)
        # 键盘操作
        key = self.driver.find_element_by_name('goodsBasicName')
        key.send_keys(Keys.CONTROL, 'a')
        key.send_keys(Keys.BACKSPACE)
        self.click('xpath', '/html/body/div[1]/div/form/div/div/div[2]/div/button[1]')
        self.click('text', '编辑')
        for i in range(10):
            js = 'window.scrollTo(0,%s)' % (i * 100)
            self.driver.execute_script(js)
        self.click('class', 'btn-primary')
        time.sleep(10)


if __name__ == '__main__':
    good = Search_goods()
    good.create_goods()
