## Task 1

### CSS Locators

Write a Selenium script for the following:

1. Go to `https://the-internet.herokuapp.com/login`
2. Locate the username field using CSS Selector with tag and `name` attribute.
3. Locate the password field using CSS Selector with tag and `id` attribute.
4. Locate the **Login** button using CSS Selector with tag and `type` attribute.
5. Locate the footer link **Elemental Selenium** using CSS Selector with descendant selector.

---
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
sleep(2)

print("Website opened")

username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
print("Username field located")

password = driver.find_element(By.CSS_SELECTOR,"input#password")
print("Password field located")

login_btn = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
print("Login button located")

footer = driver.find_element(By.CSS_SELECTOR,"#page-footer a")
print("Footer link located")
print(footer.text)

sleep(3)
driver.quit()
