from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# name = driver.find_element(By.CLASS_NAME,'_navbar_5r70f_1')
# span = driver.find_element(By.CLASS_NAME,'_link_5r70f_27')
# num1 = driver.find_element(By.CLASS_NAME,'_soonCardQuiz_1kqx3_237')
# radio = driver.find_element(By.CLASS_NAME,'_soonCardQuiz_1kqx3_237')
# dash = driver.find_element(By.CLASS_NAME,'_link_5r70f_27')
# print(dash)
# print(num1)
# print(span)
# print(name)
# print(radio)

# driver.maximize_window()
# ques1 = driver.find_element(By.ID,'modal-root')
# ques2 = driver.find_element(By.ID,'DndDescribedBy-1')
# ques3 = driver.find_element(By.ID,'DndLiveRegion-1')
# tag = driver.find_element(By.ID,'monica-content-root')
# Qname = driver.find_element(By.ID,'give-freely-root-ejkiikneibegknkgimmihdpcbcedgmpo')
# print(Qname)
# print(tag)
# print(ques1)
# print(ques2)
# print(ques3)

# a[href*="testautomationpractice"]


xpath_res = driver.find_element(By.XPATH,"//div[@class='result']")
print(xpath_res)
xPath_clear = driver.find_element(By.XPATH,"//div[@class='blog-feeds']")
print(xPath_clear)
xpath_reslt = driver.find_element(By.XPATH,"//div[@class='post hentry uncustomized-post-template']")
print(xpath_reslt)
xPath_yum = driver.find_element(By.XPATH,"//div[@class='widget Blog']")
print(xPath_yum)


# xpath_phone=driver.find_elements(By.XPATH,"//input[@id='phone']")
# print(xpath_phone)
#
# xpath_form=driver.find_elements(By.XPATH,"//div[@class='form-group'][1]")
# print(xpath_form)
#
# xpath_datepicker=driver.find_element(By.XPATH,"//input[@id='datepicker']")
# print(xpath_datepicker)
#
# xpath_postHeader=driver.find_element(By.XPATH,"//div[@class='post-header']")
# print(xpath_postHeader)
#
# xpath_textbox=driver.find_element(By.XPATH,"//label[@for='textbox']")
# print(xpath_textbox)


