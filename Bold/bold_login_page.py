from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import re

from bold_locators import LoginPageLocators
from bold_configuration import Configuration


class LoginPage(Configuration):
    def __init__(self, driver):
        self.locatorsPP = ProductsPageLocators()
        self.locatorsLP = LoginPageLocators()
        self.driver = driver

    def log_in(self, username, password):
        self.set_username_field(username)
        self.set_password_field(password)
        self.use_login_button()

    def set_username_field(self, username):
        self.username_field.send_keys(username)

    def set_password_field(self, password):
        self.password_field.send_keys(password)

    def use_login_button(self):
        self.login_button.click()


    @property
    def username_field(self):
        WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.locatorsLP.USERNAME_FIELD)))
        return self.driver.find_element_by_xpath(self.locatorsLP.USERNAME_FIELD)

    @property
    def password_field(self):
        WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.locatorsLP.PASSWORD_FIELD)))
        return self.driver.find_element_by_xpath(self.locatorsLP.PASSWORD_FIELD)

    @property
    def login_button(self):
        WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.locatorsLP.LOGIN_BUTTON)))
        return self.driver.find_element_by_xpath(self.locatorsLP.LOGIN_BUTTON)
