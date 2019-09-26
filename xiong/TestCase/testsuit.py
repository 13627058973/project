#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest
from TestCase.mytest import TestCase
import HTMLTestRunner


class Test(unittest.TestCase):
    def test_suit(self):
        # 创建测试套件
        mysuit = unittest.TestSuite()

        # 向测试套件中添加测试用例
        case_list = ['test_001', 'test_002', 'test_003', 'test_004']
        for case in case_list:
            mysuit.addTest(case)
        # 使用runner运行测试用例
        # unittest.TextTestRunner(verbosity=2).run(myst)       # verbosity=2 生成测试报告

        # 生成html格式测试报告的步骤
        with open('../report.html', 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(
                strram=f,  # 设定测试数据写入那个文件
                title='第一个测试报告',  # 设定测试报告标题
                description='软件测试第一期',  # 设定测试报告的描述
                verbosity=2
            ).run(mysuit)


if __name__ == '__main__':
    unittest.main()
