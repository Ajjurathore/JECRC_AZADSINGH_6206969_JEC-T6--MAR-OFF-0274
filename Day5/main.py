from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()

opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://www.flipkart.com/")

'''
- send_keys sends data to a particular text field
- clear():- clears the data in a text field 
- get_attribute() in Selenium is used to read the value 
of an HTML attribute from a web element.
- click():- clicks a particular search button
'''


# name = driver.find_element(By.ID, "twotabsearchtextbox")
#
# # name.send_keys("azad")
# # sleep(2)
# # name.clear()
#
# name.send_keys("bmw m5 cs")
#
# sleep(2)
# name.clear()
# search_button = driver.find_element(By.ID, "nav-search-submit-button")
#
# search_button.click()



# driver.get("https://joinindianarmy.nic.in/index.html")
# name = driver.find_elements(By.ID,'ContentPlaceHolder1_KeywordSearch1_txtKeyword')
# name.send_keys("officers")
# sleep(2)
# name.clear()
# search_btn = driver.find_elements(By.ID,'ContentPlaceHolder1_KeywordSearch1_btnSearch')
# search_btn.click()

# driver.find_element(By.ID,"male").click()


driver.maximize_window()
# driver.find_element(By.XPATH, "//label[text()='Monday']").click()

search = driver.find_element(By.XPATH,"//input[@class = 'nw1UBF v1zwn25']")
search.clear()
search.send_keys("bmw")
sleep(2)
driver.find_element(By.XPATH,"//span[text()='✕']").click()
sleep(2)
btn = driver.find_element(By.XPATH,"//button[@type = 'submit']")
btn.click()



