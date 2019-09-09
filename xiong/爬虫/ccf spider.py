#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import urllib.request
import xlwt
from selenium import webdriver


def get_url():
    for i in range(991):
        url = 'https://www.caichufang.com/esearch/goods-list.html?pageNo='
        url = url + str(i)
        get_good(url)


def get_good(url):
    driver = webdriver.Chrome()

    # option = webdriver.ChromeOptions()
    # option.add_argument('headless')  # 设置option
    # option.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(chrome_options=option)
    try:
        driver.get('https://www.caichufang.com')
        driver.implicitly_wait(30)
        driver.add_cookie({'name': 'SESSION', 'value': 'c55efd3c-2ebf-4576-9340-4fc136d781ba'})
        driver.get(url)
        infos = driver.find_elements_by_xpath('//*[@id="app"]/section/main/div/div[4]/ul')[0].text
        info = infos.split('\n')
        item = {}
        for i in range(len(info)):
            info = info[i]
            print(info)
    except:
        driver.close()






get_url()
