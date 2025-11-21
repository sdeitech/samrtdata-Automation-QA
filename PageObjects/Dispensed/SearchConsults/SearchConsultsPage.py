from PageObjects.Dispensed.SearchConsults.SearchConsultsXpath import SearchConsultsXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader


class SearchConsultsPage(BaseHelpers):
    def __init__(self, driver, path, sheet, row, col):
        super().__init__(driver)
        self.email_address = data_reader.get_cell_data(path, sheet, row, col)
        self.fname = data_reader.get_cell_data(path, sheet, 2, 2)
        self.lname = data_reader.get_cell_data(path, sheet, 2, 3)

    @allure.step("Read Upcoming consults number")
    def upcoming_consults_number(self):
        try:
            return self.get_text_from_element(SearchConsultsXpath.read_missed_consults_number)
        except Exception as e:
            allure.attach(str(e), name="get_text_upcoming_consults_number", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Read missed consults number")
    def missed_consults_number(self):
        try:
            return self.get_text_from_element(SearchConsultsXpath.read_missed_consults_number)
        except Exception as e:
            allure.attach(str(e), name="get_text_upcoming_consults_number", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Return Patient status")
    def get_patient_status(self):
        try:
            return self.get_text_from_element(SearchConsultsXpath.patient_status)
        except Exception as e:
            allure.attach(str(e), name="get_text_upcoming_consults_number", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Searching patient appointment using email")
    def search_consultations(self):
        try:
            self.mouse_click_action(SearchConsultsXpath.SearchBTN)
            self.enter_text_action(self.email_address, SearchConsultsXpath.search_box)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Searched patient profile using email NOT to be present")
    def patient_profile_not_present(self):
        try:
            self.verify_element_not_present(self.email_address, SearchConsultsXpath.view_pending_prescription)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify treatment plan details")
    def verify_treatment_plan_details(self):
        try:
            self.wait_for_sync(5)
            list_treatment_plan = ["Plan: Indica-and-Sativa-Flower", "5 unit/s of Balance Oil - 30ml",
                                   "7 unit/s of Hybrid 50:50 Vape Cartridge", "30 grams of Hybrid Flower",
                                   "5 unit/s of Indica Vape Cartridge", "30 grams of Indica Flower THC: 21-28%",
                                   "20 grams of Sativa Flower THC: 21-28%", "5 unit/s of Sativa Vape Cartridge",
                                   "6 unit/s of CBD Oil - 30ml"]
            for index, items in enumerate(list_treatment_plan):
                actual_text = self.get_text_from_element(
                    SearchConsultsXpath.read_treatment_data + "[" + str(index+1) + "]")
                self.log.info("Actual treamtment plan is " + actual_text)
                if actual_text == items:
                    assert True
                else:
                    assert False

        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify order no, status, Doctor and consultation")
    def verify_patient_nurse_row_header(self):
        try:
            self.wait_for_sync(5)
            order_id = self.get_text_from_element(SearchConsultsXpath.read_order_id)
            self.log.info(" Order Id " + order_id)
            if int(order_id) > 50:
                assert True
            else:
                assert False,  f"Expected: {order_id} "

            patient_name = self.get_text_from_element(SearchConsultsXpath.read_patient_name)
            self.log.info(" Patient Name " + patient_name)
            expected = str(self.fname) + " " + str(self.lname)
            if patient_name.lower() == expected.lower():
                assert True
            else:
                assert False, f"Expected: {expected} and actual is : {patient_name}"

            patient_status = self.get_text_from_element(SearchConsultsXpath.read_patient_status)
            self.log.info(" Patient status " + patient_status)
            if patient_status == "Awaiting Action":
                assert True
            else:
                assert False,  f"Expected: 'Awaiting Approval' and actual is : {patient_status}"

            doctor_name = self.get_text_from_element(SearchConsultsXpath.read_doctor_name)
            self.log.info(" Doctor Name " + doctor_name)
            if doctor_name == "V.NUR":
                assert True
            else:
                assert False, f"Expected: V.NUR and actual is : {doctor_name}"
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
            self.driver.click(patient_link)
            # self.mouse_click_action(patient_link, locator_type="link", max_time_out=5)

            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Review Application button")
    def review_application(self):
        try:
            self.mouse_click_action(SearchConsultsXpath.review_application_btn)
        except Exception as e:
            allure.attach(str(e), name="review_application_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify the Patient summary text present")
    def verify_patient_summary_text_present(self):
        try:
            expected = "Patient Summary"
            actual = self.get_text_from_element(SearchConsultsXpath.patient_summary_text)
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
            actual = self.get_text_from_element(SearchConsultsXpath.patient_summary_text)
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
            self.mouse_click_action(SearchConsultsXpath.view_pending_prescription)
        except Exception as e:
            allure.attach(str(e), name="view_pending_prescription_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Mark as Missed")
    def mark_as_missed(self):
        try:
            self.mouse_click_action(SearchConsultsXpath.mark_as_missed_btn)
        except Exception as e:
            allure.attach(str(e), name="click_mark_as_missed_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify given patient is NOT present")
    def patient_not_present(self):
        try:
            if self.driver.isDisplayed(SearchConsultsXpath.mark_as_missed_btn):
                assert False
            else:
                assert True
        except Exception as e:
            allure.attach(str(e), name="patient_not_present",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Profile name")
    def view_profile(self):
        try:
            self.mouse_click_action(SearchConsultsXpath.view_profile)
        except Exception as e:
            allure.attach(str(e), name="view_profile_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify navigation is present on not")
    def verify_navigation_dropdown(self):
        try:
            self.get_element(SearchConsultsXpath.naviagtion_drpdwn)
        except Exception as e:
            allure.attach(str(e), name="verify_navigation_dropdown_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise
