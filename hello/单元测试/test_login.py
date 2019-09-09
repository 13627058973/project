#!/usr/bin/python
# -*- coding:utf-8 -*-
import HTMLTestRunner
from unittest import TestCase, TestLoader, TextTestRunner
from 单元测试.login import login_check
from 单元测试.test import MyTestCase


class TestLogin(TestCase):

    def ttt_de(self):
        # 普通的方法
        pass

    def test_username_none(self):
        """ 测试用例，账号为空 """
        expected = '{"code":0,"msg":"账号不能为空"}'
        res = login_check(username=None, password='test')
        if res == expected:
            print('用例通过')
        else:
            print('用例不通过')

    def test_password_none(self):
        """ 密码为空 """
        expected = '{"code":0,"msg":"密码不能为空"}'
        res = login_check(username='python', password=None)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            result = '用例不通过'
            raise e
        else:
            result = '用例通过'
        finally:
            print(result)

    def test_succeed(self):
        """ 账号密码输入正确 """
        expected = '{"code":1,"msg":"登录成功"}'
        res = login_check(username='python', password='test')
        self.assertEqual(expected, res)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            result = '用例不通过'
            raise e
        else:
            result = '用例通过'
        finally:
            print(result)

    def test_error(self):
        """ 账号或者密码输入错误 """
        expected = '{"code":0,"mes":"账号或者密码不正确"}'
        res = login_check(username='python', password='t')
        self.assertEqual(expected, res)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            result = '用例不通过'
            raise e
        else:
            result = '用例通过'
        finally:
            print(result)


if __name__ == '__main__':
    suit = TestCase()
    loader = TestLoader()
    suit.addTest(loader.loadTestsFromModule(MyTestCase, TestLogin))
    runner = TextTestRunner()
    runner.run(suit)
