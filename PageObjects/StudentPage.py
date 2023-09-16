from selenium.webdriver.common.by import By


class StudentPage:
    manage_student_xpath = "//span[normalize-space()='Manage Student']"
    Student_name = "nameorId"
    class_div = "(//div[@id='demo-simple-select-helper'])[1]"
    class_li = "//li[normalize-space()='CLASS 5']"
    div_div = "(//div[@id='demo-simple-select-helper'])[2]"
    div_li = "//li[normalize-space()='A']"
    busno_div = "(//div[@id='demo-simple-select-helper'])[3]"
    busno_li = "//li[normalize-space()='004']"
    adm_div = "(//div[@id='demo-simple-select-helper'])[4]"
    adm_li = "//li[normalize-space()='Studying']"

    def __init__(self, driver):
        self.driver = driver

    def goToManageStudent(self):
        s = self.driver.find_element(By.XPATH, self.manage_student_xpath)
        self.driver.execute_script("arguments[0].click();", s)

    def searchStudentByName(self, name):
        self.driver.find_element(By.NAME, self.Student_name).send_keys(name)

    def searchStudentByClass(self):
        self.driver.find_element(By.XPATH, self.class_div).click()
        self.driver.find_element(By.XPATH, self.class_li).click()

    def searchStudentByDivision(self):
        self.driver.find_element(By.XPATH, self.div_div).click()
        self.driver.find_element(By.XPATH, self.div_li).click()

    def searchStudentByBusNo(self):
        self.driver.find_element(By.XPATH, self.busno_div).click()
        self.driver.find_element(By.XPATH, self.busno_li).click()

    def searchStudentByAdm(self):
        self.driver.find_element(By.XPATH, self.adm_div).click()
        self.driver.find_element(By.XPATH, self.adm_li).click()
