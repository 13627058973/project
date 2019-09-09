#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

class common(object):
    # 初始化方法
    def __init__(self):
        # 创建浏览器对象
        self.driver = webdriver.Chrome()
        # 使浏览器最大化
        self.driver.maximize_window()
        # 隐形等待
        self.driver.implicitly_wait(3)

    def open_url(self, url):
        # 请求站点
        self.driver.get(url)
        time.sleep(3)

    def locateElement(self, locate_type, value):
        # 封装八种定位方法
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el = self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'tag':
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == 'text':
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == 'xpath':
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el = self.driver.find_element_by_css_selector(value)

        # 返回定位到元素，才返回元素
        if el is not None:
            return el

    # 对点击元素的封装
    def click(self, locate_type, value):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()

    # 直接对定位到的元素进行文本输入
    def input_data(self, locate_type, value, data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.send_keys(data)

    # 获取定位到的元素中的文本内容 <a>xxx</a>
    def get_text(self, locate_type, value):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.text

    # 获取定位到的元素中的标签属性
    def get_attribut(self, locate_type, value, data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        return el.get_attribute(data)

    # 收尾清理方法
    def __del__(self):
        time.sleep(3)
        self.driver.close()

if __name__ == '__main__':
    com = common()
    com.open_url('http://www.baidu.com')