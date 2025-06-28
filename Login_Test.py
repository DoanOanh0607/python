from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)

driver.get("https://google.com/")
print(driver.title)

driver.back()
print(driver.title)

# Wait for username field to be present
wait = WebDriverWait(driver, 10)
user_name = wait.until(EC.presence_of_element_located((By.NAME, "username")))
user_name.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for Dashboard text to appear
dashboard_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
assert dashboard_text.text == "Dashboard"

driver.quit()

