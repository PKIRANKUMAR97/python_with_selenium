import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByXpath():
    def locate_by_xpath_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_element(By.XPATH,"//input[@id='login-input']").send_keys('asdfg.com')
        time.sleep(5)


findbyxpath = DemoFindElementByXpath()
findbyxpath.locate_by_xpath_demo()
