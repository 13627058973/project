#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
python3六个标准的数据类型：
number(数字)
string(字符串)  Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
             如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
list(列表)   列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
tuple(元组)  元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
set(集合)    可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
dictionary(字典)
不可变数据：number，string，tuple
可变数据：list，dictionary，set

#判断数据类型：
a = -1
isinstance(a, int)
#列表数据截取：
list =['abcd',20,3,'runoob',70.2]
print(list[1:4:2])
list[2] ='python'
list[3] =18
print(list)
if 17 in list:
    print('17在列表中')
else:
    print('17不在列表中')
#set(集合)
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student) #输出集合，重复的元素被自动去掉

#dictionary(字典)
dict = {}
dict['one'] = "菜鸟教程"
dict[2] = "菜鸟工具"
tinydict ={'name':'runoob','code':1, 'site':'www.runoob.com'}
print(dict['one'])       #输出键为‘one’的值
print(dict[2])           #输出键为2的值
print(tinydict)          #输出完整的字典
print(tinydict.keys())   #输出所有键
print(tinydict.values()) #输出所有值
'''
a={x:x**2 for x in (2,4,6)}
print(a)
b=dict(Runoob=1, Google=2, Taobao=3)  #构造字典
print(b)