## Task 1
### Create a Selenium script in Python to demonstrate browser control commands such as opening a website, maximizing the window, navigating backward and forward, refreshing the page, minimizing the window, and quitting the browser using ChromeDriver.

from selenium import webdriver
from time import sleep

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
driver = webdriver.Chrome()#options=opts)
driver = webdriver.Chrome()

driver.get("https://www.google.com")
#
# driver.maximize_window()
# sleep(3)
# driver.minimize_window()
# sleep(3)
sleep(3)

driver.close()
driver.quit()
driver.forward()
driver.back()
driver.refresh()
