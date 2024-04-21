from selenium.webdriver.common.by import By

class HomePage():
    lnk_myaccount_xpath = "//a[@title='My Account']"
    register_LinkText = "Register"
    Login_LinkText = "Login"

    # Condstructores---------
    def __init__(self, driver):
        self.driver = driver

    # ActionsMethods---------

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT, self.register_LinkText).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT, self.Login_LinkText).click()
