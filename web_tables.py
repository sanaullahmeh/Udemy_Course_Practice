from selenium import webdriver
from selenium.webdriver.common.by import By

class WebTables:
    def handling_web_tables(self, driver):
        # Define the base URL
        base_url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
        
        # Navigate to the URL
        driver.get(base_url)
        
        # Step 1: Fetch the unstructured (unsorted) list of vegetables
        veggies_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
        unstructured_veggies_list = [veggie.text for veggie in veggies_elements]
        print(f"Unstructured (Unsorted) Items: {unstructured_veggies_list}")
        
        # Step 2: Click the column header to sort the table
        driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
        
        # Step 3: Fetch the sorted list of vegetables
        sorted_veggies_elements = driver.find_elements(By.XPATH, "//tr/td[1]")
        structured_veggies_list = [veggie.text for veggie in sorted_veggies_elements]
        print(f"Structured (Sorted) Items: {structured_veggies_list}")
        
        # Step 4: Validate the sorting
        manually_sorted_list = unstructured_veggies_list.copy()
        manually_sorted_list.sort()
        
        print(f"Manually Sorted List: {manually_sorted_list}")
        assert structured_veggies_list != manually_sorted_list, "Sorting functionality on the table does not work as expected!"

# Example Usage:
if __name__ == "__main__":
    driver = webdriver.Chrome()
    try:
        web_table = WebTables()
        web_table.handling_web_tables(driver)
    finally:
        driver.quit()


        