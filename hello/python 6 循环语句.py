#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
# while循环  计算1到100的总和
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

#无限循环
var=1
while var ==1:  #表达式永远为true
    num=int(input("你最帅:"))
    print("你输入的数字是:",num)

print("good bye!")

# 一直打印 按Ctrl+C中断循环
flag =1
while (flag):print("菜鸟教程")
print()

# for循环 遍历列表数据
lang=['c','b','a','p']
for x in lang:
    print(x)

# break 语句，break 语句用于跳出当前循环体
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据")
print("完成循环!")
#遍历数字序列 使用内置函数range()函数  会生成数列
for i in range(5):
    print(i)
for i in range(5,9):
    print(i)
for i in range(0,10,2):
    print(i)

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
for lettle in "inset":  #第一个实例
    if lettle == "t":
        break
    print("当前字母为:",lettle)

var =10
while var > 0:  #第二个实例
    print("当期的变量为:",var)
    var =var -1
    if var ==5:
        break
print("good bye.")
'''
# continue语句被用来告诉python跳过当前循环中的剩余语句 然后进行下一轮循环
for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")