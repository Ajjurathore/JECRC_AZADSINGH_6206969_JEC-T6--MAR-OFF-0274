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

# key = 'The Weekend'
#
# if select.is_multiple:
#     for option in select.options:
#         if key.lower() in option.text.lower():
#             option.click()

options = driver.find_elements(By.XPATH, '//optgroup[@label="The Weekend"]/option')

for key in options:
    key.click()

print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()

sleep(2)
driver.quit()