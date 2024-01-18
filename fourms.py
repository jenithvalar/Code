from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class Fourms(SeleniumHelper):
    logo = (By.XPATH, '//h4[text()="Forum Topics"]')
    loadmore = (By.XPATH, '(//div[@class="stats"])[4]')
    web = (By.XPATH, '//ul[@class="navbar-nav float-left mr-auto"]/li')

    def test_fourms(self):
        self.element_is_present(self.logo)
        self.element_is_present(self.loadmore)
        self.element_click(self.loadmore)

        web = self.wait_for_element_to_be_present(self.web, timeout=5)
        report = "Fourms page is successfully navigated and it is verified"
        if web:
            self.write_report_to_file(report,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\fourms.txt")

