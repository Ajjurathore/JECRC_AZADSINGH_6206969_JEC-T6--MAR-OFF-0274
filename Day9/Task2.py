from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()

# wait  = WebDriverWait(driver, 10)
# actions = ActionChains(driver)
#
# men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Men']")))
# actions.move_to_element(men_menu).perform()
#
# tshirts = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Tshirt']"))).click()
#
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-base")))


wait = WebDriverWait(driver, 15)
actions = ActionChains(driver)

men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Men']")))
actions.move_to_element(men_menu).perform()

tshirts = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='T-Shirts']")))
tshirts.click()

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-base")))

for i in range(4):
    driver.execute_script("window.scrollBy(0, 500);")
    sleep(1)

products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-base")))

target_product = products[12]

driver.execute_script("arguments[0].scrollIntoView();", target_product)

sleep(2)
target_product.click()

sleep(3)
