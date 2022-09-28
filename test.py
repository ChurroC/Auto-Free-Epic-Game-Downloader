import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


from dotenv import load_dotenv
load_dotenv()
import time
import os

driver = uc.Chrome(use_subprocess=True)

#Sign into google
def signIntoGoogle():
    driver.get('https://accounts.google.com/signin/v2/identifier?elo=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, 'identifierId')))
    driver.find_element(By.ID, 'identifierId').send_keys(os.getenv('EMAIL'), Keys.ENTER)
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.NAME, 'password')))
    driver.find_element(By.NAME, 'password').send_keys(os.getenv('PASSWORD'), Keys.ENTER)
    print('Signed Into Google For')

#Sign into epic
def signIntoEpicGame():
    driver.get('https://www.epicgames.com/id/login')
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, 'login-with-google')))
    driver.find_element(By.ID, 'login-with-google').click()
    WebDriverWait(driver, timeout=10).until(lambda test: driver.current_url == 'https://www.epicgames.com/account/personal')
    print('Signed Into Epic Games For')

#Find all free games
def findAllFreeGames():
    time.sleep(1)
    driver.get('https://store.epicgames.com/en-US/free-games')
    allFreeGames = driver.find_elements(By.XPATH, '//*[text()= "Free Now"]')
    print(allFreeGames)
    for index in range(len(allFreeGames)):
        index += 1
        collectOneFreeGame(index)

def collectOneFreeGame(index):
    print(index)
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, f'(//*[text()= "Free Now"])[{index}]')))
    driver.find_element(By.XPATH, f'(//*[text()= "Free Now"])[{index}]').click()

    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="css-8en90x"]/span[not(@*)]')))
    buttonText = driver.find_element(By.XPATH,'//*[@class="css-8en90x"]/span[not(@*)]').text
    print(buttonText)
    if buttonText == 'IN LIBRARY':
        return print('IN LIBRARY')
    
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="css-15fg505"]/div[not(@*)]/button[@data-testid="purchase-cta-button"]')))
    driver.find_element(By.XPATH, '//div[@class="css-15fg505"]/div[not(@*)]/button[@data-testid="purchase-cta-button"]').click()

    time.sleep(.5)

    if(expectedConditions('visibility_of_element_located', 'ID', 'agree', 3)):
        driver.find_element((By.ID, 'agree')).click()
        driver.find_element((By.XPATH, '//button[@class="css-1qqsbi4"]')).click()
        print('License Agreement Done')


    time.sleep(3)
    
    driver.get('https://store.epicgames.com/en-US/free-games')
    #print('hjko')
    #time.sleep(3)

def expectedConditions(whatElementConditions, typeOfSelections, selector, timeoutWait=10):
    try:
        WebDriverWait(driver, timeout=timeoutWait).until(EC[whatElementConditions]((By[typeOfSelections], selector)))
        return True
    except:
        return False


signIntoGoogle()
signIntoEpicGame()
findAllFreeGames()

time.sleep(10)