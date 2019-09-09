#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# 返回函数的执行结果


def test1(a, b):
    print('测试')
    return a + b


res = test1(1, 2)
print(res)


# 结束函数的执行
def test2(a):
    print("xionghongbin")
    if a > 10:
        return
    # return下面的函数不会运行了
    print("**********")


test2(100)


def login(username, password):
    if username == 'python' and password == "test":
        result = '{"code":1,"msg":"登录成功"}'
    return result


s = login("python", "test")
print(s)


def fot(string):
    List = []
    for i in string:
        List.append(i)
    print(List)


fot("python")


class Myclass:
    i = 12345

    def f(self):
        return "hello word"


X = Myclass()
print("Myclass类的属性i为：", X.i)
print("Myclass类的方法f输出为：", X.f())


class init:
    name = 'math'
    age = 0
    _weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self._weight = w
        if a > 1:
            print("确实大于")
        elif w < 2:
            print("我不喜欢这种感觉")
        else:
            print("哈哈")

    def speck(self):
        print("%s说：我%d岁。" % (self.name, self.age))


p = init('root', 18, 3)
p.speck()
