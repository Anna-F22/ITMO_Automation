from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    name = driver.find_element(By.CSS_SELECTOR,'#user-name')
    passw = driver.find_element(By.CSS_SELECTOR, '#password')
    button = driver.find_element(By.CSS_SELECTOR, 'button[type='submit']')

    if name is None or passw is None or button is None :
        print('Не найден')
    else:
        print('Найден')



