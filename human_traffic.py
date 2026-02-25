import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---------- CONFIG ----------
URL = "http://127.0.0.1:5000/login"
USERNAME = "sufi"
PASSWORD = "wrongpassword"   # try wrong once, then right
ATTEMPTS = 3                 # low number = human
# ----------------------------

def human_delay(a=0.3, b=1.2):
    time.sleep(random.uniform(a, b))

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.25))

# ---------- DRIVER ----------
driver = webdriver.Firefox()   # or Chrome()
driver.get(URL)

human_delay(2, 4)

for i in range(ATTEMPTS):
    print(f"[HUMAN] Attempt {i+1}")

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.clear()
    password_input.clear()

    human_typing(username_input, USERNAME)
    human_delay()

    # First attempt wrong, last attempt correct (human behavior)
    if i == ATTEMPTS - 1:
        human_typing(password_input, "12345")
    else:
        human_typing(password_input, PASSWORD)

    human_delay()

    password_input.send_keys(Keys.RETURN)

    # Wait after login attempt
    human_delay(3, 6)

    # Human might refresh or navigate slowly
    if random.random() < 0.3:
        driver.refresh()
        human_delay(2, 4)

# Stay idle (human reading page)
human_delay(5, 8)

driver.quit()
print("[HUMAN] Done")
