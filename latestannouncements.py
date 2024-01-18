from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class LatestAnnouncements(SeleniumHelper):
    LA = (By.XPATH, '//div[@class="card-body  basictext "]')
    logo = (By.XPATH, '//I[@class="fas fa-bullhorn"]')
    close = (By.XPATH, '//A[@title="Close"]')
    next = (By.XPATH, '//a[@title="Next"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_LA(self):
        self.element_is_present(self.logo)
        self.element_click(self.LA)
        if self.element_is_present(self.next):
            self.element_click(self.next)

            self.element_is_present(self.close)
            self.element_click(self.close)

            report = "LA section is verified successfully"
            self.write_report_to_file(report,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\LA.txt")
