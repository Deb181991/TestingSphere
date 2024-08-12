from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


options1 = Options()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         "download.default_directory": "F:\SphereWMS\CevaVision - Copy\CevaVision\Download"}
options1.add_experimental_option("excludeSwitches", ["enable-automation"])
options1.add_experimental_option("prefs", prefs)
options1.add_experimental_option("detach", True)
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path='D:\Bestinet\Driver\chromedriver.exe', options=options1)
driver.maximize_window()

driver.get("https://sandbox.v2.nonprod.spherewms.com/")
# to identify element
UserID = driver.find_element_by_xpath("//*[@id='username']")
UserID.send_keys("umar.anwar@spherewms.com")
# # import pandas as pd

# # filepath = r".\Download\House_Bills_List_For_Customers_20240307_151517.xlsx"
# # sheetName = "House Bills"

# # # Read the Excel file into a DataFrame
# # df = pd.read_excel(filepath, sheet_name=sheetName)
# # # Total Count of Customers
# # totalCount = df['CUSTOMER'].count()
# # print(f"Total Count: {totalCount}")
# # # Separate Counts for Each Customer
# # separateCounts = df['CUSTOMER'].value_counts()
# # print("Separate Counts:")
# # print(separateCounts)
# # # Assuming you have columns like 'CUSTOMER' and 'MILESTONE'
# # distinct_milestone_count = df.groupby(['CUSTOMER', 'MILESTONE']).size().reset_index(name='COUNT')
# # # Display distinct milestone count for each customer
# # for index, row in distinct_milestone_count.iterrows():
# #     customer = row['CUSTOMER']
# #     milestone = row['MILESTONE']
# #     milestone_count = row['COUNT']
# #     print(f"Customer: {customer}, Milestone: {milestone}, Milestone Count: {milestone_count}")

# import os
# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# options1 = Options()
# prefs = {"credentials_enable_service": False,
#          "profile.password_manager_enabled": False,
#          "download.default_directory": "F:\SphereWMS\CevaVision - Copy\CevaVision\Download"}
# options1.add_experimental_option("excludeSwitches", ["enable-automation"])
# options1.add_experimental_option("prefs", prefs)
# options1.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path='./chromedriver', options=options1)

# driver.get('https://develop.cevavision.nonprod.spherewms.com/login')
# driver.maximize_window()
# time.sleep(5)
# UI = driver.find_element(By.XPATH, "//input[@type='email']")
# UI.send_keys("admin@spherewms.com")
# PW = driver.find_element(By.XPATH, "//input[@type='password']")
# PW.send_keys("!@#$ceva-vision!@#$")
# Login = driver.find_element(By.XPATH, "//button[@type='submit']")
# Login.click()
# time.sleep(5)
# ECOLAB = driver.find_element(By.XPATH, "//*[text()='ECOLAB']")
# ECOLAB.click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(15)
# Downlaoad = driver.find_element(By.XPATH, "//*[@class='btn btnDownlaoad']")
# Downlaoad.click()
# time.sleep(10)
# download_folder = "F:\SphereWMS\CevaVision - Copy\CevaVision\Download"
# latest_file = max([os.path.join(download_folder, f) for f in os.listdir(download_folder)], key=os.path.getctime)
# filename = os.path.basename(latest_file)
# v = f'{download_folder}\{filename}'
# print(v)




# from datetime import datetime, timedelta

# def next_monday():
#     today = datetime.today()
#     days_ahead = 0 - today.weekday() + 7  # Calculate the number of days until the next Monday
#     next_monday_date = today + timedelta(days=days_ahead)
#     return next_monday_date

# print(next_monday().strftime('%Y-%m-%d'))  # Print the date of the next Monday in YYYY-MM-DD format


# from datetime import datetime, timedelta

# today = datetime.today()
# # days_ahead = 0 - today.weekday() + 7  # Calculate the number of days until the next Monday
# # next_monday_date = today + timedelta(days=days_ahead)
# print(today.day)  # Extract just the date part
# # current_date = datetime.now()
# next_day = today + timedelta(days=1)
# print(next_day.day)


import time
from selenium import webdriver

driver = webdriver.Chrome()  # Initialize a browser driver (you need to install the appropriate driver for your browser)

driver.get("https://example.com")  # Open a webpage
time.sleep(10)
try:
    # Try to find and close the pop-up
    pop_up = driver.find_element_by_id("pop-up-id")  # Replace "pop-up-id" with the actual ID of the pop-up element
    pop_up.find_element_by_id("close-button").click()  # Replace "close-button" with the ID or class of the close button
except:
    # If the pop-up doesn't appear, do something else
    print("No pop-up found.")

# Continue with the rest of your script
