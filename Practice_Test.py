import pytest
from selenium import webdriver
from time  import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")

hide_button = driver.find_element(By.ID,"hide-textbox")
hide_button.click()
sleep(5)
#Using Javascript
displayed_textbox = driver.find_element(By.ID, "displayed-text")
driver.execute_script("arguments[0].value = 'Hello World!'", displayed_textbox)
sleep(5)
show_button = driver.find_element(By.ID, "show-textbox")
show_button.click()
sleep(5)