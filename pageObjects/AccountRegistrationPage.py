from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountRegister:
    # ------------Locatores----------
    txtbox_FirstName_ID = "input-firstname"
    txtbox_LastName_CSSID = "#input-lastname"
    txtbox_Email_Xpath = "//input[@id='input-email']"
    txtbox_Telephone_Xpath = "//input[@id='input-telephone']"
    txtbox_Pasword_ID = "input-password"
    txtbox_Confirm_Pasword_ID = "input-confirm"
    NewsLeter_Radio_Button_Xpath = "(//label/input[@type='radio'])[2]"
    policy_CheckBox_Xpath = "//input[@name='agree']"
    continue_Button_Xpath = "//input[@value='Continue']"
    txt_Msg_Confirmation_Xpath="//div/h1"


    # ------------Constructore----------
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ------------Action methods----------
    #1)FirstName
    def setFirstName(self, firstName):
        fnTXT = self.driver.find_element(By.ID, self.txtbox_FirstName_ID)
        fnTXT.send_keys(firstName)

    #2)LastName
    def setLastName(self, LastName):
        lnText = self.driver.find_element(By.CSS_SELECTOR, self.txtbox_LastName_CSSID)
        lnText.send_keys(LastName)

    def setEmail(self, Email):
        emailTXT = self.driver.find_element(By.XPATH, self.txtbox_Email_Xpath)
        emailTXT.send_keys(Email)

    #3)TelepohoneNumber
    def setTelephone(self, mobile):
        numberTXT = self.driver.find_element(By.XPATH, self.txtbox_Telephone_Xpath)
        numberTXT.send_keys(mobile)

    #4)Password
    def setpassword(self, pasword):
        paswrdTXT = self.driver.find_element(By.ID, self.txtbox_Pasword_ID)
        paswrdTXT.send_keys(pasword)

    #5)confpassword
    def setConfirm_password(self, cnfpasword):
        cnfPaswrdTXT = self.driver.find_element(By.ID, self.txtbox_Confirm_Pasword_ID)
        cnfPaswrdTXT.send_keys(cnfpasword)

    #6)NewsRadioButton
    def clickNews_RadioButton(self):
        cnfPaswrdTXT = self.driver.find_element(By.XPATH, self.NewsLeter_Radio_Button_Xpath)
        cnfPaswrdTXT.click()

    #7)PolicyCheckBox
    def click_policy_Button(self):
        pCButton = self.driver.find_element(By.XPATH, self.policy_CheckBox_Xpath)
        pCButton.click()

    #8)ContinueButton
    def continue_Button(self):
        ConButton = self.driver.find_element(By.XPATH, self.continue_Button_Xpath)
        ConButton.click()

    #9)AccountConfirmaton Text

    def getConfirmationMsg(self):
        try:
            msgTxt = self.driver.find_element(By.XPATH, self.txt_Msg_Confirmation_Xpath).text
            return msgTxt
        except:
            return None






