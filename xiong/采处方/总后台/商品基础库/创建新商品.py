#!/usr/bin/env python
# -*- coding:utf-8 -*-
from lib2to3.pgen2 import driver

from selenium import webdriver
from Commonlib.commonlib import Commonshare
# 导入下拉框select
from selenium.webdriver.support.select import Select
# 导入键盘操作
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# 创建基础商品

class Create_goods(Commonshare):
    def create(self):
        self.driver.implicitly_wait(3)
        # 打开采处方
        self.login('dd20fefc-ce6f-410f-8c38-8262bce7fc6d')
        # 进入商品基础库页面
        self.click('xpath', '/html/body/div/div[2]/div[2]/div[1]/div/div/div[2]/ul/li[1]/div/a/div[2]')
        iframe = self.driver.find_element_by_name('inner')
        self.driver.switch_to_frame(iframe)
        # 点击创建新商品
        self.click('text', '创建新商品')
        time.sleep(3)
        # 填写商品分类
        c = random.randint(1, 14)
        class_good = self.locateElement('id', 'product_classify')
        Select(class_good).select_by_index(c)
        class_good.click()
        class_two_good = self.locateElement('id', 'classTow')
        d = random.randint(1, 3)
        Select(class_two_good).select_by_index(d)
        class_two_good.click()
        self.input_data('id', 'product_name', '脑络通')
        self.input_data('id', 'generic_name', '胶囊')
        self.click('id', 'select2-myManufacturer-container')
        self.input_data('class', 'select2-search__field', '北京')
        self.driver.find_element(By.ID, "product_Specifications").click()
        # self.driver.execute_script("arguments[0].click();", manufacturers)
        # self.webdriver.ActionChains(driver).move_to_element(manufacturers).click(manufacturers).perform()
        # manufacturers.send_keys(Keys.ENTER)
        self.input_data('id', 'product_Specifications', '1g*1粒')
        self.input_data('id', 'approval_number', '国药准字X42323jj')
        unit = self.locateElement('id', 'product_Company')
        Select(unit).select_by_value('盒')
        unit.click()
        Checkbox = self.driver.find_elements_by_id('scopesCheckbox')
        for i in Checkbox:
            i.click()
        self.click('name', 'button')


if __name__ == '__main__':
    a = Create_goods()
    a.create()
