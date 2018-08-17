# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
import time,os

driver=webdriver.Chrome()
url='http://www.deng18.cn'
driver.get(url)
time.sleep(2)

c=driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/ul[1]/li[1]')
ActionChains(driver).move_to_element(c).perform()
time.sleep(2)

#按钮
driver.find_element_by_class_name("btn-primary").click()
time.sleep(1)


#下拉列表
s1 = Select(driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul[1]/li[3]/select"))
s1.select_by_value("2")
time.sleep(1)

#Dropdown
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul[1]/li[4]/div/button").click()
time.sleep(1)
driver.find_element_by_class_name('dropdown-item').find_element_by_xpath('/html/body/div[3]/div[2]/div/ul[1]/li[4]/div/div/a[2]').click()
time.sleep(1)

#单选框
driver.find_element_by_xpath("//input[@id='inlineRadio1']").click()
time.sleep(1)
#复选框
driver.find_element_by_xpath("//input[@id='inlineCheckbox1']").click()
driver.find_element_by_xpath("//input[@id='inlineCheckbox2']").click()
time.sleep(1)
#输入框
driver.find_element_by_class_name("mr-sm-2").send_keys("hello")
driver.find_element_by_class_name("my-sm-0").click()
time.sleep(1)

#浮层弹窗
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/ul[1]/li[8]/button').click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='exampleModal']/div/div/div[3]/button[1]").click()
time.sleep(1)


#新页面打开链接
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul[1]/li[9]/p[1]/a").click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
#当前页面打开链接
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/ul[1]/li[9]/p[2]/a").click()
time.sleep(1)
driver.back()
time.sleep(1)

driver.find_element_by_xpath("//input[@value='显示警告框']").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element_by_xpath("//input[@value='显示确认框']").click()
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.find_element_by_xpath("//input[@value='显示提示框']").click()
time.sleep(1)
s=driver.switch_to.alert
print(s.text)
time.sleep(1)
s.send_keys('123456')
time.sleep(1)
s.accept()

#上传文件---AutoIt---调用control.exe上传程序
driver.find_element_by_id('inputGroupFile02').click()
os.system('C:/Users/i-jiangyihan/Desktop/control.exe')
time.sleep(2)

#下载
driver.find_element_by_css_selector('body > div.container-fluid.all > div.maincontent.row > div > ul:nth-child(2) > li:nth-child(12) > a').click()
time.sleep(5)

driver.switch_to.frame('frame1')
driver.find_element_by_id('input').send_keys('123')
driver.find_element_by_id('search-button').click()
driver.quit()



