from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    click_Logout_Xpath ="(//a[normalize-space()='Logout'])[1]"
    click_Account_button="//span[normalize-space()='My Account']"

    # ------------Constructore----------
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def Account_Button(self):
        AcButton=self.driver.find_element(By.XPATH,self.click_Account_button)
        AcButton.click()
    def Logout_Button(self):
        LogoUtButton = self.driver.find_element(By.XPATH, self.click_Logout_Xpath)
        LogoUtButton.click()