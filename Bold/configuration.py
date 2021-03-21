from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Configuration:
    URL_LINK = "https://www.saucedemo.com/"
    MAX_WAIT_TIME = 5
    DEFAULT_PASS = "secret_sauce"

    LOCKED_OUT_USER_ERROR_TEXT = "Sorry, this user has been locked out."
    INCORRECT_LOGIN_DATA_ERROR_TEXT = "Username and password do not match any user in this service"
    MISSING_USERNAME_ERROR_TEXT = "Username is required"
    MISSING_PASSWORD_ERROR_TEXT = "Password is required"

    MAIN_PAGE_LABEL_TEXT = "Products"

    USERS = {
        "standard": {
            "username": "standard_user",
            "password": DEFAULT_PASS
        },
        "locked": {
            "username": "locked_out_user",
            "password": DEFAULT_PASS
        },
        "problem": {
            "username": "problem_user",
            "password": DEFAULT_PASS
        },
        "performance": {
            "username": "performance_glitch_user",
            "password": DEFAULT_PASS
        }
    }
    USERS_CREDENTIALS_LIST = {USERS["standard"]["username"], USERS["locked"]["username"], USERS["problem"]["username"], USERS["performance"]["username"]}
    SORT_TYPE_LIST = {"NAME_ASC": "Name (A to Z)",
                      "NAME_DESC": "Name (Z to A)",
                      "PRICE_ASC": "Price (low to high)",
                      "PRICE_DESC": "Price (high to low)"}

    def open_application(self, url_link=URL_LINK):
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.get(url_link)

        return driver
