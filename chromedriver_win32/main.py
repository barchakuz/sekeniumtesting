from selenium import webdriver
import time
#SP20-BSE-057
#Behroze Aslam
driver = webdriver.Chrome('./chromedriver')
print("-----------------------------------")
print("Test.py Testing Started")
print("-----------------------------------\n\n")

driver.maximize_window()
driver.get("https://www.bbc.com/")
search_box = driver.find_element("name","password")
search_box.send_keys("secret_sauce")
time.sleep(3)
search_bar.clear()

time.sleep(3)
search_bar.send_key("Starting Python")

time.sleep(3)
driver_find_element("name","Login-button").click()

time.sleep(3)
search_bar.clear()
search_bar.send_key("secret_sauce")

time.sleep(3)
driver_find_element("name","Login-button").click()

time.sleep(3)
print("-----------------------------------")
print("Driver title is :-- ", driver.title)
print("-----------------------------------\n\n")
print(driver.current_url)
print("-----------------------------------")
print("Main.py Completed Sucessfully ")
print("-----------------------------------\n\n")