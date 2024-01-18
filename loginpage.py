import time
from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper



class LoginPage(SeleniumHelper):
    email_input = (By.XPATH, '//input[@type="email"]')
    password_input = (By.XPATH, '//input[@type="password"]')
    login_button = (By.XPATH, '//input[@id="submitbtn"]')
    profile_button = (By.XPATH, '//li[@class="nav-item dropdown"]')
    logout_button = (By.XPATH, '//button[@type="submit"]')
    dashboard = (By.XPATH, '//span[text()="Dashboard"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Define a test method for logging in
    def test_aspire_login(self, email, password):

        self.element_enter(self.email_input, email)
        self.element_enter(self.password_input, password)

        time.sleep(10)
        self.element_click(self.login_button)

        login_success = self.wait_for_element_to_be_present(self.profile_button, timeout=5)
        report = "The login was successful"
        if login_success:
            self.write_report_to_file(report,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\login.txt")




