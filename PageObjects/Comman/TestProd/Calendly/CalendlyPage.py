from PageObjects.Comman.Calendly.CalendlyXpath import CalendlyXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class CalendlyPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Switching to Calendly frame")
    def switching_to_calendly_frame(self):
        try:
            self.wait_for_sync(5)
            self.switch_to_iframe(CalendlyXpath.calendly_frame)
            self.wait_for_sync(5)
        except Exception as e:
            allure.attach(str(e), name="switching_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Switching to Calendly frame 2")
    def switching_to_calendly_frame_2(self):
        try:
            self.wait_for_sync(5)
            self.switch_to_iframe(CalendlyXpath.calendly_frame_2)
            self.wait_for_sync(5)
        except Exception as e:
            allure.attach(str(e), name="switching_frame_2_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting available date")
    def select_available_date(self, date):
        try:
            # self.mouse_click_action(date)
            self.wait_and_click(date)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_available_date_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting available time")
    def select_available_time(self, time):
        try:
            # self.mouse_click_action(time)
            self.wait_and_click(time)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_available_time_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Move to next month")
    def next_month(self):
        try:
            self.mouse_click_action(CalendlyXpath.next_month)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="next_month_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View next month")
    def view_next_month(self):
        try:
            move_to_next_month = self.check_element(CalendlyXpath.view_next_month)
            if move_to_next_month:
                self.mouse_click_action(CalendlyXpath.view_next_month)
                self.wait_for_sync(2)
                self.log.info("Slots are not available in this month, moved to next month")
            else:
                allure.attach(str("Slots are available in this month"), self.driver.get_screenshot_as_png(), name="available_slots_of_this_month",
                              attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="view_next_month_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Selecting Available Slot from Calendly")
    def select_available_slot(self):
        try:
            # Locate available dates
            available_dates = self.get_element_list(CalendlyXpath.available_dates)
            if available_dates:
                # Click on the first available date
                self.select_available_date(available_dates[0])
                # Wait for time slots to load and click on the first available time slot
                available_time_slots = self.get_element_list(CalendlyXpath.available_time_slots)
                if available_time_slots:
                    self.select_available_time(available_time_slots[0])
                    self.wait_for_sync(5)

            else:
                # Click the next month button
                self.next_month()
                # Wait for the next month to load and recursively call the function again
                self.wait_for_sync(2)
                self.select_available_slot()
        except Exception as e:
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="select_available_slot_exception",
                          attachment_type=allure.attachment_type.PNG)
            raise

    @allure.step("Click on Next button")
    def click_next_button(self):
        try:
            self.mouse_click_action(CalendlyXpath.next_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="click_next_button_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Schedule button")
    def schedule_appointment(self):
        try:
            self.mouse_click_action(CalendlyXpath.schedule_btn)
            self.wait_for_sync(5)
        except Exception as e:
            allure.attach(str(e), name="schedule_appointment_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking next button to onboard")
    def click_next_onboard(self):
        try:
            self.mouse_click_action(CalendlyXpath.agree_btn)
            self.mouse_click_action(CalendlyXpath.next_onboarding_btn)
            self.mouse_click_action(CalendlyXpath.next_onboarding_btn)
            self.mouse_click_action(CalendlyXpath.next_onboarding_btn)
            self.mouse_click_action(CalendlyXpath.next_onboarding_btn)
            self.mouse_click_action(CalendlyXpath.next_onboarding_btn)
            self.wait_for_sync(20)
        except Exception as e:
            allure.attach(str(e), name="click_next_onboard_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Calendly Book Appointment")
    def calendly_book_appointment(self):
        self.switching_to_calendly_frame()
        self.switching_to_calendly_frame_2()
        # self.view_next_month()
        self.select_available_slot()
        self.click_next_button()
        self.schedule_appointment()
        # self.click_next_onboard()


