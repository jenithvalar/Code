from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class Greeting(SeleniumHelper):
    logo = (By.XPATH, '(//div[@class="card-header card-header-danger card-header-text "])[1]')
    birthday = (By.XPATH, '//a[@class="nav-link active"]')
    workAnniversary = (By.XPATH, '//a[@id="v-pills-profile-tab"]')
    left = (By.XPATH, '(//span[@class="glyphicon glyphicon-chevron-left"])[1]')
    right = (By.XPATH, '(//span[@class="glyphicon glyphicon-chevron-right"])[1]')
    page = (By.XPATH, '//body')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_TSLB(self):
        try:
            self.element_is_present(self.logo)

            if self.element_is_present(self.birthday):
                self.element_click(self.birthday)

                left_arrow = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.left))
                left_arrow.click()

                # Wait for the right arrow to be clickable
                right_arrow = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.right))
                right_arrow.click()

            if self.element_is_present(self.workAnniversary):
                self.element_click(self.workAnniversary)

                report = "Greeting section is verified successfully"
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\greet.txt")

        except TimeoutException as e:
            print(f"TimeoutException: {e}")

        except StaleElementReferenceException:
            # Handle stale element exception, e.g., by refreshing the page
            self.driver.refresh()
