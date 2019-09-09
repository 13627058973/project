#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver

# webdriver.Chrome().get('http://www.baidu.com')
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")   # 打开百度首页

seek_input = browser.find_element_by_id("kw")  # 通过ID找网页的标签，找到搜索框的标签

seek_input.send_keys("饮料")  # 设置搜索的内容

seek_but = browser.find_element_by_id("sb")  # 找到搜索文档按钮

seek_but.click()  # 点击搜索文档按钮







