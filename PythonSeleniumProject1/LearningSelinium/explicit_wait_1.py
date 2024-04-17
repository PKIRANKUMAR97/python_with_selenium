import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.find_element(By.XPATH,"//span[normalize-space()='Flights']").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//button[@aria-label='Leaving from']").click()
driver.find_element(By.XPATH,"//input[@id='origin_select']").send_keys("SFO")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@aria-label='Going to']").click()
driver.find_element(By.XPATH,"//input[@id='destination_select']").send_keys("NYC")
time.sleep(5)
# driver.find_element(By.XPATH,"//button[normalize-space()='May 2 - May 9']")
driver.find_element(By.XPATH,"//button[@id='search_button']").click()





