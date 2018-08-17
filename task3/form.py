# -*- coding: utf-8 -*-
from selenium import webdriver
import time
url='http://www.deng18.cn/form/index'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#bootstrap日期选择插件
china=driver.find_element_by_xpath('//*[@id="form-datepicker"]/div[6]/div/div/input')
china.send_keys('2017/08/17')
time.sleep(1)
japan=driver.find_element_by_xpath('//*[@id="form-datepicker"]/div[7]/div/div/div/input')
japan.click()
japan.send_keys('2018/05/07')
time.sleep(1)
fanwei1=driver.find_element_by_xpath('//*[@id="form-datepicker"]/div[8]/div/div/div/input[1]')
fanwei1.click()
fanwei1.clear()
fanwei1.send_keys('2017/08/17')
time.sleep(1)
fanwei2=driver.find_element_by_xpath('//*[@id="form-datepicker"]/div[8]/div/div/div/input[2]')
fanwei2.click()
fanwei2.clear()
fanwei2.send_keys('2018/05/07')
time.sleep(1)

#bootstrap日期及时间范围选择插件
chajian=driver.find_element_by_id('tbTime')
chajian.click()
chajian.clear()
chajian.send_keys('2016/04/19 12:00:00 - 2017/04/20 11:00:00')
chajian.find_element_by_xpath('/html/body/div[6]/div[3]/div/button[1]').click()

#bootstrap日期时间选择插件
effect1=driver.find_element_by_xpath('//*[@id="datetimepicker1"]/input')
effect1.click()
effect1.clear()
effect1.send_keys('08/15/2018 11:00')
time.sleep(1)
effect2=driver.find_element_by_xpath('//*[@id="datetimepicker3"]/input')
effect2.click()
effect2.clear()
effect2.send_keys('1:00 PM')
time.sleep(1)

#bootstrap选色插件
color=driver.find_element_by_xpath('//*[@id="cp2"]/input')
color.clear()
color.send_keys('#33d4c0')
time.sleep(1)

#Bootstrap Form Helper 插件集合
js="document.querySelector('#form-formhelper > div:nth-child(8) > div > div > div > div:nth-child(1) > div > div.input-group.bfh-timepicker-toggle > input').removeAttribute('readonly')"
driver.execute_script(js)
helper=driver.find_element_by_xpath('//*[@id="form-formhelper"]/div[6]/div/div/div/div[1]/div/div[1]/input')
helper.clear()
helper.send_keys('10:15')
helper2=driver.find_element_by_xpath('//*[@id="form-formhelper"]/div[6]/div/div/div/div[2]/form/div/input')
helper2.clear()
helper2.send_keys('2')
driver.find_element_by_xpath('//*[@id="form-formhelper"]/div[6]/div/div/div/div[2]/form/div/span[1]').click()
time.sleep(1)
driver.quit()