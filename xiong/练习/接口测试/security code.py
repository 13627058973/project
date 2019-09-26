#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver

url = 'https://www.caichufang.com/pc/login.html'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# 定位账号，密码，验证码元素，验证码地址
userElement = driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[1]/input')
passElement = driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[3]/input')
codeElement = driver.find_element_by_xpath('/html/body/div/section/main/div/div/div/div/div[5]/div/input')
imgElement = driver.find_element_by_xpath('//*[@id="app"]/section/main/div/div/div/div/div[5]/img')

# 2,截取屏幕内容，保存到本地
driver.save_screenshot('E:/01.png')
# 获取验证码的坐标
loc = imgElement.location
# 获取验证码的宽高
size = imgElement.size
print("坐标:", loc)
print('宽高:', size)

# 3.获取验证码位置
left = loc['x']
top = loc['y']
bottom = top+size['height']
right = left+size['width']

# 4.打开截图，获取验证码的位置，截取保存验证码
imageCode = Image.open('E:/01.png')
box = (left, top, right, bottom)
imageCode.crop(box).save('E:/02.png')

# 5.获取验证码图片，读取验证码
image = Image.open('E:/02.png')  # 图像增强，二值化
image = image.convert('L')    # 转换模式：L/RGB
image = ImageEnhance.Contrast(image)  # 增强对比度
image = image.enhance(2.0)  # 增强饱和度
image.save('E:/03.png')
image = Image.open('E:/03.png')
# 识别验证码
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)

# 输入账号，密码，验证码
userElement.send_keys('13627058973')
passElement.send_keys('123456')
codeElement.send_keys(code.strip())
time.sleep(5)
driver.quit()






