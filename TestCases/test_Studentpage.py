import pytest
import time
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from PageObjects.StudentPage import StudentPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen
import logging


class Test_004_StudentPage:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen(logLevel=logging.INFO)

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********************** Test_004 *********************************")
        self.logger.info("********************* Verifying Student Page Title ************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        actual_title = self.driver.title
        if actual_title == "Rai-Kpsr-Bams":
            assert True
            self.driver.close()
            self.logger.info("********************* Student Page Title test PASSED ************************")

        else:
            self.logger.error("********************* Student Page Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_student(self, setup):
        self.logger.info("************* Test_004_StudentPage Logging started **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")
        self.student = StudentPage(self.driver)
        time.sleep(10)
        self.student.goToManageStudent()
        time.sleep(5)
        self.name = "sanjana"
        self.student.searchStudentByName(self.name)
        self.student.searchStudentByClass()
        self.student.searchStudentByDivision()
        self.student.searchStudentByBusNo()
        self.student.searchStudentByAdm()
        time.sleep(5)
        act_title = self.driver.find_element(By.XPATH, "//p[normalize-space()='Dashboard/ Manage Student']").text
        time.sleep(2)
        if act_title == "Dashboard/ Manage Student":
            assert True
            self.driver.close()
            self.logger.info("********************* Manage Student Title test PASSED ************************")
        else:
            self.logger.error("********************* Manage Student Title test FAILED ************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Studentpage.png")
            self.driver.close()
            assert False
        self.logger.info("************ Test_004_StudentPage Ended ***********")

