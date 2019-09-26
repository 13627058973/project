#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd

data = xlrd.open_workbook('../单元测试/晋实惠旗舰店.xls')
tables = data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(2, 3))
