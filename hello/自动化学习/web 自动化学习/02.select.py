#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

# 下拉框操作

driver = webdriver.Chrome()
driver.get('https://admin.caichufang.com/admin/index.html')
driver.add_cookie({'name': 'SESSION', 'value': 'b572ec13-2fbb-4a0d-9445-32b55925a041'})
driver.get('https://admin.caichufang.com/admin/index.html')
# 进入总后台采购商大模块
admin_purchaser = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/div[4]/div/div/a')
admin_purchaser.click()
time.sleep(2)
# 进入采购商列表
admin_purchaser_list = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[2]/div[4]/div/div/div[2]/ul/li[2]/div/a/div[2]')
admin_purchaser_list.click()
time.sleep(2)
driver.maximize_window()
# 进入镶嵌的页面iframe
iframe = driver.find_element_by_name('inner')
driver.switch_to.frame(iframe)
stats = driver.find_element_by_xpath('//*[@id="searchForm"]/div/div/div[1]/div[5]/div/select')
elst = Select(stats)
elst.select_by_index(0)
time.sleep(2)
elst.select_by_index(1)
time.sleep(2)
elst.select_by_index(2)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="searchForm"]/div/div/div[2]/button').click()
'''
#点击编辑，进入采购商资料详情页面
edit = driver.find_element_by_xpath('//*[@id="purchaserList"]/table/tbody/tr[1]/td[10]/a[1]')
edit.click()
time.sleep(2)
#点击企业类型
company_type = driver.find_element_by_id('select2-enterprise-Type-container')
company_type.click()
for i in range(10):
    js = 'window.scrollTo(0,%s)'%(i*100)
    driver.execute_script(js)
    time.sleep(3)
purchaser = driver.find_element_by_xpath('//*[@id="dataForm"]/div/div[20]/div/button')
purchaser.click()
time.sleep(1)
'''

time.sleep(3)
driver.quit()
