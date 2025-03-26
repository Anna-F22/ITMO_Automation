from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    name = driver.find_element(By.CSS_SELECTOR,'#user-name')
    passw = driver.find_element(By.CSS_SELECTOR, '#password')
    button_s = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if name is None or passw is None or button_s is None:
        print('Не найден')
    else:
        print('Найден')





