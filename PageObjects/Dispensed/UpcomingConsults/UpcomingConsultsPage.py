from PageObjects.Dispensed.UpcomingConsults.UpcomingConsultsXpath import UpcomingConsultsXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader


class UpcomingConsultsPage(BaseHelpers):
    def __init__(self, driver, path, sheet, row, col):
        super().__init__(driver)
        self.email_address = data_reader.get_cell_data(path, sheet, row, col)
        self.fname = data_reader.get_cell_data(path, sheet, 2, 2)
        self.lname = data_reader.get_cell_data(path, sheet, 2, 3)

    @allure.step("Verify order no, status, Doctor and consultation")
    def verify_patient_nurse_row_header(self):
        try:
            self.wait_for_sync(5)
            order_id = self.get_text_from_element(UpcomingConsultsXpath.read_order_id)
            self.log.info(" Order Id " + order_id)
            if int(order_id) > 50:
                assert True
            else:
                assert False

            patient_name = self.get_text_from_element(UpcomingConsultsXpath.read_patient_name)
            self.log.info(" Patient Name " + patient_name)
            expected = str(self.fname) + " " + str(self.lname)
            if patient_name.lower() == expected.lower():
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="get_text_patient_row_header", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Read Upcoming consults number")
    def upcoming_consults_number(self):
        try:
            return self.get_text_from_element(UpcomingConsultsXpath.read_missed_consults_number)
        except Exception as e:
            allure.attach(str(e), name="get_text_upcoming_consults_number", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Return Patient status")
    def get_patient_status(self):
        try:
            return self.get_text_from_element(UpcomingConsultsXpath.read_patient_status)
        except Exception as e:
            allure.attach(str(e), name="get_text_upcoming_consults_number", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Searching patient appointment using email")
    def search_consultations(self):
        try:
            self.enter_text_action(self.email_address, UpcomingConsultsXpath.search_box)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Patient name link")
    def click_on_patient_name(self):
        try:
            self.log.info("Patient name is " + self.fname + " " + self.lname)
            patient_link = self.fname + " " + self.lname
            self.wait_for_sync(3)

            # self.click_on_link("Yash2024-08-14 Gaikwad14:27:31")
            # self.driver.click(patient_link)
            # self.click_on_link("Yash2024-07-03")
            self.mouse_click_action(UpcomingConsultsXpath.first_in_table_xpath)
            # self.mouse_click_action(patient_link,locator_type="link",max_time_out=5)
            # self.mouse_click_action(patient_link, locator_type="link", max_time_out=5)

            self.wait_for_sync(20)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Review Application button")
    def review_application(self):
        try:
            self.mouse_click_action(UpcomingConsultsXpath.review_application_btn)
        except Exception as e:
            allure.attach(str(e), name="review_application_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify email present in  page")
    def verify_email_present_in_page(self):
        try:
            search_text = self.email_address
            actual = self.get_text_from_element(UpcomingConsultsXpath.get_email_from_search_page)
            self.log.info(" Expected: " + search_text + " and Actual " + actual)
            if actual.lower() == search_text.lower():
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_email_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify the Patient summary text present")
    def verify_patient_summary_text_present(self):
        try:
            expected = "Patient Summary"
            actual = self.get_text_from_element(UpcomingConsultsXpath.patient_summary_text)
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="review_application_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify the Patient name is present")
    def verify_patient_email_id_present(self):
        try:
            expected = "Patient Summary"
            actual = self.get_text_from_element(UpcomingConsultsXpath.patient_summary_text)
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="review_application_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    # @allure.step("Click on Patient name")
    # def click_on_patient_name(self):
    #     try:
    #         expected = "Patient Summary"
    #         # self.click_on_link()
    #         actual = self.mouse_click_action(SearchConsultsXpath.missed_patient_name)
    #         if actual == expected:
    #             assert True
    #         else:
    #             assert False
    #     except Exception as e:
    #         allure.attach(str(e), name="review_application_exception", attachment_type=allure.attachment_type.TEXT)
    #         raise

    @allure.step("Clicking on View Pending Prescription")
    def view_pending_prescription(self):
        try:
            self.mouse_click_action(UpcomingConsultsXpath.view_pending_prescription)
        except Exception as e:
            allure.attach(str(e), name="view_pending_prescription_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Mark as Missed")
    def mark_as_missed(self):
        try:
            self.mouse_click_action(UpcomingConsultsXpath.mark_as_missed_btn)
        except Exception as e:
            allure.attach(str(e), name="click_mark_as_missed_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify given patient is NOT present")
    def patient_not_present(self):
        try:
            if self.driver.isDisplayed(UpcomingConsultsXpath.mark_as_missed_btn):
                assert False
            else:
                assert True
        except Exception as e:
            allure.attach(str(e), name="patient_not_present",
                          attachment_type=allure.attachment_type.TEXT)
            raise
