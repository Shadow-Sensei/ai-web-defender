from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Firefox (works on Arch after installing geckodriver)
driver = webdriver.Firefox()

# Open your form page
driver.get("http://127.0.0.1:5001/login")

# Wait for page to load (optional)
time.sleep(1)

# Find input fields (replace names according to your form)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")

# Type into the fields
username.send_keys("admin")
password.send_keys("mysecretpassword")

# Submit the form
password.send_keys(Keys.ENTER)

# Optional: wait and print page title or body
time.sleep(2)
print("New page title:", driver.title)

driver.quit()
