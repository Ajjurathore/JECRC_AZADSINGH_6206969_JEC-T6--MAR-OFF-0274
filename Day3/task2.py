from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

xpath1 = driver.find_element(By.XPATH,"//input[@id='name']")
xpath2 = driver.find_element(By.XPATH,"//input[@id='email']")
xpath3 = driver.find_element(By.XPATH,"//input[@id='phone']")
xpath4 = driver.find_element(By.XPATH,"//textarea[@id='textarea']")
xpath5 = driver.find_element(By.XPATH,"//button[text()='Submit']")

print("5 elements found using XPath")

xpath6 = driver.find_element(By.XPATH,"//h2[text()='Mouse Hover']")
xpath7 = driver.find_element(By.XPATH,"//button[text()='Point Me']")
xpath8 = driver.find_element(By.XPATH,"//option[contains(text(),'Lion')]")
print("8 elements found using XPath")