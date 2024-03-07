import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''
class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('kiiii')
        time.sleep(4)
findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()

'''


class DemoFindElementByName():
    def locate_by_name_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_name('login-input').send_keys('qwerty.com')
        time.sleep(4)


findbyname = DemoFindElementByName()
findbyname.locate_by_name_demo()
