
from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TimeSheetLeaderboard(SeleniumHelper):
    logo = (By.XPATH, '(//div[@class="card-header card-header-danger card-header-text "])[2]')
    emp = (By.XPATH, '//b[text()="Employees"]')
    emvm = (By.XPATH, '//a[text()="View More"]')
    proj = (By.XPATH, '//b[text()="Projects"]')
    prvm = (By.XPATH, '(//div[@class="card-footer"])[2]')
    back = (By.XPATH, '//a[@class="btn btn-info"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver