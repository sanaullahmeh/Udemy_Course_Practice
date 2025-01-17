import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
expected_list = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
actual_list = []
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
            actual_list.append(product.find_element(By.XPATH,".//h4").text)
            product.find_element(By.XPATH,".//button").click()
            time.sleep(1)
        assert expected_list == actual_list ,f"Actual List is not same as Expected"
        print(f"List of Products - {actual_list}")
        
            
        product_count = len(products)
        print(f"Total No of Products displayed - {product_count}")
        assert product_count > 2
    def cart_button(self,driver):
        cart_btn = driver.find_element(By.XPATH,"//img[@alt='Cart']")
        cart_btn.click()
        time.sleep(1)
        proceed_checkout = driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']")
        proceed_checkout.click()
        driver.save_screenshot("screen.png")
        time.sleep(1)   
        prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p") 
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        print(f"total price of items - {sum}")
        total_amount = int(driver.find_element(By.XPATH,"//span[@class='discountAmt']").text)
        assert total_amount == sum , f"Assertion got Failed"
        promo_code = driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']")
        promo_code.send_keys("rahulshettyacademy")
        promo_btn = driver.find_element(By.XPATH,"//button[@class = 'promoBtn']")
        promo_btn.click()
        time.sleep(10)
        discounted_price = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
        discounted_price != total_amount , f"Discount Code Error"
        print(f"Total Price is - {total_amount} - Discounted Price is - {discounted_price}" )
        discount_per = driver.find_element(By.CSS_SELECTOR,".discountPerc")
        discount_per_text = discount_per.text
        expected_discount_per = "10%"
        assert discount_per_text == expected_discount_per, f"Expected {expected_discount_per}, but got {discount_per_text}"
        print(f"Assertion Passed - Discount Percentage is {discount_per_text}")
    
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Runner = GreenKart()
    Runner.search_product(driver)
    Runner.cart_button(driver)
finally:
    driver.quit()