#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#  二次方程的计算  计算X的值

#  二次方程式：ax**2 + bx +c =0
#  a,b,c用户提供，为实数，a != 0
#  X的计算公式

#  X = -b -(b**2-4ac)**0.5/(2a)
#  X = -b + (b**2-4ac)**0.5/(2a)

#  导入函数 cmath(复杂数学运算) 模块
import cmath

a = float(input("输入a :"))
b = float(input("输入b :"))
c = float(input("输入c :"))
#  计算
d = (b**2) - (4*a*c)

#  两种求解方法
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为{0}和{1}'.format(sol1, sol2))


