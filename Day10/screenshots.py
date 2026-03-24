import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

folder = os.path.join(os.getcwd(), "screenshots")
os.makedirs(folder, exist_ok=True)
driver = webdriver.Chrome()
actions = ActionChains(driver)



driver.get("https://in.pinterest.com")
driver.maximize_window()
sleep(3)

x_path = driver.find_element(By.XPATH,"(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
sleep(3)
actions.scroll_to_element(x_path).perform()
sleep(3)

driver.save_screenshot(f'{folder}/screenshot.png')
sleep(3)
