import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FindingAllElements(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_AllElements(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://demo.automationtesting.in/")
        print(driver.title)
        # element = driver.find_element(By.ID, "btn2")
        element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]/button[1]")
        element.click()
        First_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        First_name.send_keys("KIRAN")
        Last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        Last_name.send_keys("KUMAR")
        Address = driver.find_element(By.XPATH,
                                      "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/textarea[1]")
        Address.send_keys("BANGALORE")
        Email = driver.find_element(By.XPATH, "//input[@type='email']")
        Email.send_keys("kiran@email.com")
        Phone = driver.find_element(By.XPATH, "//input[@type='tel']")
        Phone.send_keys("1234567890")
        Gender = driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
        Gender.click()
        Hobbies = driver.find_element(By.ID, "checkbox1")
        Hobbies.click()
        WebTable = driver.find_element(By.LINK_TEXT, "WebTable")
        WebTable.click()
        Practice_site = driver.find_element(By.PARTIAL_LINK_TEXT, "Practice Si")
        Practice_site.click()

        time.sleep(5)

    def tearDown(self) -> None:
        print(self.driver.title)
        self.driver.close()
