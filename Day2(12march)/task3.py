## Task 3
### Create a Selenium script that opens a website in multiple browsers, prints the page title, current URL, and browser name for each, and then closes each browser.
from selenium import webdriver
from time import sleep

l = [webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for i in l:
    driver = i
    driver.get("https://google.com")
    print(driver.current_url)
    print(driver.title)
