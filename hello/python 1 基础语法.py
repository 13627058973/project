#!/usr/bin/env python 
# -*- coding:utf-8 -*-

print('1') #打印数字1，单行注释
'''
str = input("请输入") #多行注释
print("你输入的值是：",str)
'''
#行与缩进
'''
if True:
    print ("true")
    print ("answer")
else:
    print ("false")
    print ("answer")

# 语句过长，使用反斜杆（\）来实现多行语句
tolal = item_one +\
        item_two +\
        item_three

str='runoob'
print(str) #输出字符串
print(str[0:-1]) #输出第一到倒数第二个的字符串
print(str[0]) #输出第一个字符串
print(str[2:5]) #输出第三个到第五个的字符串
print(str[2:]) #输出第三个到最后的字符串
print(str * 2) #输出字符串两次
print(str + '你好') #连接字符串

print('.................')
print('hello\nrunoob') #使用反斜杆(\)+n转义特殊字符
print(r'hello\nrunoob') #在字符串前面添加一个 r，表示原始字符串，不会发生转义

input("\n\n按下enter键后退出。") #执行下面的程序在按回车键后就会等待用户输入：

import sys; x='runoob'; sys.stdout.write(x + '\n')
'''
word ='字符串'
sentence ="这是一个句子。"
paragraph ="""这是一个段落，可以由多行组成"""

x="a"
y="b"
#换行输出
print(x)
print(y)

print('.............')
#不换行输出
print(x,end="")
print(y,end="")
print()