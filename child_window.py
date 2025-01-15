import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class ChildWindows:
    def handling_child_window(self,driver):
        driver.implicitly_wait(2)
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.find_element(By.LINK_TEXT,"Click Here").click()
        title = driver.title
        print(title)
        windows_opened = driver.window_handles

        driver.switch_to.window(windows_opened[1])
        print(driver.find_element(By.TAG_NAME,"h3").text)
        title_two = driver.title
        print(f"Page Two title - {title_two}")
        driver.close
        driver.switch_to.window(windows_opened[0])
        time.sleep(1)
        assert "Opening a new window" in (driver.find_element(By.TAG_NAME,"h3").text)
        print("Assertion Passed")
driver = webdriver.Chrome()
driver.maximize_window()
try:
    Run = ChildWindows()
    Run.handling_child_window(driver)
finally:
    driver.quit()

