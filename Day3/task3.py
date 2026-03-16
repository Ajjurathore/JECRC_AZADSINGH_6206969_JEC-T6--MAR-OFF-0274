## Task 3
Write a Selenium script for the following:

1. Navigate to `https://www.amazon.in/`
2. Locate the main search bar using its ID with a CSS Selector.
3. Locate the Amazon logo using a CSS Selector.
4. Locate the **Cart** link/icon using a CSS Selector.
5. Locate the **Sign in** link in the navigation bar using descendant selector syntax.
6. Locate all the main category links in the navigation bar under **All**, using their common parent. Find all the `a` tags within it using `find_elements()` and print the count.
  
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# launch browser
driver = webdriver.Chrome()

# 1. open website
driver.get("https://www.amazon.in/")
sleep(4)

print("Amazon website opened")

# 2. locate search bar using CSS selector (ID)
search_bar = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
print("Search bar located")

# 3. locate Amazon logo using CSS selector
logo = driver.find_element(By.CSS_SELECTOR,"#nav-logo-sprites")
print("Amazon logo located")

# 4. locate Cart link/icon
cart = driver.find_element(By.CSS_SELECTOR,"#nav-cart")
print("Cart icon located")

# 5. locate Sign in link using descendant selector
signin = driver.find_element(By.CSS_SELECTOR,"#nav-tools a")
print("Sign in section located")

# 6. locate all category links under navigation bar
categories = driver.find_elements(By.CSS_SELECTOR,"#nav-xshop a")
print("Number of category links:", len(categories))

sleep(3)

driver.quit()
