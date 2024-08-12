

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options1 = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         "download.default_directory": "F:/SphereWMS/CevaVision - Copy/CevaVision/Download"}  # Use forward slashes in the path
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("prefs", prefs)
options1.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path='./chromedriver', options=options1)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
time.sleep(5)
UI = driver.find_element(By.XPATH, "//*[@class='_3sdu8W emupdz']")
# Get the value of a specific attribute, for example, 'innerText' or 'textContent'
attribute_value = UI.get_attribute('innerText')
attribute_value1 = UI.get_attribute('textContent')
print(attribute_value)
print(attribute_value1)



# String projectPath = System.getProperty("user.dir");
# String driverPath = projectPath + "/drivers/chromedriver.exe";





