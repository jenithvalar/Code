import pytest
from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class DashboardMenus(SeleniumHelper):
    menu = (By.XPATH, '//*[@class="sidebar-nav m-t-10"]')
    dashboard = (By.XPATH, '//span[text()="Dashboard"]')
    text = (By.XPATH, '//b[text()="Employees"]')
    HumanResource = (By.XPATH, '//span[text()="Human Resource"]')
    HM = (By.XPATH, '//b[text()="Human Resource Dashboard"]')
    MyProfile = (By.XPATH, '//span[text()="My Profile"]')
    prof = (By.XPATH, '//a[text()="Profile"]')
    Reimbursements = (By.XPATH, '//span[text()="Reimbursements"]')
    reimbursement = (By.XPATH, '//h4[text()="My Reimbursements"]')
    MyColleague = (By.XPATH, '//span[text()="My Colleague"]')
    colleague = (By.XPATH, '//h3[text()="Know your colleague"]')
    Timesheet = (By.XPATH, '//span[text()="Timesheet"]')
    timesheet = (By.XPATH, '//h1[@class="pull-left"]')
    OpenPosition = (By.XPATH, '// span[text() = "Open Positions"]')
    position = (By.XPATH, '//h4[text()="Open Positions"]')
    Events = (By.XPATH, '//span[text()="Events"]')
    event = (By.XPATH, '//h4[@class="card-title"]')
    Forums = (By.XPATH, '//span[text()="Forums"]')
    forum = (By.XPATH, '//a[text()="New Discussion"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_all_menus(self):
        try:

            menus = self.get_element_text(self.menu)
            print(menus)
            menu = self.wait_for_element_to_be_present(self.dashboard, timeout=5)
            if menu:
                report = "".join(menus)
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\menu.txt")

            if self.element_is_present(self.text):
                report = "your in dashboard page"
                self.write_report_to_file(report, r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\dashboard.txt")

            self.element_click(self.HumanResource)
            if self.element_is_present(self.HM):
                report = "Your in HumanResource page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\HumanResource.txt")
                self.driver.back()

            self.element_click(self.MyProfile)
            if self.element_is_present(self.prof):
                report = "Your in MyProfile page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\MyProfile.txt")
                self.driver.back()

            self.element_click(self.Reimbursements)
            if self.element_is_present(self.reimbursement):
                report = "Your in Reimbursements page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\Reimbursements.txt")
                self.driver.back()

            self.element_click(self.MyColleague)
            if self.element_is_present(self.colleague):
                report = "Your in MyColleague page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\MyColleague.txt")
                self.driver.back()

            self.element_click(self.Timesheet)
            if self.element_is_present(self.timesheet):
                report = "Your in Timesheet page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\Timesheet.txt")
                self.driver.back()

            self.element_click(self.OpenPosition)
            if self.element_is_present(self.position):
                report = "Your in OpenPosition page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\OpenPosition.txt")
                self.driver.back()

            self.element_click(self.Events)
            if self.element_is_present(self.event):
                report = "Your in Events page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\Events.txt")
                self.driver.back()

            self.element_click(self.Forums)
            if self.element_is_present(self.forum):
                report = "Your in Forums page "
                self.write_report_to_file(report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\Forums.txt")
                self.driver.back()
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")
