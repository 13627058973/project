#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import cmath
#  三角形的三个边分别是 a,b,c 且  任意两边加起来大于第三边
a = float(input("输入三角形第一边长:"))
b = float(input("输入三角形第二边长:"))
c = float(input("输入三角形第三边长:"))

s = (a+b+c)/2

#    面积数据以浮点数float显示:
#   area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#   print('三角形面积为 %0.2f' %area)


#  面积不规定格式
area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print("结果为{0}".format(area))

