from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



#                 drag and drop
#                   1
# driver = webdriver.Chrome()
# # driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
#
# btn = driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
# btn.click()
#
# sleep(3)
# actions = ActionChains(driver)
# orig_ele = driver.find_element(By.ID,"dragBox")
# target_ele = driver.find_element(By.ID,"notGreedyInnerDropBox")
# sleep(4)
# actions.drag_and_drop(orig_ele,target_ele).perform()
# sleep(4)

#                  2
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
#
# btn = driver.find_element(By.ID,'droppableExample-tab-revertable')
# btn.click()
#
# sleep(3)
# actions = ActionChains(driver)
#
# orig_ele1 = driver.find_element(By.ID,"notRevertable")
# target_ele1 = driver.find_element(By.ID,"droppable")
# actions.drag_and_drop(orig_ele1,target_ele1).perform()
# sleep(2)
#
# orig_ele = driver.find_element(By.ID,"revertable")
# target_ele = driver.find_element(By.ID,"droppable")
# actions.drag_and_drop(orig_ele,target_ele).perform()
# sleep(4)


#             //Mouse Hover

# driver = webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# action = ActionChains(driver)

# doogo = driver.find_element(By.XPATH,'//span[contains(text(),"Dogs")][1]')

# action.move_to_element(doogo).perform()
# sleep(5)


#          scrolling of elements

# driver = webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(3)
# # catto = driver.find_element(By.XPATH, "//div[@data-ganame='Breed 5']")

# actions.scroll_to_element(catto).perform()
# sleep(4)
#
# actions.scroll_by_amount(0,-1200).perform()
# sleep(4)


# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(4)
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(4)




#
# driver = webdriver.Chrome()
# driver.get(r"C:\Users\azads\OneDrive\Desktop\git\project\Day9\index.html")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(3)
# present = driver.find_element(By.ID,"presentAddress")
# permanent = driver.find_element(By.ID,"permanentAddress")
# present.send_keys('BabyRaj  is Mine Onlyyy')
# present.click()
# sleep(3)
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(3)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(3)
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep





#           password visibility

driver = webdriver.Chrome()
driver.get(r"C:\Users\azads\OneDrive\Desktop\git\project\Day9\index1.html")
driver.maximize_window()
actions = ActionChains(driver)

driver.find_element(By.ID,'password').send_keys("yoyo")
sleep(3)
show_pwd = driver.find_element(By.ID,'eyeBtn')
actions.click_and_hold(show_pwd).perform()
sleep(3)
actions.release().perform()
sleep(4)
