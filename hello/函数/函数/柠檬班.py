#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql


class Boss(object):
    """Boss类"""
    def __init__(self, money, goods):
        self.monkey = money
        self.goods = goods
        self.emp_list = []

    def add_list(self, emp):
        """雇员工的方法"""
        self.emp_list.append(emp)
        print(self.emp_list)

    def sale(self):
        """卖产品的方法"""
        self.monkey += self.goods*10
        print(self.money)


class Employee(object):

    def __init__(self):
        self.skill = 300

    def work(self, boos):
        """员工工作"""
        boos.goods += self.skill*12
        boos.money -= 2000*12
        if not self.skill == 500:
            self.skill += 50


def main(year):
    """计算boss金钱的函数"""
    # 创建一个Boss
    boos = Boss(10000, 1)
    # 设置一个for循环来控制，员工的雇佣，每年增加一个员工
    for i in range(year):
        '''创建一个员工，加入到老板的雇佣列表中'''
        emp = Employee()
        boos.add_list(emp)
        # 遍历所有的员工，开始工作
        for emp in boos.emp_list:
            emp.work(boos)

    # 卖出商品
    boos.sale()
    print(boos.money)
