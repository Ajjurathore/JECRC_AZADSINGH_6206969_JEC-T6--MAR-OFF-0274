from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

# opts.add_argument('--headless')
# headless will make sure it runs in background without opening the browser or ui

driver = webdriver.Chrome(options = opts)
driver.get("https://testautomationpractice.blogspot.com/")
# sleep(4)
driver.maximize_window()

print("its working")


name = driver.find_element(By.ID,'name')
phone = driver.find_element(By.ID,'phone')
nav_bar = driver.find_element(By.ID,'navbar')
print(name)
print(phone)
print(nav_bar)
print('heheh')


radio = driver.find_elements(By.CLASS_NAME,'form-check-input')
print(radio)
print(len(radio))
# driver.quit()
# locater are used to fund the atrributes so that selenium can interact with it

# CSS SELECTOR -> siplest way to user clasas and is (. -> class and # -> id)
animals = driver.find_element(By.CSS_SELECTOR,'#animals')
print(animals)
# driver.quit()


# * ->  used to take a part of it   =>  a[href *= "testautomationpractice"]
# ^ -> used when to start with  =>  a[href *= "test"]
# $ -> ends with   =>  a[href *= "practice"]

 # <- ------- xPath--------------->
 
