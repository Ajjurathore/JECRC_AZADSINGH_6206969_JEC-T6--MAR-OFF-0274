from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/eyeglasses/brands/vincent-chase-eyeglasses/cat-eye.html?dir=desc&gan_data=true&sort=created")
driver.maximize_window()

search = driver.find_element(By.XPATH,"//input[@class = 'aa-Input']")
search.clear()
search.send_keys("osm glass", Keys.ENTER)
sleep(4)


filter = driver.find_element(By.ID,"sortByDropdown")
dropdown = Select(filter)
dropdown.select_by_value("created")
sleep(1)
# dropdown.select_by_index(1)
# sleep(5)
# dropdown.select_by_text("Low to High")
# sleep(5)
select  = driver.find_element(By.XPATH,"//div[@class='sc-bf32d8a7-0 gOVKHN']/descendant::div[1]")
select.click()
sleep(4)


driver.quit()