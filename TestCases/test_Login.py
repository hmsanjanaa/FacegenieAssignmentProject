import time

import pytest
import logging
from PageObjects.LoginPage import LoginPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    log = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.log.info("********************** Test_001_Login *********************************")
        self.log.info("********************* Verifying HomePage Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == "Rai-Kpsr-Bams":
            assert True
            self.driver.close()
            self.log.info("********************* HomePage Title test PASSED ************************")
        else:
            self.log.error("********************* HomePage Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_hometitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.log.info("********************** Test_001_Login Test start *********************************")
        self.log.info("********************* Verifying Login ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)
        act_title = self.driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard/ Home']").text
        time.sleep(5)
        if act_title == "Dashboard/ Home":
            assert True
            self.driver.close()
            self.log.info("********************* Login Page test PASSED ************************")
        else:
            self.log.error("********************* Login Page test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
