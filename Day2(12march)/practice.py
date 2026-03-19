from selenium import webdriver
from time import sleep
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
# sleep(3)
driver.get("https://www.google.com")

driver.maximize_window()
driver.minimize_window()
