from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.common.by import By


class EventGallery(SeleniumHelper):
    logo = (By.XPATH, '//h4[text()="Event Gallery"]')
    loadmore = (By.XPATH, '(//a[text()="Load More"])[1]')
    eventbody = (By.XPATH, '//h4[@class="card-title"]')
    viewmore = (By.XPATH, '//div[@class="card-footer"]')
    backtolist = (By.XPATH, '//a[@class="btn btn-default"]')

    def test_eventgallery(self):
        self.element_is_present(self.logo)

        self.element_click(self.loadmore)

        self.element_is_present(self.eventbody)

        events = self.driver.find_elements(*self.eventbody)
        for event in events:
            event_text = event.text
            print(f"Event Title: {event_text}")

        self.driver.back()

        report = "Event Gallery section is verified successfully"
        self.write_report_to_file(report,
                                  r"C:\Users\jenith.ravichandran\PycharmProjects\AspireDashboard\reports\event.txt")
