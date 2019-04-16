#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True  #设置无头浏览器
driver = webdriver.Firefox(executable_path="geckodriver",options=options)
url = "http://www.baidu.com"
q=u"共a1产党的"
driver.get(url)
kw = driver.find_element_by_xpath('//*[@id="kw"]')
kw.clear()
kw.send_keys("%s"%q)
su = driver.find_element_by_xpath('//*[@id="su"]')
su.click()
driver.close()
