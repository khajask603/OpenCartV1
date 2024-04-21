import os.path
import time

from pageObjects.HomePage import HomePage
from pageObjects.AccountPage import AccountPage
from pageObjects.LoginPage import LoginPage
from utilities.custom_Logger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from utilities import XLUtils
import pytest



class Test_loginDDT():
    logger=LogGen.loggen()
    baseurl=ReadConfig.getApplicationUrl()

    path=os.path.abspath(os.path.curdir)+r"\testData\Opencart_LoginData.xlsx"
    def test_login_ddt(self,setup):
        self.logger.info("--------------Starting test_Login_DDT_Test----------")
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        lst_Status=[]

        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.Hp=HomePage(self.driver)
        self.Ap=AccountPage(self.driver)
        self.Lp=LoginPage(self.driver)

        for r in range(2, self.rows+1):
            self.Hp.clickMyAccount()
            self.Hp.clickLogin()
            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.pasword=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.Lp.set_Email(self.email)
            self.Lp.set_Paswword(self.pasword)
            self.Lp.click_Login()
            time.sleep(3)
            self.targetPage = self.Lp.isMy_AcoountPage_Exists()

            # from Excel Data if recived ->Valid (true+True Credntials=Valid)
            if self.exp=="Valid":
                if self.targetPage==True:               #Account Page Displayed with login pass right credntials
                    lst_Status.append("Pass")          #We are Updating empty list as pass for testCase INPUT LIST on TOP
                    self.Ap.Account_Button()
                    self.Ap.Logout_Button()
                else:
                    lst_Status.append("Fail")       #Even After the valid Data the Login Failed TC Should Fail


            # from Excel Data if recived ->INValid (true+False <-> False+True Credntials=IValid)
            elif self.exp=="Invalid":
                if self.targetPage == True:         # IF Account Page Displayed with login pass **INVALID** credntials
                    lst_Status.append("Fail")       # We are Updating empty list as FAIL  for testCase INPUT LIST on TOP
                    self.Ap.Account_Button()
                    self.Ap.Logout_Button()
                else:
                    lst_Status.append("Pass") #So Expected in testcases from excel with invalid  Data the Login Failed TC Should PASS
        self.driver.close()


        #FINAL VALIDTION->Above with respect to Excel data we are passing and failing
        #2) if Unexpected result shows in the User Defined list we will fial it/
        if "Pass" in lst_Status:
            assert True
        else:
            assert False

        self.logger.info(("---------------End of test driven Testing-----------------------"))

