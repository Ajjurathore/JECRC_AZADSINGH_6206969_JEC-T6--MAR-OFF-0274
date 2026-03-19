from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")

# xPath =driver.find_element(By.XPATH,"//span[text() = 'All']/ancestor::div[@id = 'nav-main']")
# print(xPath)
# xPath2 = driver.find_element(By.XPATH,"//div[@id = 'nav-main']/descendant::span[text() = 'All']")
# print(xPath2)
# xPath3 = driver.find_element(By.XPATH,"//div[@class = 'nav-left']/descendant::span[@id = 'nav-search-label-id']")
# print(xPath3)
# xpath4 = driver.find_element(By.XPATH,"//div[@class= 'nav-div']/ancestor::div[@class ='nav-fill']")
# print(xpath4)


# driver.find_element(By.LINK_TEXT,"Udemy Courses")
# print("i found it")
# driver.find_element(By.PARTIAL_LINK_TEXT,"udemy")
# print("i found it using partial link")

# price = driver.find_element(By.XPATH,"//td[text() = 'Learn Java']/following-sibling::td[3]")
# print(price)
#
# tabel1 = driver.find_element(By.XPATH,"//td[text() = 'Amod']/ancestor::table[@name='BookTable']/descendant::td[3]")
# print(tabel1)

list = driver.find_elements(By.XPATH,"//td[text()='300']/preceding-sibling::td[3]")
for i in list:
    print(i.text)
driver.quit()


list2 = driver.find_elements(By.XPATH,"//tbody[@id = 'rows']/descendant::tr/descendant::td[1]")
for i in list2:
    print(list2.text)
