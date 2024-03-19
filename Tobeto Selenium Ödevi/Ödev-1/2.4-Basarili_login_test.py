from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")
        #print(errorMessage.text)
        testResult = errorMessage == driver.find_element(By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")
        print(f"TEST SONUCU: {testResult}")
        listCountTest = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print("Sayfa üzerindeki ürün sayisi:", len(listCountTest))


testClass = Test_Sauce()
testClass.test_invalid_login()