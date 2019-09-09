'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print(driver.title)
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import time
import pyautogui
import multiprocessing
import os
import numpy as np
# -*- coding:utf-8 -*-

def get_driver(url):
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9221")
    chrome_driver='./chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver,options=chrome_options)
    driver.implicitly_wait(5)
    print(22222222)
    return driver

def close_windows(driver):
    windows = driver.window_handles
    for i in range(len(windows)-1):
        driver.switch_to.window(windows[i])
        driver.close()
    windows = driver.window_handles
    driver.switch_to.window(windows[0])

def login(driver):
    try:
        driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
        print('1')
    except:
        pass
    finally:
        driver.find_element_by_xpath('//*[@id="TPL_username_1"]').clear()
        print('1')
        for i in 'zwzlan':
            driver.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys(i)
            time.sleep(random.choice([0.01, 0.02, 0.03, 0.04, 0.05]))
        driver.find_element_by_xpath('//*[@id="TPL_password_1"]').clear()
        for i in 'z123456789i':
            driver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(i)
            time.sleep(random.choice([0.01, 0.02, 0.04, 0.06, 0.08]))
        driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
        time.sleep(0.2)
        print(pyautogui.position())
        pyautogui.moveTo(1233, 492)
        time.sleep(0.2)
        pyautogui.mouseDown()
        pyautogui.moveTo(1496,492,duration=0.2)
        pyautogui.mouseUp()
        driver.find_element_by_xpath('//*[@id="TPL_password_1"]').clear()
        for i in 'z123456789i':
            driver.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(i)
            time.sleep(random.choice([0.01, 0.02, 0.03, 0.04, 0.05]))
        driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
        time.sleep(2)





def cmd():
    b=['C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'% i for i in os.listdir('C:\\Users')
     if os.path.exists('C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'% i)]
    b=b[0]
    b='%s https://login.taobao.com --remote-debugging-port=9221 --user-data-dir=%s\\selenum\\AutomationProfile'%(b,os.getcwd())
    os.system(b)



if __name__ == '__main__':
    mp = multiprocessing.Process(target=cmd)
    mp.start()
    print(1111111111)
    driver = get_driver('https://login.taobao.com')
    close_windows(driver)
    login(driver)
    pass

