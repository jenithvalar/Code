from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class TimeSheetLeaderboardEmployee(SeleniumHelper):
    logo = (By.XPATH, '(//div[@class="card-header card-header-danger card-header-text"])[3]')
    emp = (By.XPATH, '//b[text()="Employees"]')
    emvm = (By.XPATH, '//a[text()="View More"]')
    entries = (By.XPATH, '//select[@name="emp_metrics_length"]')
    tcount = (By.XPATH, '//tbody/tr')
    previous = (By.XPATH, '//a[text()="Previous"]')
    next = (By.XPATH, '//a[text()="Next"]')
    back = (By.XPATH, '//a[@class="btn btn-info"]')
    member = (By.XPATH, '(//tr/td)[3]')
    value1 = (By.XPATH, '//option[@value="10"]')
    value2 = (By.XPATH, '//option[@value="25"]')
    value3 = (By.XPATH, '//option[@value="50"]')
    value4 = (By.XPATH, '//option[@value="100"]')
    profile = (By.XPATH, '//div[@class="card-body ctm"]')
    backlist = (By.XPATH, '//a[@class="btn btn-info"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_employee_TLB(self):
        self.element_is_present(self.logo)
        self.element_is_present(self.emp)
        self.element_is_present(self.emvm)
        self.element_click_with_retry(self.emvm)

        self.element_click(self.next)
        self.element_click(self.previous)

        value = self.element_click(self.value3)
        count = len(self.find_elements(self.tcount))

        if value == count:
            print("value is 25")

        value = self.element_click(self.value1)
        count = len(self.find_elements(self.tcount))

        if value == count:
            print("value is 10")

        value = self.element_click(self.value3)
        count = len(self.find_elements(self.tcount))

        if value == count:
            print("value is 50")

        value = self.element_click(self.value4)
        count = len(self.find_elements(self.tcount))

        if value == count:
            print("value is 100")

        report = "The the count of the entries an the number of employee are same"
        self.write_report_to_file(report,
                                  r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\employeescount.txt")

        self.driver.back()
