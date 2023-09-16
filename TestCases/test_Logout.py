import pytest
import time
import logging
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from PageObjects.Logout import LogoutPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen


class Test_002_Logout:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, setup):
        self.log.info("********************** Test_002_Logout *********************************")
        self.log.info("********************* Verifying Logout Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.lo = LogoutPage(self.driver)
        self.lo.clickLogout()
        self.driver.close()

