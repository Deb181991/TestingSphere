import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



options1 = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         "download.default_directory": "F:\SphereWMS\CevaVision - Copy\CevaVision\Download"}
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("prefs", prefs)
options1.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path='D:\Bestinet\Driver\chromedriver.exe', options=options1)
driver.maximize_window()

driver.get("https://sandbox.v2.nonprod.spherewms.com/")
# to identify element
time.sleep(2)
UserID = driver.find_element(By.XPATH, "//*[@id='username']")
UserID.send_keys("umar.anwar@spherewms.com")
Password = driver.find_element(By.XPATH, "//*[@name='password']")
Password.send_keys("Silentassasin123")
Submit = driver.find_element(By.XPATH, "//*[@type='submit']")
Submit.click()
# time.sleep(2)
# Dashboard = driver.find_element(By.XPATH, "//*[@title='Dashboard']")
# Dashboard.click()
# Target = driver.find_element(By.XPATH, "//*[text()='Target Portal']")
# Target.click()
# time.sleep(2)
# driver.switch_to.window(driver.window_handles[1])
# # time.sleep(20)
# WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Close']")))
# time.sleep(2)
# # element.click()
 
# Close = driver.find_element(By.XPATH, "//*[text()='Close']")
# Close.click()
# time.sleep(2)
# TruckInfo = driver.find_element(By.XPATH, "//div[@class='boxImage col-12']//img[1]")
# TruckInfo.click()
# time.sleep(8)
# TruckSchedule = driver.find_element(By.XPATH, "//*[text()=' Truck Schedule ']")
# TruckSchedule.click()