#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import unittest


# 继承TestCase类，TestCase类是测试用例类

class Test1(unittest.TestCase):
    def setUp(self):
        print('hello')

    def tearDown(self):
        print('bye')

    def test_001(self):
        print('001')

    def test_002(self):
        print('002')

    def test_003(self):
        print('003')


if __name__ == '__main__':
    # 创建测试套件
    suit = TestCase()
    # 向测试套件中添加测试用例类
    # 定义一个测试用例列表
    case_list = ['test_001', 'test_002', 'test_003']
    for case in case_list:
        suit.addTest(Test1(case))
    # 运行测试用例，verbosity=2为每个测试用例输出报告。run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suit)

    # unittest.main()
