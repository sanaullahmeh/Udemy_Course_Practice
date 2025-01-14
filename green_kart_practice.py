import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class GreenKart:
    def search_product(self,driver):
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        time.sleep(1)
        title = driver.title
        print(f'title of the page is - {title}')
        search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
        search_box.send_keys("Ca")
        time.sleep(2)
        products = driver.find_elements(By.XPATH,"//div[@class='products']/div")
        for product in products:
            product.find_element(By.XPATH,".//button").click()
            time.sleep(1)
        product_count = len(products)
        print(f"Total No of Products displayed - {product_count}")
        assert product_count > 2
    def cart_button(self,driver):
        cart_btn = driver.find_element(By.XPATH,"//img[@alt='Cart']")
        cart_btn.click()
        time.sleep(1)
        proceed_checkout = driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']")
        proceed_checkout.click()
        time.sleep(1)   
        prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p") 
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        print(f"total price of items - {sum}")
        total_amount = int(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
        assert total_amount == sum , f"Assertion got Failed"
        discount_text = driver.find_element(By.XPATH,"//b[normalize-space()='Total After Discount :']").text
        numeric_value = discount_text.split(':')[-1].strip()
        discount_amount = int(numeric_value)
        print(discount_amount)



  
        promo_code = driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']")
        promo_code.send_keys("rahulshettyacademy")
        promo_btn = driver.find_element(By.XPATH,"//button[@class = 'promoBtn']")
        promo_btn.click()
        time.sleep(10)
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = GreenKart()
    Runner.search_product(driver)
    Runner.cart_button(driver)
finally:
    driver.quit()