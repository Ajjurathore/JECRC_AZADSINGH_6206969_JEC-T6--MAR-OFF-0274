
## Task 3

### Wikipedia Actions

Write a Python Selenium script for the following:

1. Navigate to `https://www.wikipedia.org/`
2. Find the search input field.
3. Find the **English** language link.
4. Find the main Wikipedia logo image.
5. Count how many language links are present in the central block using `find_elements()` and print the count.
6. Navigate back to the previous page.
7. Navigate forward.
8. Refresh the page.
9. Print the final page title.
10. Quit the browser.
from selenium import webdriver
from time import sleep

websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com",
    "https://www.python.org"
]

driver = webdriver.Chrome()

for site in websites:
    sleep(3)
    driver.get(site)

    print("Website:", site)
    print("Title:", driver.title)
    print("-" * 40)

driver.quit()
