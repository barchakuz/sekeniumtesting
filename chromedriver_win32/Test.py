import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#SP20-BSE-057
driver = webdriver.Chrome('./chromedriver')
chrome_options = webdriver.ChromeOption()
chrome_options.add.argunment('--no-sanbox')
chrome_options.add.argunment('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',option=chrome_options)


print("-----------------------------------")
print("Test.py Testing Started")
print("-----------------------------------\n\n")

driver.maximize_window()
driver.get("https://www.youtube.com/")
time.sleep(3)
search_box = driver.find_element("name","q")
search_box.send_keys("ChromeDriver")
time.sleep(3)
search_box.submit()


print("-----------------------------------")
print("Driver title is :-- ", driver.title)
print("-----------------------------------\n\n")

driver.close()

print("-----------------------------------")
print("Test.py Completed Sucessfully ")
print("-----------------------------------\n\n")