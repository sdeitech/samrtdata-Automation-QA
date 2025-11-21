from selenium.webdriver.common.by import By

from PageObjects.Dispensed.NurseDashboard.NurseDashboardXpath import NurseDashboardXpath
from SupportLibraries.base_helper import BaseHelpers
from Utilities import data_reader
import allure


class NurseDashboardPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Nurse profile")
    def click_nurse_profile(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.nurse_profile_xpath)
        except Exception as e:
            allure.attach(str(e), name="verify_text_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Searching patient appointment using email")
    def search_consultations(self, email_address):
        try:
            self.wait_for_sync(5)
            self.enter_text_action(text_value=email_address, locator_properties=NurseDashboardXpath.search_box)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    def get_email_id(self, path, sheet, row, col):
        email_address = data_reader.get_cell_data(path, sheet, row, col)
        return email_address

    @allure.step("Verify new image present for signed up patient")
    def verify_new_image_present(self):
        try:
            if self.is_element_present(NurseDashboardXpath.new_patient_image_xpath):
                assert True
            else:
                assert False, f"Expected the new Image to be present but could NOT find"
        except Exception as e:
            allure.attach(str(e), name="verify_text_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Return Treatment number of the Patient")
    def get_treatment_number(self):
        try:
            treatment_number = self.get_text_from_element(NurseDashboardXpath.treatment_number_xpath)
            return treatment_number
        except Exception as e:
            allure.attach(str(e), name="get_treatment_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Back button in Browser")
    def navigate_back(self):
        try:
            self.driver.execute_script("window.history.go(-1)")
        except Exception as e:
            allure.attach(str(e), name="Click_back_button_browser_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Nurse home page link")
    def click_nurse_home_page_link(self):
        try:
            element = self.driver.find_element(By.LINK_TEXT, "Home")
            element.click()
        except Exception as e:
            allure.attach(str(e), name="verify_click_home_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Upcoming consults link")
    def click_upcoming_consults_link(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.upcoming_consults_xpath)
        except Exception as e:
            allure.attach(str(e), name="upcoming_consults_xpath_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Consultations link")
    def click_consultations_link(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.consultations_xpath)
        except Exception as e:
            allure.attach(str(e), name="consultations_xpath_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Awaiting approval link")
    def click_awaiting_approval_link(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.awaiting_approval_number_xpath)
        except Exception as e:
            allure.attach(str(e), name="click_awaiting_approval_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Consulted Patients")
    def click_consulted_patients(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.consult_patient_xpath)
        except Exception as e:
            allure.attach(str(e), name="click_consulted_patients_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Get upcoming consults Page title")
    def verify_upcoming_consult_title(self, expected):
        try:
            actual = self.get_text_from_element(NurseDashboardXpath.upcoming_page_title_text)
            if actual == expected:
                assert True
            else:
                assert False, f"Expected was {expected} but actual was {actual}"
        except Exception as e:
            allure.attach(str(e), name="get_page_title_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Update first name")
    def update_first_name(self, somevalue):
        try:
            self.send_text_action(somevalue, NurseDashboardXpath.nurse_first_name_xpath)
        except Exception as e:
            allure.attach(str(e), name="verify_first_name_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Update last name")
    def update_last_name(self, somevalue):
        try:
            self.send_text_action(somevalue, NurseDashboardXpath.nurse_last_name_xpath)
        except Exception as e:
            allure.attach(str(e), name="verify_last_name_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Save changes button")
    def click_save_changes_button(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.save_changes_button)
        except Exception as e:
            allure.attach(str(e), name="verify_save_changes_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify profile updated success text not present")
    def verify_profile_update_success_not_present(self):
        try:
            if self.verify_element_not_present(NurseDashboardXpath.profile_update_success_xpath):
                assert True
            else:
                assert False, f"Assert failed : Expected was Success message NOT to be present"
        except Exception as e:
            allure.attach(str(e), name="getting_element_NOT_present_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify profile updated success text")
    def verify_profile_update_success_message(self):
        try:
            actual = self.get_text_from_element(NurseDashboardXpath.profile_update_success_xpath)
            expected = self.get_error_text("profile_update_success")
            if actual == expected:
                assert True
            else:
                assert False, f"Assert failed : Expected was {expected} but actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="verify_profile_update_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Patient review link and click NOT prescribed")
    def click_patient_review_button(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.review_application_btn)
        except Exception as e:
            allure.attach(str(e), name="click_mark_as_missed_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Check review link NOT present")
    def verify_review_button_not_present(self):
        try:
            self.verify_element_not_present(NurseDashboardXpath.review_application_btn)
        except Exception as e:
            allure.attach(str(e), name="click_mark_as_missed_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Mark as Missed")
    def mark_as_missed(self):
        try:
            self.mouse_click_action(NurseDashboardXpath.mark_as_missed_btn)
        except Exception as e:
            allure.attach(str(e), name="click_mark_as_missed_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("verify first name")
    def verify_first_name(self, expected):
        try:
            element = self.get_element(NurseDashboardXpath.nurse_first_name_xpath)
            actual = element.get_attribute("value")
            if expected == actual:
                assert True
            else:
                assert False, f"Not matching {expected} but actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="get_element_attribute_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify last name")
    def verify_last_name(self, expected):
        try:
            element = self.get_element(NurseDashboardXpath.nurse_last_name_xpath)
            actual = element.get_attribute("value")
            if expected == actual:
                assert True
            else:
                assert False, f"Not matching {expected} but actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="get_element_attribute_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify last name is mandatory")
    def verify_last_name_star(self):
        try:
            actual = self.get_element_text(NurseDashboardXpath.nurse_last_name_star)
            expected = "*"
            if expected == actual:
                assert True
            else:
                assert False, f"Not matching {expected} but actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="get_element_attribute_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify first name is mandatory")
    def verify_first_name_star(self):
        try:
            actual = self.get_element_text(NurseDashboardXpath.nurse_first_name_star)
            expected = "*"
            if expected == actual:
                assert True
            else:
                assert False, f"Not matching {expected} but actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="get_element_attribute_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Text")
    def verify_text(self, expected, xpath):
        try:
            actual = self.get_element_text(xpath)
            if expected.lower() == actual.lower():
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_text_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Get upcoming consults number")
    def get_upcoming_consults_number(self):
        try:
            consult_number = self.get_text_from_element(NurseDashboardXpath.upcoming_consults_number_xpath)
            self.log.info(f"Consult number is : {consult_number}")
            return consult_number

        except Exception as e:
            allure.attach(str(e), name="get_upcoming_consults_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
        raise

    @allure.step("Get missed consults number")
    def get_missed_consults_number(self):
        try:
            consult_number = self.get_text_from_element(NurseDashboardXpath.missed_consults_number_xpath)
            self.log.info(f"Missed Consult number is : {consult_number}")
            return consult_number

        except Exception as e:
            allure.attach(str(e), name="get_missed_consults_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
        raise

    @allure.step("Get Team consults number")
    def get_team_consults_number(self):
        try:
            consult_number = self.get_text_from_element(NurseDashboardXpath.team_consults_number_xpath)
            self.log.info(f"Team Consult number is : {consult_number}")
            return consult_number

        except Exception as e:
            allure.attach(str(e), name="get_missed_consults_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
        raise

    @allure.step("Verify status of the patient changed to request pathology")
    def verify_patient_status_updated(self, expected):
        patient_status = self.get_text_from_element(NurseDashboardXpath.read_patient_status)
        if expected == patient_status:
            assert True
        else:
            assert False, f"Expected was : {expected} but actual is {patient_status}"

    @allure.step("Verify status of the patient changed to Awaiting approval")
    def verify_patient_status_changed(self, expected):
        patient_status = self.get_text_from_element(NurseDashboardXpath.read_patient_awaiting_xpath)
        if expected == patient_status:
            assert True
        else:
            assert False, f"Expected was : {expected} but actual is {patient_status}"

    @allure.step("Verify status of the patient updated to prescribed and approval letter link is present")
    def verify_patient_approval_letter_present(self):
        if self.is_element_present(NurseDashboardXpath.patient_approval_letter_xpath):
            assert True
        else:
            assert False, f"Expected was Approval letter link to be present"

    @allure.step("Verify order no, status, Doctor and consultation")
    def verify_patient_nurse_row_header(self, path, sheet):
        try:
            fname = data_reader.get_cell_data(path, sheet, 2, 2)
            lname = data_reader.get_cell_data(path, sheet, 2, 3)
            self.wait_for_sync(5)
            order_id = self.get_text_from_element(NurseDashboardXpath.read_order_id)
            self.log.info(" Order Id " + order_id)
            if int(order_id) > 50:
                assert True
            else:
                assert False, f"Expected: {order_id} "

            patient_name = self.get_text_from_element(NurseDashboardXpath.read_patient_name)
            self.log.info(" Patient Name " + patient_name)
            expected = str(fname) + " " + str(lname)
            if patient_name.lower() == expected.lower():
                assert True
            else:
                assert False, f"Expected: {expected} and actual is : {patient_name}"

            patient_status = self.get_text_from_element(NurseDashboardXpath.read_patient_status)
            self.log.info(" Patient status " + patient_status)
            if patient_status == "Awaiting Action":
                assert True
            else:
                assert False, f"Expected: 'Awaiting Action' and actual is : {patient_status}"

            doctor_name = self.get_text_from_element(NurseDashboardXpath.read_doctor_name)
            self.log.info(" Doctor Name " + doctor_name)
            # if doctor_name == "V.SAU":
            #     assert True
            # else:
            #     assert False, f"Expected: V.NUR and actual is : {doctor_name}"
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise
