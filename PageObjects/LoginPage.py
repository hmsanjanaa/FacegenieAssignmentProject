from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_username_name = "email"
    textbox_password_name = "password"
    button_submit_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

