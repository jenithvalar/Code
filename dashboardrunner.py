import pytest
from pages.loginpage import LoginPage
from pages.logoutpage import LogoutPage
from pages.dashboardmenus import DashboardMenus
from pages.dashboard import Dashboard
from pages.latestannouncements import LatestAnnouncements
from pages.awarness import Awarness
from pages.timesheetleaderboardEmployee import TimeSheetLeaderboardEmployee
from pages.Greeting import Greeting
from pages.jobopenings import JobOpenings
from pages.eventgallery import EventGallery
from pages.fourms import Fourms


class TestDashboard:

    @pytest.fixture(autouse=True)
    def setup_class(self, base_url, browser_setup, dashboard_data):
        self.driver = browser_setup
        self.driver.get(base_url)

        self.login_page = LoginPage(self.driver)
        self.email = dashboard_data["email"]
        self.password = dashboard_data["password"]
        self.logout_page = LogoutPage(self.driver)
        self.dashboard_page = DashboardMenus(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.latest = LatestAnnouncements(self.driver)
        self.awarness = Awarness(self.driver)
        self.employee = TimeSheetLeaderboardEmployee(self.driver)
        self.greet = Greeting(self.driver)
        self.job = JobOpenings(self.driver)
        self.event = EventGallery(self.driver)
        self.fourm = Fourms(self.driver)

    def test_dashboard(self):
        try:
            self.login_page.test_aspire_login(self.email, self.password)
            self.logout_page.test_logout(self.email, self.password)
            self.dashboard_page.test_all_menus()
            self.dashboard.Dashboard_section()
            self.latest.test_LA()
            self.awarness.test_AW()
            self.employee.test_employee_TLB()

            self.greet.test_TSLB()
            self.job.test_jobopenings()
            self.event.test_eventgallery()
            self.fourm.test_fourms()

        except Exception as e:
            pytest.fail(f"An error occurred: {e}")
