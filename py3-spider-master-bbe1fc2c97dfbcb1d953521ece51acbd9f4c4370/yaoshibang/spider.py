# coding:utf-8
import json
import threading
import time
import pymongo

import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import _thread
from lxml import etree

import ssl

from yiyaocheng.spider_category import get_category

ssl._create_default_https_context = ssl._create_unverified_context


def get_url(url):

    cookies = '_ga=GA1.2.1102168922.1554175937; Token=5adf987d9aae4e75aa73947e82e38cbe'
    headers = {
        # 'GET': url + ' HTTP/1.1',
        'Host': 'dian.ysbang.cn',
        'Connection': 'keep-alive',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://dian.ysbang.cn/supplierstore.html?v=0.8250431638952687&providerId=498',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookies,
    }
    request = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(request)  # 打开网页
    return page.read()  # 读取页面源码




def write_csv(list,):
    columns = ['供应商名称', '商品名称', '生产厂家', '销售价', '有效期','规格', '销量']
    csvfile = pd.DataFrame(columns=columns, data=list)  # 打开方式还可以使用file对象
    csvfile.to_csv('药师帮.csv', index=False, encoding='utf-8')


def get_current_category_item_list():
    items = []
    # 得到类别code
    total = 333
    for i in range(total):
        page = i + 1
        print(str(page) + '/' + str(total))
        url = 'https://dian.ysbang.cn/wholesale-drug/sales/getWholesaleList/v4110'
        cookies = '__guid=140493094.703276529043041200.1555490681782.6792; Token=2d71445c8b624347941cbb84d4963e4d; monitor_count=7';
        headers = {
            # 'GET': url + ' HTTP/1.1',
            'Host': 'dian.ysbang.cn',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://dian.ysbang.cn/supplierstore.html?v=0.1181111242048094&providerId=498',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': cookies,
        }
        params = {
            "platform": "pc",
            "version": "pc4.15.0",
            "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36 Chrome 73",
            "page": str(page),
            "pagesize": 60,
            "operationtype": 2,
            "provider_id": 1790,
            "mustStockAvailable": 0,
            "sort": "默认",
            "classify_id": "",
            "tagId": "",
            "searchkey": "",
            "onSale": "",
            "factoryNames": ""
        }

        params = json.dumps(params)
        res = requests.post(url, data=params, headers=headers)
        res = res.json()
        item = res['data']['wholesales']
        for item_index in range(len(item)):
            item_index = item[item_index]
            try:
                detail = [
                    str(item['provider_name']),  # 供应商名称
                    str(item['cn_name']),  # 商品名称
                    str(item['manufacturer']),  # 生产厂家
                    str(item['chainPrice']),  # 销售价
                    str(item['valid_date']),  # 有效期
                    str(item['specification']),# 规格
                    str(item['total'])  # 销量
                ]
                items.append(detail)
            except BaseException as e:
                print(e)
    write_csv(items)



# main入口
category_list = get_category()
page_list = []
try:
    get_current_category_item_list()
except BaseException as e:
    print(e)

