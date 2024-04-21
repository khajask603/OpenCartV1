from selenium.webdriver.common.by import By


class LoginPage():

    text_Email_Xpath="//input[@id='input-email']"
    text_Paswod_Xpath="//input[@id='input-password']"
    click_Login_Xpath="//input[@value='Login']"
    myAccount_Text_Xpath="//h2[text()='My Account']"

    def __init__(self,driver):
        self.driver=driver

    def set_Email(self,Email):
        self.driver.find_element(By.XPATH, self.text_Email_Xpath).send_keys(Email)

    def set_Paswword(self, password):
        self.driver.find_element(By.XPATH, self.text_Paswod_Xpath).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH, self.click_Login_Xpath).click()

    def isMy_AcoountPage_Exists(self):
        try:
            return self.driver.find_element(By.XPATH,self.myAccount_Text_Xpath).is_displayed()
        except:
            return False



