#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# 创建一个浏览器
driver = webdriver.Chrome()
# 获取浏览器的尺寸
print(driver.get_window_size())
# 设置浏览器的大小
# driver.set_window_size(width=100, height=100)
print(driver.get_window_size())
url = 'http://baidu.com'
driver.get(url)
# 刷新页面
driver.refresh()
driver.get('https://www.caichufang.com/index.html')
# 添加token 跳过登录
driver.add_cookie({'name':'SESSION', 'value':'6f76285f-129a-47ca-8c52-817cd5bdfd37'})
driver.get('https://www.caichufang.com/index.html')
time.sleep(3)
# 回退到之前的页面
driver.back()
# 前进到之后的页面
driver.forward()

# 最大化页面
driver.maximize_window()
print(dir(driver))
time.sleep(3)
# 获取当前访问页面的url
print(driver.current_url)
# 获取当前浏览器标题
print(driver.title)
# 保存图片
# print(driver.get_screenshot_as_png())
# 直接保存，并新建一个文件保存
# driver.get_screenshot_as_file('bb.png')
# 获取分类元组
# ccf_list = driver.find_elements_by_class_name('button-text-333')
# for i in ccf_list:
#     ActionChains(driver).move_to_element(i).perform()
#     time.sleep(3)
ccf_su = driver.find_element_by_css_selector('div.bg-white:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
ccf_su.send_keys('胶囊')
ccf_su.send_keys(Keys.ENTER)




time.sleep(3)

driver.close()