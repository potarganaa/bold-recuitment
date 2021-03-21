class Locators:
    """A class for common locators used in various pages"""


class LoginPageLocators(Locators):
    """A class for main page locators. All main page locators should come here"""
    USERNAME_FIELD = "//input[@name='email]"
    PASSWORD_FIELD = "//input[@name='password']"

    LOGIN_BUTTON = "//button[@data-cy='login-submit']"



class MainPageLocators(Locators):
    """A class for search results locators. All search results locators should come here"""
    TEST_CV = 'CV - TEST'
    CV_TEST = f"//input[@value='{TEST_CV}']"
    POBIERZ_CV_TEST = f"//input[@value='{TEST_CV}']/ancestor::div[@class='_2hgNI']//button//span[contains(text(),'Pobierz')]"
