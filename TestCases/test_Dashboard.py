import pytest
import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen
import logging


class Test_005_DashboardPage:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************** Test_005 *********************************")
        self.logger.info("********************* Verifying Dashboard Page Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == "Rai-Kpsr-Bams":
            assert True
            self.driver.close()
            self.logger.info("*********************  Dashboard Page Title test PASSED ************************")
        else:
            self.logger.error("*********************  Dashboard Page Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_DashboardPageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_dashboard(self, setup):
        self.logger.info("************* Test_004_DashboardPage Test started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("************* Login successful **********")
        self.ds = DashboardPage(self.driver)
        time.sleep(5)
        self.ds.goToAttendence()
        self.ds.goToAnalytics()
        self.ds.goToManageStudent()
        self.ds.goToManageLicences()
        self.ds.goToManageSync()
        self.ds.goToSettings()
        self.ds.goToDashboard()
        time.sleep(5)
        act_title = self.driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard/ Home']").text
        time.sleep(2)
        if act_title == "Dashboard/ Home":
            assert True
            self.driver.close()
            self.logger.info("********************* Manage Student Title test PASSED ************************")
        else:
            self.logger.error("********************* Manage Student Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Studentpage.png")
            self.driver.close()
            assert False
        self.logger.info("************ Test_005_DashboardPage Test Ended ***********")
