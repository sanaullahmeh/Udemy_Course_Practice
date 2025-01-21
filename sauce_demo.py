from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
BaseURL = 'https://www.saucedemo.com/'
username = 'standard_user'
password = 'secret_sauce'

class SauceDemo:
    def login(self,driver):
        driver.get(BaseURL)
        username_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"user-name"))
        )
        username_field.send_keys(username)
        password_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"password"))
        )
        password_field.send_keys(password)
        login_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"login-button"))
        )
        login_button.click()
        title = driver.title

        print(f"Login Successful - title of the loaded Page - {title}")
        items = driver.find_elements(By.XPATH,"//div[@class ='inventory_item']")
        for item in items:
            cart_button =item.find_element(By.XPATH,".//button")
            cart_button.click()
        item_count = len(items)
        print(f"Total Products on Page - {item_count}")
        cart_icon = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,".shopping_cart_link"))
        )
        cart_icon.click()
        time.sleep(2)
        checkout_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"checkout"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , checkout_button)
        checkout_button.click()
        time.sleep(2)
        



driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = SauceDemo()
    Runner.login(driver)
finally:
    driver.quit()