#!/usr/bin/env python 
# -*- coding:utf-8 -*-

def test():
    import json
    info = [{'a':'1','b':'2','c':'3','d':'4','f':'5'}]
    data = json.dumps(info, sort_keys=True, indent=4, separators=(',', ': '))
    print(data)


test()

def test1():
    import json
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
    text = json.loads(jsonData)
    print(jsonData)
    print(text)

test1()

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)