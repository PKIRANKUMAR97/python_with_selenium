import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Navigation_keys_1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_navigation_keys_1(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.emirates.com/nz/english/")
        assert "Emirates" in driver.title
        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "(//button[@name='clear Departure airport'])[1]").click()
        time.sleep(5)
        print(driver.title)

    def tearDown(self):
        self.driver.close()
