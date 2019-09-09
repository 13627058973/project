#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import xlwt
#
# workbook = xlwt.Workbook(encoding='utf-8')  # 新建空白表格
# sheet = workbook.add_sheet('jmeter')
# for i in range(6000):
#     user = "jmeter%s"%i
#     print(user)
#     sheet.write(i, 0, user)
# workbook.save('E:/jmeter.xls')
l1 = [183,0,1,2,-184,367]

num = []

for i in range (0,len(l1)):

    for l in range (i+1,len(l1)):

        if l1[i]+l1[l]==183:
            num.append((l1[i],l1[l]))
            sum = set(num)

print(sum)