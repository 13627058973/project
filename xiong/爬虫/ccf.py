#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import time
from lxml import etree
import urllib
from bs4 import BeautifulSoup



def get_url():
    for i in range(861):
        url = 'https://www.caichufang.com/esearch/goods-list.html?pageNo='
        url = url + str(i)
    header = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'SESSION=c55efd3c-2ebf-4576-9340-4fc136d781ba; SERVERID=08b6fa607352e9ab3aa82a650dfdd1ad|1563958528|1563949670',
        'origin': 'https://www.caichufang.com',
        'referer': 'https://www.caichufang.com/esearch/goods-list.html?pageNo=0&key=RECOMMEND&goodsAvailable=false&allInActivity=false&value=1&newGoods=false&goodsClassIds=&storeIds=&factoryIds=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=header)
    page = urllib.request.urlopen(request)  # 打开网页
    return page.read()  # 读取页面源码


def get_good():
    html = get_url()
    selector = etree.HTML(html.text)
    infos = selector.xpath('//*[@id="app"]/section/main/div/div[4]/ul/li[1]/div/p')
    print(infos)


get_url()

