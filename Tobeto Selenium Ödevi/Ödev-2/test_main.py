from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

class Test_Sauce():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def teardown_method(self):
        self.driver.quit()
    
    def getData():
        return [("1","1"),("abc","123"),("deneme","secret_sauce")]

    def test_valid_login(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        locateLogo = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        testResult = locateLogo == WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[1]/div[2]/div")))
        print(f"Logo gorundu mu?: {testResult}")
        listCountTest = WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        print("Sayfa üzerindeki ürün sayisi:", len(listCountTest))

    def test_locked_out_user(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "locked_out_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_empty_pass_login(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_empty_login(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username is required"

    def test_add_to_cart(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addtoCard = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")))
        addtoCard.click()
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")))
        checkout.click()
        bikeLight = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div")))
        assert bikeLight.text == "Sauce Labs Bike Light"
         
    def test_remove_from_card(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addtoCard = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")))
        addtoCard.click()
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")))
        checkout.click()
        removefromCard = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='remove-sauce-labs-bike-light']")))
        removefromCard.click()

    @pytest.mark.parametrize("username,password",getData())
    def test_invalid_login(self,username,password):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,username)
        actions.send_keys_to_element(passwordInput,password)
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage =WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_empty_checkout_info(self):
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addtoCard = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-bike-light']")))
        addtoCard.click()
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a")))
        checkout.click()
        checkoutButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='checkout']")))
        checkoutButton.click()
        continueButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='continue']")))
        continueButton.click()
        errorMsg = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='checkout_info_container']/div/form/div[1]/div[4]/h3")))
        assert errorMsg.text == "Error: First Name is required"