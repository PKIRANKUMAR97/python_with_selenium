from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.guru99.com/test/newtours/")  # this url takes time to load
driver.maximize_window()
driver.implicitly_wait(10)  # wait for 10 seconds
assert "Welcome: Mercury Tours" in driver.title
driver.find_element(By.NAME, "userName").send_keys("mercury")
driver.find_element(By.NAME,"password").send_keys("travels")
driver.find_element(By.NAME,"submit").click()
driver.close()


