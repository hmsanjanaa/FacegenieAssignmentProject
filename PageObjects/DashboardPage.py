from selenium.webdriver.common.by import By


class DashboardPage:
    select_dasboard_xpath = "//span[normalize-space()='Dashboard']"
    select_attendence_xpath = "//span[text()='Attendance Logs']"
    select_analytics_xpath = "//span[text()='Analytics and Reports']"
    select_manage_xpath = "//span[text()='Manage Student']"
    select_licences_xpath = "//span[text()='Manage Licenses']"
    select_sync_xpath = "//span[text()='Manage Sync']"
    select_setting_xpath = "//span[text()='Setting']"

    def __init__(self, driver):
        self.driver = driver

    def goToDashboard(self):
        dashboard = self.driver.find_element(By.XPATH, self.select_dasboard_xpath)
        self.driver.execute_script("arguments[0].click();", dashboard)

    def goToAttendence(self):
        attendence = self.driver.find_element(By.XPATH, self.select_attendence_xpath)
        self.driver.execute_script("arguments[0].click();", attendence)

    def goToAnalytics(self):
        analytics = self.driver.find_element(By.XPATH, self.select_analytics_xpath)
        self.driver.execute_script("arguments[0].click();", analytics)

    def goToManageStudent(self):
        student = self.driver.find_element(By.XPATH, self.select_manage_xpath)
        self.driver.execute_script("arguments[0].click();", student)

    def goToManageLicences(self):
        licence = self.driver.find_element(By.XPATH, self.select_licences_xpath)
        self.driver.execute_script("arguments[0].click();", licence)

    def goToManageSync(self):
        sync = self.driver.find_element(By.XPATH, self.select_sync_xpath)
        self.driver.execute_script("arguments[0].click();", sync)

    def goToSettings(self):
        setting = self.driver.find_element(By.XPATH, self.select_setting_xpath)
        self.driver.execute_script("arguments[0].click();", setting)

