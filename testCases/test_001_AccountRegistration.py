import os

import pytest

from pageObjects.AccountPage import AccountPage
from pageObjects.AccountRegistrationPage import AccountRegister
from pageObjects.HomePage import HomePage
from utilities import randomString, readProperties
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import LogGen

class Test_001_AccountReg:
    # baseurl="https://naveenautomationlabs.com/opencart/index.php?route=common/home"
    baseurl=ReadConfig.getApplicationUrl()
    logger=LogGen.loggen() # for logging

    @pytest.mark.regression
    def test_Account_reg(self,setup):
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver=setup
        self.logger.info("Launching application")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

    #HomePage Object
        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

    #RegisterPage Object
        self.logger.info("-----Providing Costumer details for Registeration-----")
        self.regPage=AccountRegister(self.driver)
        self.regPage.setFirstName("John")
        self.regPage.setLastName("wick")
        self.Email = randomString.random_string_generator() + '@gmail.com'
        self.regPage.setEmail(self.Email)
        self.regPage.setTelephone("+8721190248")
        self.regPage.setpassword("White@456")
        self.regPage.setConfirm_password("White@456")
        self.regPage.clickNews_RadioButton()
        self.regPage.click_policy_Button()
        self.regPage.continue_Button()
        self.confirmmsg=self.regPage.getConfirmationMsg()
        if self.confirmmsg=="Your Account Has Been Created!":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_Acunt_Reg.png")
            self.logger.error("Account registration is failed.")
            assert False
        self.logger.info("**** test_001_AccountRegistration finished *** ")
        #AccountPAGE0------------------
        self.Ap=AccountPage(self.driver)
        self.Ap.Account_Button()
        self.Ap.Logout_Button()
        self.driver.close()









