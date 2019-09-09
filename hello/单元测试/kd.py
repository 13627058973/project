#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import requests


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.headers = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                            "63.0.3239.132Safari / 537.36 "
        }
        self.s = requests.session()

    def test_yunda(self):
        number = '1202247993797'
        kd = 'yunda'
        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html' % (number, kd)
        print(self.url)
        # 第一步发请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        result = r.json()
        # 第二步获取结果
        print(result['company'])  # 获取公司名称
        data = result['data']  # 获取data的数据
        print(data[0])  # 获取data的第一条数据
        get_result = data[0]['context']  # 获取已签收的状态
        print(get_result)
        # 断言：判断预期结果与实际结果
        self.assertEqual('韵达快递', result['company'])
        self.assertIn('已签收', get_result)

    def test_tiantian(self):
        number = '1202247993797'
        kd = 'tiantian'
        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html' % (number, kd)
        print(self.url)
        # 第一步发请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        result = r.json()
        # 第二步获取结果
        print(result['company'])  # 获取公司名称
        data = result['data']  # 获取data的数据
        print(data[0])  # 获取data的第一条数据
        get_result = data[0]['context']  # 获取已签收的状态
        print(get_result)
        # 断言：判断预期结果与实际结果
        self.assertEqual('天天快递', result['company'])
        self.assertIn('已签收', get_result)


if __name__ == '__main__':
    unittest.main()
