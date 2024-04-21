import os

from pageObjects.AccountRegistrationPage import AccountRegister
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountPage import AccountPage
from utilities import randomString
from utilities.readProperties import ReadConfig
from utilities.custom_Logger import LogGen


class Test_Acc_Reg_login():

    logger=LogGen.loggen()
    baseurl=ReadConfig.getApplicationUrl()
    password=ReadConfig.getPaswword()

    def test_Account_Reg_LOGIN(self, setup):

        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver = setup
        self.logger.info("Launching application")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        # HomePage Object
        self.hp = HomePage(self.driver)
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        # RegisterPage Object
        self.logger.info("-----Providing Costumer details for Registeration-----")
        self.regPage = AccountRegister(self.driver)
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
        self.confirmmsg = self.regPage.getConfirmationMsg()

        if self.confirmmsg == "Your Account Has Been Created!":
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

        #LOGIN TEST _CASE____________________
        self.logger.info("---------test__002_Login Strarted---------")
        #HomePage
        self.Hp=HomePage(self.driver)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.Hp.clickMyAccount()
        self.Hp.clickLogin()

        #LoginPage
        self.Lp=LoginPage(self.driver)
        self.Lp.set_Email(self.Email)
        self.Lp.set_Paswword(self.password)
        self.Lp.click_Login()
        self.targetPage=self.Lp.isMy_AcoountPage_Exists()
        if self.targetPage==True:
            assert True
            # self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_Login.png")
            self.logger.error("---------test__002_Login Failed---------")
            self.driver.close()
            assert False
        self.logger.info("---------END OF test__002_Login Completed---------")

