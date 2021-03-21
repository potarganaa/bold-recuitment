from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Configuration:
    URL_LINK = "https://app.interviewme.pl/login"
    MAX_WAIT_TIME = 5
    DEFAULT_PASS = "parmezan6"
    DEFAULT_LOGIN = "vincent-sqa+rekrutacja@bold.com"




    def open_application(self, url_link=URL_LINK):
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.get(url_link)

        return driver
