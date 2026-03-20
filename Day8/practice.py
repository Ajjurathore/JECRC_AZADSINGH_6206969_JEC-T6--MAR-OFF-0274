# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# select = driver.find_element(By.XPATH,"//")
# if select.is_multiple():
#     select.select_by_value("blue")
#     select.select_by_index(3)
#     select.select_by_visible_text("Red")
#
# print('before deslect',[i.text for i in select.all_selected_options])
# sleep(3)
#
# select.deselect_by_value("blue")
# print('after deselect',[i.text for i in select.all_selected_options])

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get(r"C:\Users\azads\OneDrive\Desktop\git\project\Day8\index.html")
driver.maximize_window()

song_list = driver.find_element(By.ID,'songs')
select = Select(song_list)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text("Shape of you")
    select.select_by_visible_text("Animals")

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()

sleep(4)
driver.quit()