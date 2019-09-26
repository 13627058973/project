#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

url = 'https://store.caichufang.com/supplier/login.html'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.maximize_window()
driver.add_cookie({'name': 'token', 'value': 'MmNiN2JhZDUtNzg4Zi00YzFlLThkYjItZWUyNDg1ODQzNDA36'})
driver.get('https://store.caichufang.com/supplier/index.html')
time.sleep(3)
