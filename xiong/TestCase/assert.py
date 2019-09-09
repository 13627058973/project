#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from unittest import TestCase

class Test(TestCase):
    def setUp(self):
        print('start')


    def tearDown(self):
        print('end')

    #判断预期值与实际值是否相等
    def test_001(self):
        self.assertEquals('1', '1')

    def test_002(self):
        self.assertEquals('2', '2')

