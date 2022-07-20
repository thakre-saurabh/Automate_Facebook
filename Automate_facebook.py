# Automate_Facebook
This script will login automatically using synthetic automation

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import getpass
email =input("Enter user id")
passw =getpass.getpass("Enter password")
driver = webdriver.Chrome(ChromeDriverManager().install()) #execute first time to know chromedriver path
driver=webdriver.Chrome(r"C:\Users\Administrator\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver.exe")
driver.get("https:\\www.google.com")
time.sleep(2)
driver.find_element_by_id('input').send_keys(gmail)
time.sleep(2)
driver.find_element_by_id("rso").click()
time.sleep(5)
driver.find_element_by_id("password").send_keys(passw)
time.sleep(2)
driver.find_element_by_name("login").click()





