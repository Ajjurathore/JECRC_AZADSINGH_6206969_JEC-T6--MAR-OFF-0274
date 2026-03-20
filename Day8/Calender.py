from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "datepicker").click()

target_day = "20"
target_month = "March"
target_year = "2026"

while True:
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if month == target_month and year == target_year:
        break
    else:
        driver.find_element(By.XPATH, "//a[@title='Next']").click()

driver.find_element(By.XPATH, f"//a[text()='{target_day}']").click()