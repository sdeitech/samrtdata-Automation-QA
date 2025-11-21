from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Dispensed.Typeform.TypeformXpath import TypeformXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class TypeformPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Switching to type form frame")
    def switching_to_type_form_frame(self):
        try:
            self.switch_to_iframe(TypeformXpath.type_form_frame)
            self.wait_for_sync(5)
        except Exception as e:
            allure.attach(str(e), name="switching_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Validating age")
    def validating_age(self):
        try:
            self.mouse_click_action(TypeformXpath.yes_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="validating_age_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Which of the following describes your relationship to cannabis:This question is required.")
    def select_relation_to_cannabis(self):
        try:
            self.mouse_click_action(TypeformXpath.i_am_new_to_cannabis_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_relation_to_cannabis_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please tick the box if any of the following are true.")
    def select_box(self):
        try:
            self.mouse_click_action(TypeformXpath.select_true_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_box_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Selecting: Please select what you suffer from")
    def select_suffer(self):
        try:
            self.mouse_click_action(TypeformXpath.suffer_from_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_suffer_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please email a referral letter from your specialist")
    def select_referral_letter(self):
        try:
            self.mouse_click_action(TypeformXpath.click_to_proceed_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_referral_letter_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please select any conditions or secondary conditions you are suffering from, for which you are seeking treatment.This question is required.")
    def select_suffering_condition(self):
        try:
            self.mouse_click_action(TypeformXpath.pain_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.ok_btn)
            # self.driver.find_element(By.XPATH, TypeformXpath.pain_btn).click()
            # self.wait_and_click(TypeformXpath.pain_btn)
            # self.wait_and_click(TypeformXpath.pain_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_suffering_condition_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: What is your Medicare Number(optional): {medicare_number}")
    def enter_medicare_number(self, medicare_number):
        try:
            self.enter_text_action(medicare_number, TypeformXpath.medicare_textarea)
            # self.mouse_click_action(TypeformXpath.medicare_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_medicare_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: Individual Reference Number (optional): {reference_number}")
    def enter_reference_number(self, reference_number):
        try:
            self.wait_for_sync(2)
            self.enter_text_action(reference_number, TypeformXpath.reference_textarea)
            # self.mouse_click_action(TypeformXpath.reference_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_reference_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Where did you hear about us?")
    def select_where_did_you_hear_about_us(self):
        try:
            self.mouse_click_action(TypeformXpath.radio_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_where_did_you_hear_about_us_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Declaration: I have answered all questions truthfully/to the best of my knowledge.")
    def select_declaration(self):
        try:
            self.mouse_click_action(TypeformXpath.i_accept_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_declaration_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Switching to default frame")
    def switching_default_frame(self):
        try:
            self.switch_to_default_content()
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="switching_default_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Validating consent form with NO")
    def verify_do_not_qualify_cannabis(self):
        try:
            self.switching_to_type_form_frame()
            self.mouse_click_action(TypeformXpath.no_btn)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(TypeformXpath.do_not_qualify_cannabis_text)
            self.log.info("Actual text retrieved: " + actual)
            expected = "Sorry but to you do not qualify for medicinal cannabis."
            if expected == actual:
                assert True
            else:
                assert False
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.reset_form)
        except Exception as e:
            allure.attach(str(e), name="validating_text_do_not_qualify_cannabis", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Validating consent form and click Reset ")
    def verify_consent_form_reset_account(self):
        try:
            self.switching_to_type_form_frame()
            self.mouse_click_action(TypeformXpath.no_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.reset_form)
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.yes_btn)
            self.wait_for_sync(5)
            self.select_relation_to_cannabis()

        except Exception as e:
            allure.attach(str(e), name="validating_reset_form", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Entering details into Dispensed typeform")
    def enter_typeform_details(self, medicare_number, reference_number):
        self.switching_to_type_form_frame()
        self.validating_age()
        self.wait_for_sync(5)
        self.select_relation_to_cannabis()
        self.select_box()
        self.select_suffer()
        self.select_referral_letter()
        self.select_suffering_condition()
        self.enter_medicare_number(medicare_number)
        self.enter_reference_number(reference_number)
        self.select_where_did_you_hear_about_us()
        self.select_declaration()
        # self.switching_default_frame()


    @allure.step("Entering details into smartData2 typeform")
    def enter_smartData2_typeform_details(self, medicare_number="1231231212", reference_number="1231231212"):
        self.switching_to_type_form_frame()
        self.validating_age()
        self.wait_for_sync(5)
        self.select_relation_to_cannabis()
        self.select_box()
        self.select_suffer()
        self.select_referral_letter()
        self.select_suffering_condition()
        self.enter_medicare_number(medicare_number)
        self.enter_reference_number(reference_number)
        self.select_where_did_you_hear_about_us()
        self.select_declaration()
        # self.switching_default_frame()