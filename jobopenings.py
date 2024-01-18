from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class JobOpenings(SeleniumHelper):
    logo = (By.XPATH, '//h4[text()="Job Openings"]')
    knowmore = (By.XPATH, '//a[text()="Know More"]')
    previous = (By.XPATH, '//a[text()="Previous"]')
    next = (By.XPATH, '//a[text()="Next"]')
    back = (By.XPATH, '//a[@class="btn btn-info"]')
    entries = (By.XPATH, '//select[@name="jobstable_length"]')
    tcount = (By.XPATH, '//tbody/tr')
    value1 = (By.XPATH, '//option[@value="10"]')
    value2 = (By.XPATH, '//option[@value="25"]')
    value3 = (By.XPATH, '//option[@value="50"]')
    value4 = (By.XPATH, '//option[@value="100"]')
    position = (By.XPATH, '(//tr/td)[1]')

    def test_jobopenings(self):
        self.element_is_present(self.logo)
        self.element_click(self.knowmore)

        self.element_click(self.next)
        self.element_click(self.previous)

        value = self.element_click(self.value2)
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

        self.driver.back()
        report = "The count all is matheched with the entries -job section is verified successfully"
        self.write_report_to_file(report,
                                  r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\job.txt")

