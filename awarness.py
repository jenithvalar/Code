from selenium.webdriver.common.by import By

from helper.seleniumhelper import SeleniumHelper


class Awarness(SeleniumHelper):
    logo = (By.XPATH, '//h4//i[@class="far fa-address-book"]')
    aw = (By.XPATH, '//div[@id="awareCarousel"]')
    close = (By.XPATH, '//A[@title="Close"]')
    next = (By.XPATH, '//a[@title="Next"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_AW(self):
        self.element_is_present(self.logo)
        self.element_click(self.aw)
        self.element_click(self.next)

        if self.element_is_present(self.close):
            self.element_click(self.close)

            report = "AW section is verified successfully"
            self.write_report_to_file(report,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\AW.txt")
        else:

            print("Close button not found")



