#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time


browers = webdriver.Chrome()

browers.get('http://www.baidu.com')
# browers.add_cookie({'name': 'Token', 'value': 'd671e63a-54e5-48d5-b9ab-9442ec642e32'})
browers.get("https://admin.caichufang.com/index.html")
