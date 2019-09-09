#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#  九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(j, i, i * j), end='')
    print()

#  阶乘实例

#  获取用户的数字
num = int(input("请输入数字:"))
factorial = 1

# 查看输入的数字是负数 ，0 ，正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0的阶乘为1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("%d的阶乘为%d" % (num, factorial))
