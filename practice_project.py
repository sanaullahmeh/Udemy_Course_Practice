from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PracticeProject:
    def test_project(self,driver):
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        title = driver.title
        print(f"Title of the Page is - {title}")

        mobile_products = driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")
        for mobile in mobile_products:
            button =mobile.find_element(By.XPATH,".//button")
            button.click()
        time.sleep(2)

        checkout_button = driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']")
        checkout_button.click()

        mobile_count = len(mobile_products)
        print(f"Total Products on Page - {mobile_count}")
        time.sleep(2)

        final_checkout = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", final_checkout)
        final_checkout.click()
        time.sleep(2)
        address_field = driver.find_element(By.ID,"country")
        address_field.send_keys("Pak")
        selected_country = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT,"Pakistan"))
        )
        selected_country.click()
        time.sleep(2)

        checkbox_buttton = driver.find_element(By.XPATH,"//div[@class = 'checkbox checkbox-primary']")
        checkbox_buttton.click()
        purchase_button = driver.find_element(By.XPATH,"//input[@type='submit']")
        purchase_button.click()

        confirmation_message = driver.find_element(By.CSS_SELECTOR,".alert-success").text
        assert "Success! Thank you!" in confirmation_message ,f"Order not submitted"

        time.sleep(2)

        print("Complete Flow Automated")


driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = PracticeProject()
    Runner.test_project(driver)
finally:
    driver.quit()

        