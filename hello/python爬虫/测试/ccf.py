#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from lxml import etree
import json


def get_url_list():  # 根据url地址的规律，构造url list
    url_list = []
    page = 1
    while page <= 113:
        return url_list
        page = page + 1
        if page > 113:
            break


def get_content_list(html_str):  # 3,提取数据
    html = etree.HTML(html_str)
    div_list = html.xpath("//div[@id='content-left']/div")
    content_list = []
    for div in div_list:
        item = {}
        item["author_name"] = div.xpath(".//h2/text()")[0].strip() if len(div.xpath(".//h2/text()")) > 0 else None
        item["content"] = div.xpath(".//div[@class='content']/span/text()")
        item["content"] = [i.strip() for i in item["content"]]
        item["stats_vote"] = div.xpath(".//div[@class='stats-vote']/i/text()")
        item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None
        item["stats_comments"] = div.xpath(".//span[@class='stats-comments']//i/text()")
        item["stats_comments"] = item["stats_comments"][0] if len(item["stats_comments"]) > 0 else None
        content_list.append(item)
    return content_list


def save_content_list(content_list):  # 4,保存
    with open("ccf.txt", "a", encoding='utf-8') as f:
        for content in content_list:
            f.write(json.dumps(content, ensure_ascii=False) + "\n")
            f.write("\n")
    print("保存成功")


class ccf_spider:

    def __init__(self):
        self.url_temp = "https://dian.ysbang.cn/index.html#%2Fsupplierstore.html%3FproviderId%3D42"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/63.0.3239.132 Safari/537.36"}

    def parse_url(self, url):
        print("now parsing: ", url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def run(self):  # 实现主要逻辑
        # 1，根据url地址的规律，构造url list
        url_list = get_url_list()
        # 2,发送请求 获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3,提取数据
            content_list = get_content_list(html_str)
            # 4，保存数据
            save_content_list(content_list)


if __name__ == '__main__':
    ccf = ccf_spider
    ccf.run()
