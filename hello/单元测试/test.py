#!/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner


class MyTestCase(unittest.TestCase):

    def test_01(self):
        """判断 a ==b """
        a = 1
        b = 1
        self.assertAlmostEqual(a, b)

    def test_03(self):
        """判断 a in b """
        a = "hello"
        b = "hello word"
        self.assertIn(a, b)

    def test_02(self):
        """判断 a is True"""
        a = True
        self.assertTrue(a)

    def test_04(self):
        """失败案例"""
        a = "熊"
        b = "熊"
        self.assertAlmostEqual(a, b, msg="失败原因: %s != %s" % (a, b))


if __name__ == '__main__':
    test_suit = unittest.TestSuite()  # 创建一个测试集合
    # test_suit.addTest(MyTestCase('test_04'))  # 测试套件中添加测试用例
    test_suit.addTest(unittest.makeSuite(MyTestCase))  # 使用makeSuite方法添加所有的测试方法
    fp = open('res.html', 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='测试报告',
                                           description='测试描述',
                                           verbosity=2
                                           )  # 生成测试用例的对象
    runner.run(test_suit)
    # unittest.main()
