from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import re

from bold_locators import MainPageLocators
from bold_configuration import Configuration


class MainPage(Configuration):
    def __init__(self, driver):
        self.locatorsMP = MainPageLocators()
        self.driver = driver


    def is_cv_test_present(self):
        try:
            WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
                EC.invisibility_of_element((By.XPATH, self.locatorsMP.CV_TEST)))
            return True
        except (TimeoutException, NoSuchElementException):
            return False
    
    def use_pobierz_button(self):
        self.cv_test_pobierz_button.click()

    @property
    def cv_test_link(self):
        WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.locatorsMP.CV_TEST)))
        return self.driver.find_element_by_xpath(self.locatorsMP.CV_TEST)
    
    @property
    def cv_test_pobierz_button(self):
        WebDriverWait(self.driver, self.MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH, self.locatorsMP.POBIERZ_CV_TEST)))
        return self.driver.find_element_by_xpath(self.locatorsMP.POBIERZ_CV_TEST)
