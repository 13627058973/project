#!/usr/bin/env python 
# -*- coding:utf-8 -*-

a = 21
b = 10
c = 0

c = a + b   #	加 - 两个对象相加
print("1 - c 的值为：", c)

c = a - b   #	减 - 得到负数或是一个数减去另一个数
print("2 - c 的值为：", c)

c = a * b  #  乘 - 两个数相乘或是返回一个被重复若干次的字符串
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b  # 取模 - 返回除法的余数
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b  #	幂 - 返回x的y次幂
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b  #	取整除 - 向下取接近除数的整数
print("7 - c 的值为：", c)

a = 21
b = 10
c = 0

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)