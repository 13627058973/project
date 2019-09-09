#!/usr/bin/env python 
# -*- coding:utf-8 -*-

a=1.2
print(int(a))
print("我叫%s 今年%d岁！"%('小明',10))
a,b =0,1
while b<10:
    print(b)
    a,b =b,a+b

age=int(input("请输入你狗狗的年龄:"))
print("")
if age <0:
    print("你在逗我吧！")
elif age ==1:
    print("相当于14岁的人")
elif age ==2:
    print("相当于22岁的人")
elif age >2:
    human=22+(age-2)*5
    print("对应人类的年龄：",human)

# 退出提示
input("点击enter键退出")

number=7
guess=-1
print("数字猜谜游戏！")
while guess !=number:
    guess =int(input("输入数字"))
    if guess==number:
        print("恭喜你猜对了")
    elif guess<number:
        print("你猜的数字小了")
    elif guess>number:
        print("你猜的数字大了")

