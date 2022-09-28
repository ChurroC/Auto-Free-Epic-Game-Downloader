import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


from dotenv import load_dotenv
load_dotenv()
import os

driver = uc.Chrome(use_subprocess=True)

#Sign into google
def signIntoGoogle():
    driver.get('https://accounts.google.com/signin/v2/identifier?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'identifierId'))
    driver.find_element(By.ID, 'identifierId').send_keys(os.getenv('EMAIL'), Keys.ENTER)
    WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.NAME, 'password'))
    driver.find_element(By.NAME, 'password').send_keys(os.getenv('PASSWORD'), Keys.ENTER)
    print('Signed Into Google For')

#Sign into epic
def signIntoEpicGame():
    driver.get('https://www.epicgames.com/id/login')
    WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.ID, 'login-with-google'))
    driver.find_element(By.ID, 'login-with-google').click()
    print('Signed Into Epic Games For')

signIntoGoogle()
signIntoEpicGame()

WebDriverWait(driver, timeout=10).until(lambda test: test.find_element(By.NAME, 'awdadw'))