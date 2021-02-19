# coding:utf8
import time

import xlrd
"""
from phone import Phone

p = Phone()
c = '15854648273'  # 手机号
city = p.find(c)
print(city)  # 所有信息
print('手机号：' + c)
print('所属省份：' + city['province'])
print('所属市区：' + city['city'])
print('邮    编：' + city['zip_code'])
print('电话区号：' + city['area_code'])
print('运 营 商：' + city['phone_type'])
"""

from selenium import webdriver

import pyautogui

driver = webdriver.Chrome()
driver.get("http://yxtcd.f3322.net:10080/admin")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="username"]').send_keys("1001")
driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/input[2]').send_keys("qazwsx123")
driver.find_element_by_xpath('//*[@id="validateCode"]').send_keys("1234")
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

pyautogui.moveTo(1177, 629, duration=1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(532, -262, duration=1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(594, 540, duration=1)
pyautogui.click()