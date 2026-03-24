from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com")
driver.maximize_window()
sleep(4)

#to the bottom scroll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)

#scroll to the top
driver.execute_script("window.scrollTo(0,0)")
sleep(3)

#using scroll by
driver.execute_script("window.scrollTo(0,500)")
sleep(3)

driver.execute_script("window.scrollTo(0,-200)")
sleep(3)

