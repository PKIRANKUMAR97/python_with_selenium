import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Demo1():
    def find_el(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get(
            "https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_3lda0bxyzj_e&adgrpid=155259813513&hvpone=&hvptwo=&hvadid=678719109054&hvpos=&hvnetw=g&hvrand=1608668459257532887&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062006&hvtargid=kwd-365295376496&hydadcr=5620_2412619&gad_source=1")
        driver.find_element(By.ID,"twotabsearchtextbox").send_keys('iphone 15')
        time.sleep(5)


d1 = Demo1()
d1.find_el()
