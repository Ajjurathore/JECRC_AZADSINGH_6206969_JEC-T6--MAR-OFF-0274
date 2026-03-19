## Task 2
### Create a Selenium automation script that demonstrates cross-browser testing by opening the same website in Chrome, Edge, and Firefox one after another, pausing for a few seconds in each browser, and then closing it.

from selenium import webdriver
from time import sleep

l = [webdriver.Chrome(),webdriver.Firefox(),webdriver.Edge()]
for i in l:
    driver = i
    driver.get("https://google.com")
    sleep(2)