from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

country = driver.find_element(By.ID,"country")
dropdown = Select(country)

dropdown.select_by_value("india")
sleep(12)
dropdown.select_by_index(4)
sleep(12)
dropdown.select_by_text("India")
sleep(12)
driver.quit()