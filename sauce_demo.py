from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BaseURL = 'https://www.saucedemo.com/'
username = 'standard_user'
password = 'secret_sauce'
first_name = "John"
last_name = "Doe"
postal_code = 5474

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
        checkout_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"checkout"))
        )
        driver.execute_script("arguments[0].scrollIntoView()" , checkout_button)
        checkout_button.click()
        firstname_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"first-name"))
        )
        firstname_field.send_keys(first_name)

        lastname_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"last-name"))
        )
        lastname_field.send_keys(last_name)

        postalcode_field = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.ID,"postal-code"))
        )
        postalcode_field.send_keys(postal_code)
        continue_button = driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_button.click()

        item_total = driver.find_element(By.CSS_SELECTOR,".summary_subtotal_label").text
        assert item_total == 'Item total: $129.94', f"Expected Item total price is not as expected. Found: {item_total}"

        tax_percentage = driver.find_element(By.CSS_SELECTOR,".summary_tax_label").text
        assert '$10.40' in tax_percentage , f"Expected tax to be 10.40 but found {tax_percentage}"

        finish_button = driver.find_element(By.CSS_SELECTOR,"#finish")
        finish_button.click()

        success_message = driver.find_element(By.CSS_SELECTOR,".complete-header").text
        assert "Thank you" in success_message , f"checkout process failed"
        print(f"Whole Flow Automated of Sauce Demo - {success_message}")

driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = SauceDemo()
    Runner.login(driver)
finally:
    driver.quit()