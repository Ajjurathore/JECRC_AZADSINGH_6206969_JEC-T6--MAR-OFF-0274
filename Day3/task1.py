## Task 1
Write a Python Selenium script that opens a single website and demonstrates the use of different Selenium locators to identify web elements. The script should use ID, Name, Class Name, Tag Name, CSS Selector, and XPath locators on the same webpage, print confirmation messages for each located element, and display counts where multiple elements are found.


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




from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)

xpath1 = driver.find_element(By.XPATH,"//input[@id='name']")
xpath2 = driver.find_element(By.XPATH,"//input[@id='email']")
xpath3 = driver.find_element(By.XPATH,"//input[@id='phone']")
xpath4 = driver.find_element(By.XPATH,"//textarea[@id='textarea']")
xpath5 = driver.find_element(By.XPATH,"//button[text()='Submit']")

print("5 elements found using XPath")

xpath6 = driver.find_element(By.XPATH,"//h2[text()='Mouse Hover']")
xpath7 = driver.find_element(By.XPATH,"//button[text()='Point Me']")
xpath8 = driver.find_element(By.XPATH,"//option[contains(text(),'Lion')]")
print("8 elements found using XPath")



from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com")
sleep(5)

css1 = driver.find_element(By.CSS_SELECTOR,"a[title='Live Cricket Score']")
print("CSS selectors working")
print(css1)
css2 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Schedule']")
print("CSS selectors working")
print(css2)
css3 = driver.find_element(By.CSS_SELECTOR,"a[title='Cricket Series']")
print("CSS selectors working")
print(css3)

print("CSS selectors working")



x1 = driver.find_element(By.XPATH,"//a[@title='Live Cricket Score']")
print("XPath attribute working")
print(x1)
x2 = driver.find_element(By.XPATH,"//a[@title='Cricket Schedule']")
print("XPath attribute working")
print(x2)
x3 = driver.find_element(By.XPATH,"//a[@title='Cricket Series']")
print("XPath attribute working")
print(x3)

print("XPath attribute working")



t1 = driver.find_element(By.XPATH,"//a[text()='Series']")
print("XPath inner text working")
print(t1)
t2 = driver.find_element(By.XPATH,"//a[text()='Teams']")
print("XPath inner text working")
print(t2)
t3 = driver.find_element(By.XPATH,"//a[text()='News']")
print("XPath inner text working")
print(t3)

print("XPath inner text working")


sleep(3)
driver.quit()
