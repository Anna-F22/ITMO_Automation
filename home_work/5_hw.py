from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_elements(By.CSS_SELECTOR, "CSS Selectors")

user = driver.find_element(By.CSS_SELECTOR, 'user-name')
password = driver.find_element_by_name('password')

driver.find_element(By.XPATH, '//button[text()="submit"]')
submit_button = driver.find_element_by_xpath("//input[@name='submit'][@type='button']")


if user is None:
    print('Элемент не найден')
elif password is None:
    print('Элемент не найден')
elif submit_button is None:
    print('Элемент не найден')
else:
    print('Элемент найден')




