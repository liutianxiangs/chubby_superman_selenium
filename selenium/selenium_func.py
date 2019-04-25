#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True  #设置无头浏览器
driver = webdriver.Firefox(executable_path="geckodriver",options=options)

q=u"共a1产党的"
class Baidu_selenium_func():
    def __init__(self,driver,sendkeys_v):
        self.sendkeys_v=sendkeys_v
        self.driver=driver
    def search_click(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        kw = self.driver.find_element_by_xpath('//*[@id="kw"]')
        kw.clear()
        kw.send_keys("%s"%self.sendkeys_v)
        su = self.driver.find_element_by_xpath('//*[@id="su"]')
        su.click()
        return self.driver.current_url
    def results_click(self):
        self.driver.get(self.search_click())
        res=self.driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[3]/div[1]/h3/a")
        res.click()
        return self.driver.current_url
if __name__=="__main__":
    print(Baidu_selenium_func(driver,q).results_click())

