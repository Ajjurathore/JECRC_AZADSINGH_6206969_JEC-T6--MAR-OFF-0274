from selenium import webdriver
from selenium.webdriver.common.by import By
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.lenskart.com/")


# sun = driver.find_element(By.XPATH,"//a[@id = 'lrd5']")

#assert is used to check whereter it is present in the tag or not

#1 assert 'SUNGLASSES' in sun.text
#2
# assert 'GLASSES' == sun.text,"din't get"
# print("got it")
# driver.quit()

