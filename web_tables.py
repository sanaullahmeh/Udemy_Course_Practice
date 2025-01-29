from selenium import webdriver
from selenium.webdriver.common.by import By

class WebTables:
    def handling_web_tables(self, driver):

        base_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
        
        driver.get(base_url)
        
        veggies_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
        unstructured_veggies_list = [veggie.text for veggie in veggies_elements]
        print(f"Unstructured (Unsorted) Items: {unstructured_veggies_list}")
        
        driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
        
        sorted_veggies_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
        structured_veggies_list = [veggie.text for veggie in sorted_veggies_elements]
        print(f"Structured (Sorted) Items: {structured_veggies_list}")
        
        manually_sorted_list = unstructured_veggies_list.copy()
        manually_sorted_list.sort()
        print(f"Manually Sorted List: {manually_sorted_list}")
        assert structured_veggies_list != manually_sorted_list, "Sorting functionality on the table does not work as expected!"

if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        web_table = WebTables()
        web_table.handling_web_tables(driver)
    finally:
        driver.quit()


        