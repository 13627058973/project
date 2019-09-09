#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import time
import unittest
from HTMLTestRunner import HTMLTestRunner

case_dir = 'E:\PycharmProjects\hello\单元测试'  # 定义用例所在的路径
'''定义discover方法'''
discover = unittest.defaultTestLoader.discover(
    case_dir,
    pattern='test_*.py',
    top_level_dir=None
)
'''
1.case_dir即测试用例所在目录
2.pattern='test_*.py' ：表示用例文件名的匹配原则，“*”表示任意多个字符，这里表示匹配所有以test_开头的文件
3.top_level_dir=None：测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是放在多级目录
中），默认为 None
'''

if __name__ == '__main__':
    """直接加载discover"""
    # 方法一：
    '''
    fp = open('result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='测试情况'
                            )
    runner.run(discover)
      
    '''
    """通过把discover中的用例加载到测试套件"""
    # 方法二：

    suit = unittest.TestSuite()  # 创建一个测试集合
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    print(suit)  # 打印一下可以看到suite中添加了哪些测试用例
    fp = open('result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='测试情况'
                            )
    runner.run(suit)