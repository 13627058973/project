# coding:utf-8
import threading
import time

import pandas as pd
from bs4 import BeautifulSoup
import requests
import urllib
import _thread

import ssl

from yiyaocheng.spider_category import get_category

ssl._create_default_https_context = ssl._create_unverified_context


def get_html(url):
    cookies = 'siteId=440000; siteName=%E5%B9%BF%E4%B8%9C; NTKF_T2D_CLIENTID=guest35663013-C2A4-D4A1-49C2-50DF47C348C5; JSESSIONID=0276096A04C0084BB11BFCA389223; ycuserType=%E6%89%B9%E5%8F%91%E4%BC%81%E4%B8%9A; yctoken=""; ycusername=18665036778; yccity_id=440000; ycavatarUrl=%2Ffky%2Fimg%2Ftest%2FappUpload151056161029832.jpg; ycgltoken=eEFxTXRWaDRNVGVUM3gxTk9OM2lNTi81TG1qUm9pYXRUWktYRFFJbVRTbExJMUhoNFVhNTFxeHhVY09pWHZya2gzb1FmNHNqTHRFS2xuQWh3S2lzd1hxUmF1V1lhNjR4T0l6bHZ2VUNkSXFsZlhxYmF4QUwxWmYyQkI3REM5ZUtDS2VZUlc3aEpTei9SREJDdnV1TEJQZU95UjBFdWo2OTMwKy9kM2hMMm4yLzhRODN3VW53eFZPUWwwczEvTlRmP2FwcElkPTEyNTAma2V5SWQ9MTI1MA%3D%3D; yc_pass_gltoken=eEFxTXRWaDRNVGVUM3gxTk9OM2lNTi81TG1qUm9pYXRUWktYRFFJbVRTbExJMUhoNFVhNTFxeHhVY09pWHZya2gzb1FmNHNqTHRFS2xuQWh3S2lzd1hxUmF1V1lhNjR4T0l6bHZ2VUNkSXFsZlhxYmF4QUwxWmYyQkI3REM5ZUtDS2VZUlc3aEpTei9SREJDdnV1TEJQZU95UjBFdWo2OTMwKy9kM2hMMm4yLzhRODN3VW53eFZPUWwwczEvTlRmP2FwcElkPTEyNTAma2V5SWQ9MTI1MA%3D%3D; ycenterpriseName=%E5%B9%BF%E5%B7%9E%E5%B8%82%E5%B7%A8%E5%AD%9A%E8%BE%BE%E5%8C%BB%E8%8D%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; loginType=1; ycstationName=%E5%B9%BF%E4%B8%9C; ycenterpriseId=101223; ycroleId=301; ycresult=""; pc_userToken=5910bc475e2b336574aca0fd3e022962; pc_userName=18665036778; ycroleType=""; ycuserId=101223; ycstation=440000; mobile=""; nameList=%E5%B9%BF%E5%B7%9E%E5%B8%82%E5%B7%A8%E5%AD%9A%E8%BE%BE%E5%8C%BB%E8%8D%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; ycuserinfo=%7B%22ycenterpriseId%22%3A%22101223%22%7D; Hm_lvt_cc3a4282864d3f8e912d9c37b914ed23=1551839780,1551840318,1551843991; UUID=6fb6576201b7ac4d51888231c37f7ccb; Hm_lpvt_cc3a4282864d3f8e912d9c37b914ed23=1551843997; nTalk_CACHE_DATA={uid:yp_1000_ISME9754_guest35663013-C2A4-D4,tid:1551853660498589}; JSESSIONID=4916455CF8FBD2A25FDE9652675C6A6C; cururl=http%3A%2F%2Fmall.yaoex.com%2Fproduct%2FproductDetail%2F142ABHH190024%2F8353'
    headers = {
        # 'GET': url + ' HTTP/1.1',
        # 'Host': 'www.xty999.com',
        # 'Proxy-Connection': 'keep-alive',
        # 'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 QQBrowser/4.4.105.400',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Referer': 'http://www.xty999.com/index.html',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookies,
    }
    request = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(request)  # 打开网页
    return page.read()  # 读取页面源码


def write_csv(list, name, code):
    columns = ['通用名', '商品名称', '规格', '箱规', '国药准字', '厂家', '供应商', '是否有活动']
    csvfile = pd.DataFrame(columns=columns, data=list)  # 打开方式还可以使用file对象
    csvfile.to_csv('1药城_' + name + '_' + str(code) + '.csv', index=False, encoding='utf-8')


