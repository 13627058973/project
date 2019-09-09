#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql


#  打开数据库连接
db = pymysql.connect('139.9.49.15', 'caichufang', 'Caichufang2017++', 'ccf')

#  使用 cursor() 方法获取操作游标
cursor = db.cursor()

sql = 'select * from ccf_trade where order_code =2019041710043'

#  使用 execute() 方法执行 sql 查询
cursor.execute(sql)

#  使用 fetchone() 方法获取单条数据
data = cursor.fetchone()

print(data)


#  关闭数据库连接
db.close()