from selenium.webdriver.common.by import By

from helper.seleniumhelper import SeleniumHelper


class Dashboard(SeleniumHelper):
    section1 = (By.XPATH, '(//h4[@class="card-title"])[1]')
    section2 = (By.XPATH, '(//h4[@class="card-title"])[2]')
    section3 = (By.XPATH, '(//h4[@class="card-title"])[3]')
    section4 = (By.XPATH, '(//h4[@class="card-title"])[4]')
    section5 = (By.XPATH, '(//h4[@class="card-title"])[5]')
    section6 = (By.XPATH, '(//h4[@class="card-title"])[6]')
    section7 = (By.XPATH, '(//h4[@class="card-title"])[7]')
    section8 = (By.XPATH, '(//h4[@class="card-title"])[8]')
    section9 = (By.XPATH, '(//h4[@class="card-title"])[9]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Dashboard_section(self):
        sections = [self.section1, self.section2, self.section3, self.section4, self.section5, self.section6,
                    self.section7, self.section8, self.section9]

        for section_locator in sections:
            section_element = self.driver.find_element(*section_locator)
            section_text = section_element.text
            print(section_text)

            Dsection_success = self.wait_for_element_to_be_present(self.section1, timeout=5)
            report = "All Nine Section are avaliable in Dashboard section"
            if Dsection_success:
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\section.txt")