def get_item_detail(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    # 通用名
    name = soup.find('div', {'class': 'product-inner fl'}).findAll('h3')[0].text.replace('\n', '').replace('\t', '')
    # 商品名称
    goods_name = soup.find('div', {'class': 'product-info'}).findAll('li')[1].text[4:]
    # 规格
    standard = soup.find('div', {'class': 'product-info'}).findAll('li')[0].text[3:]
    # 箱规
    box_standard = soup.find('div', {'class': 'product-info'}).findAll('li')[7].text[6:]
    # 国药准字
    approval_number = soup.find('div', {'class': 'product-info'}).findAll('li')[4].text[5:]
    # 厂家
    factory = soup.find('div', {'class': 'product-info'}).findAll('li')[2].text[5:]
    # 供应商
    supplier = soup.find('div', {'class': 'p-suppliers'}).next[4:]
    # 是否有活动
    activity = soup.find('span', {'class': 'p_price fl'}) is not None
    if activity:
        activity = '有'
    else:
        activity = '无'
    return [
        name, goods_name, standard, box_standard, approval_number, factory, supplier, activity
    ]


def get_current_category_item_list(code, name):
    items = []
    # 得到类别code
    url = 'http://gateway-b2b.fangkuaiyi.com/api/search/searchProductList?tradername=yaoex_pc&trader=pc&closesignature=yes&signature_method=md5&signature=****&timestamp=1551852418720&token=eEFxTXRWaDRNVGVUM3gxTk9OM2lNTi81TG1qUm9pYXRUWktYRFFJbVRTbExJMUhoNFVhNTFxeHhVY09pWHZya2gzb1FmNHNqTHRFS2xuQWh3S2lzd1hxUmF1V1lhNjR4T0l6bHZ2VUNkSXFsZlhxYmF4QUwxWmYyQkI3REM5ZUtDS2VZUlc3aEpTei9SREJDdnV1TEJQZU95UjBFdWo2OTMwKy9kM2hMMm4yLzhRODN3VW53eFZPUWwwczEvTlRmP2FwcElkPTEyNTAma2V5SWQ9MTI1MA%3D%3D&inputCharset=utf-8&charsetColumns=keyword&keyword=&decodeKeyword=&userId=101223&roleId=301&userType=%E6%89%B9%E5%8F%91%E4%BC%81%E4%B8%9A&buyerCode=101223&sellerCode=&spuCode=&haveGoodsTag=false&promotionTag=false&buyerHistoryTag=false&templateId=&factoryIds=&sellerCodes=&sortColumn=default&sortMode=desc&per=10&invokeType=&drugName=&factoryName=&spec=&sellerName=&product2ndLMCode=' + code + '&nowPage=1'
    res = requests.get(url)
    res = res.json()
    pageCount = 0
    try:
        pageCount = res['data']['pageCount']
    except BaseException as e:
        pageCount = 0
    total = int(pageCount)
    for i in range(total):
        # if i < 0:
        #     continue;
        print(str(i) + '/' + str(total) + '   ' + name + code + '\n')
        page = i + 1
        url = 'http://gateway-b2b.fangkuaiyi.com/api/search/searchProductList?tradername=yaoex_pc&trader=pc&closesignature=yes&signature_method=md5&signature=****&timestamp=1551852418720&token=eEFxTXRWaDRNVGVUM3gxTk9OM2lNTi81TG1qUm9pYXRUWktYRFFJbVRTbExJMUhoNFVhNTFxeHhVY09pWHZya2gzb1FmNHNqTHRFS2xuQWh3S2lzd1hxUmF1V1lhNjR4T0l6bHZ2VUNkSXFsZlhxYmF4QUwxWmYyQkI3REM5ZUtDS2VZUlc3aEpTei9SREJDdnV1TEJQZU95UjBFdWo2OTMwKy9kM2hMMm4yLzhRODN3VW53eFZPUWwwczEvTlRmP2FwcElkPTEyNTAma2V5SWQ9MTI1MA%3D%3D&inputCharset=utf-8&charsetColumns=keyword&keyword=&decodeKeyword=&userId=101223&roleId=301&userType=%E6%89%B9%E5%8F%91%E4%BC%81%E4%B8%9A&buyerCode=101223&sellerCode=&spuCode=&haveGoodsTag=false&promotionTag=false&buyerHistoryTag=false&templateId=&factoryIds=&sellerCodes=&sortColumn=default&sortMode=desc&per=10&invokeType=&drugName=&factoryName=&spec=&sellerName=&product2ndLMCode=' + code + '&nowPage=' + str(
            page)
        res = requests.get(url)
        res = res.json()
        item_list = res['data']['shopProducts']
        for item_index in range(len(item_list)):
            item = item_list[item_index]
            try:
                detail = get_item_detail(
                    'http://mall.yaoex.com/product/productDetail/' + item['spuCode'] + '/' + item['vendorId'])
                items.append(detail)
            except BaseException as e:
                print(e)
    write_csv(items, name, code)


# main入口
category_list = get_category()
page_list = []
for category_index in range(len(category_list)):
    category = category_list[category_index]
    time.sleep(1)
    get_current_category_item_list(category['code'], category['name'])
    try:
        # t = threading.Thread(target=get_current_category_item_list, args=(category['code'], category['name']))
        # t.start()
        get_current_category_item_list(category['code'], category['name'])
    except BaseException as e:
        print(e)
