#!/usr/bin/env python 
# -*- coding:utf-8 -*-

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
import xlwt
from selenium import webdriver

info = []


# def get_store():
#     total = 58
#     for i in range(total):
#         page = i+1
#         #print(str(page) + '/' + str(total))
#         url = "https://dian.ysbang.cn/ysb-provider/provider/getBrandList/v3110"
#         headers = {
#             "Accept": "application/json, text/javascript, */*; q=0.01",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Connection": "keep-alive",
#             "Content-Length": "301",
#             "Content-Type": "application/json;charset=UTF-8",
#             "Cookie": "_ga=GA1.2.1102168922.1554175937; Token=bc263e57fd4f4264b710d606f23e0cc7",
#             "Host": "dian.ysbang.cn",
#             "Origin": "https://dian.ysbang.cn",
#             "Referer": "https://dian.ysbang.cn/brands.html?v=0.41764446864158256",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
#             "X-Requested-With": "XMLHttpRequest"
#         }
#
#         params = {
#             "platform": "pc",
#             "version": "pc4.15.0",
#             "businessScope": -1,
#             "cuxiao": 0,
#             "minAmount": 0,
#             "orderBy": 0,
#             "page": str(page),
#             "pageSize": 12,
#             "platform": "pc",
#             "quan": 0,
#             "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36 Chrome 74",
#             "usertoken": "bc263e57fd4f4264b710d606f23e0cc7"
#         }
#
#         params = json.dumps(params)
#         req = requests.post(url, data=params, headers=headers).content.decode()
#         req = json.loads(req)
#         # print(req)
#         req = req['data']['providers']
#         for store_list in range(len(req)):
#             provider_id = req[store_list]['provider_id']
#             provider_name = req[store_list]['provider_name']
#             print("店铺名:",provider_name)
#             inware = req[store_list]['inware']
#             get_store_good(provider_id, inware, provider_name)

def get_store_good():
    items = []
    # 得到类别code
    total = 55
    for i in range(total):
        page = i + 1
        page = page + int(10)
        url = 'https://dian.ysbang.cn/wholesale-drug/sales/getWholesaleList/v4110'
        cookies = 'Token=bba9afa8e93c49d7a7d401d1a05c57d8'
        headers = {
            # 'GET': url + ' HTTP/1.1',
            'Host': 'dian.ysbang.cn',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Referer': 'https://dian.ysbang.cn/supplierstore.html?v=4.24&providerId=1322',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': cookies,
        }
        params = {
            "platform": "pc",
            "version": "pc4.15.0",
            "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                  "Safari/537.36 Chrome 73",
            "page": str(page),
            "pagesize": 60,
            "operationtype": 2,
            "provider_id": 2071,
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
        good = res['data']['wholesales']
        for b in range(len(good)):
            goods_id = good[b]['wholesaleid']
            goods_name = good[b]['cn_name']
            specification = good[b]['specification']
            unit = good[b]['unit']
            manufacturer = good[b]['manufacturer']

            goods_id = str(goods_id)
            # url2 = 'https://dian.ysbang.cn/index.html#%2Fdrug_info.html%3Fwholesaleid%3D849523%26pid%3D672%26isSeckill%3Dfalse'
            url2 = 'https://dian.ysbang.cn/index.html#%2Fdrug_info.html%3Fwholesaleid%3D'
            url3 = '%26pid%3D'
            url4 = '%26isSeckill%3Dfalse'
            url5 = url2 + goods_id + url3 + str(1790) + url4
            print(str(b + 1) + '/' + str(len(good)))
            selenium(url5)


def selenium(url5):
    # driver = webdriver.Chrome()
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 设置option
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=option)

    driver.get('https://dian.ysbang.cn/login.html')

    driver.add_cookie({'name': 'Token', 'value': 'bba9afa8e93c49d7a7d401d1a05c57d8'})
    driver.get(url5)
    driver.implicitly_wait(30)
    iframe = driver.find_element_by_id('pageContent')
    driver.switch_to.frame(iframe)
    try:
        result = driver.find_elements_by_xpath('//div[@id="drugInfoDIV"]/div[2]')[0].text
    except:
        result = driver.find_elements_by_xpath('//div[@id="drugInfoDIV"]/div[1]')[0].text
    result_array = result.split('\n')
    info_dict = {}
    # info_dict['店铺名称'] = provider_name
    for i in range(int(len(result_array) / 2)):
        name_index = 2 * i
        desc_index = name_index + 1
        name = result_array[name_index]
        name = name[1:][:-1]
        desc = result_array[desc_index]
        info_dict[name] = desc

    info_text = []
    # 店铺名称
    # try:
    #     info_text.append(info_dict['店铺名称'])
    # except:
    #     info_text.append('')
    # try:
    #     info_text.append(info_dict['套餐药品信息'])
    # except:
    #     info_text.append('')
    # 商品名称
    try:
        info_text.append(info_dict['商品名称'])
    except:
        info_text.append('')
    # 规格包装
    try:
        info_text.append(info_dict['规格包装'])
    except:
        info_text.append('')
    # 厂家
    try:
        info_text.append(info_dict['厂家'])
    except:
        info_text.append('')
    # 功能主治
    try:
        info_text.append(info_dict['功能主治'])
    except:
        info_text.append('')
    # 成分
    try:
        info_text.append(info_dict['成分'])
    except:
        info_text.append('')
    # 用法用量
    try:
        info_text.append(info_dict['用法用量'])
    except:
        info_text.append('')
    # 不良反应
    try:
        info_text.append(info_dict['不良反应'])
    except:
        info_text.append('')
    # 注意事项
    try:
        info_text.append(info_dict['注意事项'])
    except:
        info_text.append('')
    # 禁忌
    try:
        info_text.append(info_dict['禁忌'])
    except:
        info_text.append('')

    info.append(info_text)
    save(info)


def save(info):
    header = ['商品名称', '规格', '厂家', '功能主治', '成分', '用法用量', '不良反应', '注意事项', '禁忌']
    book = xlwt.Workbook(encoding='utf-8')  # 新建一个工作簿
    sheet = book.add_sheet('sheet1')  # 在工作簿中新建一个表格
    for h in range(len(header)):
        sheet.write(0, h, header[h])  # 写入header的标题
    i = 1

    for List in info:
        j = 0
        for data in List:
            sheet.write(i, j, data)
            j += 1
        i += 1

        book.save('E:/晋实惠.xls')


get_store_good()
