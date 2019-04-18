#__author__ = 'chubby_superman'
#_*_coding=utf-8 _*_


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True  #设置无头浏览器
driver = webdriver.Firefox(executable_path="geckodriver",options=options)
url = "http://www.baidu.com"
q=u"共a1产党的"
class test_baidu_click_func():
    def search_click(self):
        driver.get(url)
        kw = driver.find_element_by_xpath('//*[@id="kw"]')
        kw.clear()
        kw.send_keys("%s"%q)
        su = driver.find_element_by_xpath('//*[@id="su"]')
        su.click()
        return driver.current_url

    def results_click(self):
        driver.get(self.search_click())
        res=driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[3]/div[2]/h3/a")
        res.click()
        return driver.current_url
if __name__=="__main__":
    print(test_baidu_click_func().results_click())


