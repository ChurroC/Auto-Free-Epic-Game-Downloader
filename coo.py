from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from dotenv import load_dotenv
load_dotenv()
import os
import re
import time

epic_home_url = "https://www.epicgames.com/site/en-US/home"
epic_store_url = "https://www.epicgames.com/store/en-US"
epic_login_url = "https://www.epicgames.com/id/login/epic"
epic_logout_url = "https://www.epicgames.com/id/logout"

print(os.environ.get('GECKO_PATH'))
if (os.environ.get('GECKO_PATH')):
    driver = webdriver.Firefox(executable_path = os.getenv('GECKO_PATH'))
else:
    driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())

driver.get('https://www.epicgames.com/id/login')

#Sign into epic
WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'login-with-epic'))
driver.find_element(By.ID, 'login-with-epic').click()
WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'email'))
driver.find_element(By.ID, 'email').send_keys(os.getenv('EMAIL'))
driver.find_element(By.ID, 'password').send_keys(os.getenv('PASSWORD'))
WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'sign-in').is_enabled())
driver.find_element(By.ID, 'sign-in').click()

#captha
wait_redirect_count = 0
has_warned_captcha = False
print("Waiting to be automatically redirected to store page")
while not re.search(epic_store_url, driver.current_url):
    if (wait_redirect_count >= 5) & (has_warned_captcha == False):
        print("Still waiting - Possible captcha requiring completion")
        has_warned_captcha = True
    time.sleep(1)
    wait_redirect_count += 1
print("Successfully logged in " + os.getenv('EMAIL'))
driver.get(epic_store_url) # So it automatically waits until page is loaded
WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'site-nav'))
time.sleep(1)