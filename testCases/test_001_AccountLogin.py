import os
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountPage import AccountPage
from pageObjects.AccountRegistrationPage import AccountRegister
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import LogGen

class Test_Login():
    logger=LogGen.loggen()
    baseurl=ReadConfig.getApplicationUrl()
    email=ReadConfig.getEmail()
    password=ReadConfig.getPaswword()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("****Login Test Started********")
        self.driver=setup
        self.logger.info("****Launching Browser*********")
        self.logger.info("---------test__002_Login Strarted---------")
        # HomePage
        self.Hp = HomePage(self.driver)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.Hp.clickMyAccount()
        self.Hp.clickLogin()

        # LoginPage
        self.Lp = LoginPage(self.driver)
        self.Lp.set_Email(self.email)
        self.Lp.set_Paswword(self.password)
        self.Lp.click_Login()
        self.targetPage = self.Lp.isMy_AcoountPage_Exists()
        if self.targetPage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Login.png")
            self.logger.error("---------test__002_Login Failed---------")
            self.driver.close()
            assert False
        self.driver.close()
        self.logger.info("---------END OF test__002_Login Completed---------")


