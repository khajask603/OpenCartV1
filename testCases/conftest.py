import os
from datetime import datetime

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver=None                                                     #Declare Globally

# --------To invoke browser from comand line for browser
# 1)This will get the value from CLI
def pytest_addoption(parser):
    # parser.addoption("--browser")
    parser.addoption("--browser", action="store",default="chrome")     #Ign   oring as i kept chrome as default browser
    parser.addoption("--headless")

# 2)--------These Below fixture will take it from from top-----------
@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")
    headless = request.config.getoption("--headless")  # Check if headless option is passed from Jenkins

    global driver                                   # ---------Declare Globally
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("------------Launching Firefox Browser----------------")

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
            options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
        print("------------Launching Edge Browser----------------")
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:  # Check if headless mode is specified
            options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        print("------------Launching Chrome Browser----------------")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver  # Assign the driver to the class attribute
    yield driver
    driver.quit()


#----------------------------------------------------------------------------REPORTS------------------------------------------------------------
# customizing reHTML Report---------------------------------------------
@pytest.hookimpl()
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Orange HRM"
    config.stash[metadata_key]["Module Name"] = "Login Module"
    config.stash[metadata_key]["Tester Name"] = "Sk Khaja Mohiddin"
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

#------------------Removing Unneseray from report---------

# Optional hook for modifying pre-existing metadata (if needed)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # Remove if present
    metadata.pop("Plugins", None)   # Remove if present

#--These Below comand can be replaced with simple Comand execution using above hook
# pytest -s -v --html=reports\report.html --capture=tee-sys .\testCases\test_001_A
# ccountRegistration.py --browser chrome
#Ex_Simple command:--
# pytest -s -v testCases\test_001_AccountRegistration.py

#@pytest.hookimpl()---------------
# It is hook for Adding Environment info to HTML Report
#------------Genrtsing report without giving CMND Line Arguments using the below Hook--------------------
#Specifying report folder location and save report with timestamp

#----------------------------------------------------------------------------REPORTS------------------------------------------------------------
