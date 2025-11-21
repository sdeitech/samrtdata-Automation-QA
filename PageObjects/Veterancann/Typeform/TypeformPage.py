from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import datetime
from PageObjects.smartData2.Typeform.TypeformXpath import TypeformXpath
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

    @allure.step("Validating age No")
    def validating_age_no(self):
        try:
            self.mouse_click_action(TypeformXpath.no_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="validating_age_no_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Reset Typeform")
    def reset_typeform(self):
        try:
            self.mouse_click_action(TypeformXpath.reset_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="reset_typeform_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Which of the following describes your relationship to cannabis:This question is required.")
    def select_relation_to_cannabis(self):
        try:
            self.mouse_click_action(TypeformXpath.i_use_cannabis_often)
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

    @allure.step("Selecting: If you have had a manic episode or psycosis in the past 12 months, please email a referral letter from your specialist psychiatrist to clinician@dispensed.com.au stating they approve you commencing treatment with medicinal cannabis.")
    def click_psycosis(self):
        try:
            self.mouse_click_action(TypeformXpath.psycosis)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="click_psycosis_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Are you currently, or have you been on a Coordinated Veteran Care plan in the past three months?")
    def select_coordinated_care_plan(self):
        try:
            self.mouse_click_action(TypeformXpath.care_plan)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_coordinated_care_plan_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: What is your DVA (veteran's number)This question is required.: {dva_number}")
    def enter_dva_number(self, dva_number):
        try:
            self.enter_text_action(dva_number, TypeformXpath.medicare_textarea)
            # self.mouse_click_action(TypeformXpath.medicare_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_dva_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: What is the expiry date: {expiry_date}")
    def enter_expiry_date(self, expiry_date):
        try:
            self.enter_text_action(expiry_date, TypeformXpath.expiry_date)
            # self.mouse_click_action(TypeformXpath.medicare_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_expiry_date_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Selecting: Please select the primary condition you are suffering from, for which you are seeking treatment.")
    def select_seeking_treatment(self):
        try:
            self.mouse_click_action(TypeformXpath.chronic_pain)
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.injury)
            self.wait_for_sync(2)
            self.mouse_click_action(TypeformXpath.ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_seeking_treatment_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: What DVA card type do you have?")
    def select_dva_card_type(self):
        try:
            self.mouse_click_action(TypeformXpath.dva_card)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_dva_card_type_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Throughout our lives, most of us have had pain from time to time (such as minor headaches, sprains, and toothaches). Have you had pain other than these everyday kinds of pain today?")
    def select_have_other_pain(self):
        try:
            self.mouse_click_action(TypeformXpath.other_pain_yes_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_have_other_pain_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Selecting: BPI: Please list the area in which you feel pain.")
    def select_pain_areas(self):
        try:
            # for key, value in TypeformXpath.pain_area.items():
            #     self.check_pains(key, value)
            self.mouse_click_action(TypeformXpath.ok_btn)
        except Exception as e:
            allure.attach(str(e), name="select_pain_areas_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Checking: Different types of pains and there areas: {key}")
    def check_pains(self, key, value):
        try:
            sides = {"Left": 1, "Right": 2, "Front": 3, "Back": 4}
            for keyid, valueid in sides.items():
                self.check_all_sides(keyid, value, valueid)

        except Exception as e:
            allure.attach(str(e), name="check_pain_areas_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Checking: All sides of areas: {sides}")
    def check_all_sides(self, sides, value, valueid):
        try:
            values = value+f"[{valueid}]"
            self.mouse_click_action(values)
        except Exception as e:
            allure.attach(str(e), name="check_all_sides_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step(
        "Selecting: BPI: Please rate your pain by selecting the one number that best describes your pain")
    def select_rate_your_pain(self):
        try:
            for key, value in TypeformXpath.rate_pain.items():
                self.rate_your_pain(key, value)
            self.mouse_click_action(TypeformXpath.rate_pain_ok_btn)
        except Exception as e:
            allure.attach(str(e), name="select_rate_your_pain_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Checking: rating pain level: {key}")
    def rate_your_pain(self, key, value):
        try:
            self.mouse_click_action(value)
        except Exception as e:
            allure.attach(str(e), name="check_all_sides_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("BPI: In the past 24 hours, how much relief have pain treatments or medications provided you?This question is required.")
    def select_relief_dropdown(self):
        try:
            self.mouse_click_action(TypeformXpath.bpi_24hr_dropdown)
            self.mouse_click_action(TypeformXpath.bpi_option)
        except Exception as e:
            allure.attach(str(e), name="check_all_sides_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Selecting: BPI: Click the corresponding number that describes how during the past 24 hours, pain has interfered with your (10 being the most):")
    def select_24hr_pain_number(self):
        try:
            for key, value in TypeformXpath.past_24hr_pain.items():
                self.rate_your_pain(key, value)
            self.mouse_click_action(TypeformXpath.rate_pain_ok_btn)
        except Exception as e:
            allure.attach(str(e), name="select_pain_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Selecting: C-SSRS: Please answer the following questions:")
    def select_cssr_answer(self):
        try:
            for key, value in TypeformXpath.cssrs.items():
                self.rate_your_pain(key, value)
            self.mouse_click_action(TypeformXpath.rate_pain_ok_btn)
        except Exception as e:
            allure.attach(str(e), name="select_cssr_answer_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Selecting: DASS 21: Please read each statement and click a number 0, 1, 2 or 3 which indicates how much the statement applied to you over the past week.")
    def select_dass21_answer(self):
        try:
            for key, value in TypeformXpath.dass_21.items():
                self.rate_your_pain(key, value)
            self.mouse_click_action(TypeformXpath.rate_pain_ok_btn)
        except Exception as e:
            allure.attach(str(e), name="select_dass21_answer_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Declaration: I have answered all questions truthfully/to the best of my knowledge.")
    def select_declaration(self):
        try:
            self.mouse_click_action(TypeformXpath.i_accept_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_declaration_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Declaration: I have answered all questions truthfully/to the best of my knowledge.")
    def reject_declaration(self):
        try:
            expected = "Please agree to the terms & conditions"
            self.mouse_click_action(TypeformXpath.i_dont_accept_btn)
            self.wait_for_sync(2)
            self.verify_validation_text(TypeformXpath.reject_validation, expected)
        except Exception as e:
            allure.attach(str(e), name="reject_declaration_exception", attachment_type=allure.attachment_type.TEXT)
            raise



    @allure.step("Selecting: Please select any conditions or secondary conditions you are suffering from, for which you are seeking treatment.This question is required.")
    def select_suffering_condition(self):
        try:
            self.mouse_click_action(TypeformXpath.pain_btn)
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
            # self.enter_text_action(reference_number, TypeformXpath.reference_textarea)
            self.mouse_click_action(TypeformXpath.reference_ok_btn)
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





    @allure.step("Enter firstname: {firstname}")
    def enter_firstname(self, firstname):
        try:
            current_datetime = datetime.now()

            # Format date and time into string
            date_time_string = current_datetime.strftime("%Y-%m-%d")
            self.send_text_action(firstname + date_time_string, TypeformXpath.fname)
        except Exception as e:
            allure.attach(str(e), name="enter_firstname_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter lastname: {lastname}")
    def enter_lastname(self, lastname):
        try:
            # Get current date and time
            current_datetime = datetime.now()

            # Format date and time into string
            date_time_string = current_datetime.strftime("%H:%M:%S")
            self.send_text_action(lastname + date_time_string, TypeformXpath.lname)
        except Exception as e:
            allure.attach(str(e), name="enter_lastname_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Phone number: {phone}")
    def enter_phone_number(self, phone):
        try:
            self.enter_text_action(phone, TypeformXpath.phone)
        except Exception as e:
            allure.attach(str(e), name="enter_phone_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What is your occupation?: {occupation}")
    def enter_occupation(self, occupation):
        try:
            self.enter_text_action(occupation, TypeformXpath.occupation)
        except Exception as e:
            allure.attach(str(e), name="enter_occupation_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("What was your sex at birth?")
    def select_gender(self):
        try:
            self.mouse_click_action(TypeformXpath.gender)
        except Exception as e:
            allure.attach(str(e), name="select_gender_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What is your weight?: {weight}")
    def enter_weight(self, weight):
        try:
            self.enter_text_action(weight, TypeformXpath.weight)
        except Exception as e:
            allure.attach(str(e), name="enter_weight_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What is your height?: {height}")
    def enter_height(self, height):
        try:
            self.enter_text_action(height, TypeformXpath.height)
        except Exception as e:
            allure.attach(str(e), name="enter_height_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select: Based on earlier answers, we would like to know what statement best describes you")
    def select_describes_you(self):
        try:
            self.mouse_click_action(TypeformXpath.new_to_cannabis)
        except Exception as e:
            allure.attach(str(e), name="select_describes_you_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on OK button")
    def click_ok_btn(self):
        try:
            self.mouse_click_action(TypeformXpath.ok_btn)
        except Exception as e:
            allure.attach(str(e), name="click_ok_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What conditions related to chronic injury and/or pain have been recognised and accepted by the DVA?: {conditions}")
    def enter_conditions(self, conditions):
        try:
            self.enter_text_action(conditions, TypeformXpath.conditions)
        except Exception as e:
            allure.attach(str(e), name="enter_conditions_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select: Please tell us about your sleep")
    def select_about_sleep(self):
        try:
            self.mouse_click_action(TypeformXpath.about_sleep)
        except Exception as e:
            allure.attach(str(e), name="select_about_sleep_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Enter What year were you diagnosed with your condition?: {diagnosed_year}")
    def enter_diagnosed_year(self, diagnosed_year):
        try:
            self.wait_for_sync(3)
            self.enter_text_action(diagnosed_year, TypeformXpath.diagnosed_year)
        except Exception as e:
            allure.attach(str(e), name="enter_diagnosed_year_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select: Do you have any allergies or are you sensitive to any medicine?This question is required.*")
    def select_sensitive(self):
        try:
            self.mouse_click_action(TypeformXpath.select_sensitive)
        except Exception as e:
            allure.attach(str(e), name="select_select_sensitive_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Enter What year were you diagnosed with your condition?: {describe_sensitive_from}")
    def enter_describe_sensitive_from(self, describe_sensitive_from):
        try:
            self.wait_for_sync(3)
            self.enter_text_action(describe_sensitive_from, TypeformXpath.describe_sensitive_from)
        except Exception as e:
            allure.attach(str(e), name="enter_describe_sensitive_from_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select: What method of administration would make you feel most comfortable? ")
    def select_comfortable_method(self):
        try:
            self.mouse_click_action(TypeformXpath.comfortable_method)
        except Exception as e:
            allure.attach(str(e), name="select_comfortable_method_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select: Have you previously been approved for and received medicinal cannabis treatment fully funded by the DVA?")
    def select_previously_funded(self):
        try:
            self.mouse_click_action(TypeformXpath.previously_funded)
        except Exception as e:
            allure.attach(str(e), name="select_previously_funded_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Enter What treatments or medications are you receiving for your pain?This question is required.: {pain_medication}")
    def enter_pain_medication(self, pain_medication):
        try:
            self.wait_for_sync(3)
            self.enter_text_action(pain_medication, TypeformXpath.pain_medication)
        except Exception as e:
            allure.attach(str(e), name="enter_pain_medication_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter your contact details")
    def enter_your_contact_details(self, firstname, lastname, phone):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_phone_number(phone)

    @allure.step("Entering details into smartData2 typeform")
    def enter_smartData2_typeform_details(self, dva, expiry, firstname, lastname, phone, occupation, weight, height, conditions, diagnosed_year, describe_sensitive_from, pain_medication):
        self.switching_to_type_form_frame()
        self.validating_age()
        self.wait_for_sync(2)
        self.enter_your_contact_details(firstname, lastname, phone)
        self.wait_for_sync(2)
        self.enter_occupation(occupation)
        self.wait_for_sync(2)
        self.select_gender()
        self.wait_for_sync(2)
        self.enter_weight(weight)
        self.wait_for_sync(2)
        self.enter_height(height)
        self.wait_for_sync(2)
        self.select_describes_you()
        self.wait_for_sync(2)
        self.select_relation_to_cannabis()
        self.wait_for_sync(2)
        self.select_box()
        self.wait_for_sync(2)
        self.select_suffer()
        self.wait_for_sync(2)
        self.select_referral_letter()
        self.wait_for_sync(2)
        self.click_psycosis()
        self.wait_for_sync(2)
        self.click_ok_btn()
        self.wait_for_sync(2)
        self.select_seeking_treatment()
        self.wait_for_sync(2)
        self.enter_conditions(conditions)
        self.wait_for_sync(2)
        self.select_about_sleep()
        self.wait_for_sync(2)
        self.enter_diagnosed_year(diagnosed_year)
        self.wait_for_sync(2)
        self.select_sensitive()
        self.wait_for_sync(2)
        self.enter_describe_sensitive_from(describe_sensitive_from)
        self.wait_for_sync(2)
        self.select_comfortable_method()
        self.wait_for_sync(2)
        self.select_coordinated_care_plan()
        self.wait_for_sync(2)
        self.select_dva_card_type()
        self.wait_for_sync(2)
        self.enter_dva_number(dva)
        self.wait_for_sync(2)
        self.enter_expiry_date(expiry)
        self.wait_for_sync(2)
        self.select_previously_funded()
        self.wait_for_sync(2)
        self.select_have_other_pain()
        self.wait_for_sync(2)
        self.select_pain_areas()
        self.wait_for_sync(2)
        self.select_rate_your_pain()
        self.wait_for_sync(2)
        self.select_relief_dropdown()
        self.wait_for_sync(2)
        self.select_24hr_pain_number()
        self.wait_for_sync(2)
        self.enter_pain_medication(pain_medication)
        self.wait_for_sync(2)
        self.select_dass21_answer()
        self.wait_for_sync(2)
        self.select_cssr_answer()
        self.wait_for_sync(2)
        self.select_declaration()
        self.wait_for_sync(2)

    @allure.step("Entering details into smartData2 typeform and rejecting declaration")
    def enter_smartData2_typeform_reject_declaration(self, dva, expiry, firstname, lastname, phone, occupation, weight,
                                               height, conditions, diagnosed_year, describe_sensitive_from,
                                               pain_medication):
            self.switching_to_type_form_frame()
            self.validating_age()
            self.wait_for_sync(2)
            self.enter_your_contact_details(firstname, lastname, phone)
            self.wait_for_sync(2)
            self.enter_occupation(occupation)
            self.wait_for_sync(2)
            self.select_gender()
            self.wait_for_sync(2)
            self.enter_weight(weight)
            self.wait_for_sync(2)
            self.enter_height(height)
            self.wait_for_sync(2)
            self.select_describes_you()
            self.wait_for_sync(2)
            self.select_relation_to_cannabis()
            self.wait_for_sync(2)
            self.select_box()
            self.wait_for_sync(2)
            self.select_suffer()
            self.wait_for_sync(2)
            self.select_referral_letter()
            self.wait_for_sync(2)
            self.click_psycosis()
            self.wait_for_sync(2)
            self.click_ok_btn()
            self.wait_for_sync(2)
            self.select_seeking_treatment()
            self.wait_for_sync(2)
            self.enter_conditions(conditions)
            self.wait_for_sync(2)
            self.select_about_sleep()
            self.wait_for_sync(2)
            self.enter_diagnosed_year(diagnosed_year)
            self.wait_for_sync(2)
            self.select_sensitive()
            self.wait_for_sync(2)
            self.enter_describe_sensitive_from(describe_sensitive_from)
            self.wait_for_sync(2)
            self.select_comfortable_method()
            self.wait_for_sync(2)
            self.select_coordinated_care_plan()
            self.wait_for_sync(2)
            self.select_dva_card_type()
            self.wait_for_sync(2)
            self.enter_dva_number(dva)
            self.wait_for_sync(2)
            self.enter_expiry_date(expiry)
            self.wait_for_sync(2)
            self.select_previously_funded()
            self.wait_for_sync(2)
            self.select_have_other_pain()
            self.wait_for_sync(2)
            self.select_pain_areas()
            self.wait_for_sync(2)
            self.select_rate_your_pain()
            self.wait_for_sync(2)
            self.select_relief_dropdown()
            self.wait_for_sync(2)
            self.select_24hr_pain_number()
            self.wait_for_sync(2)
            self.enter_pain_medication(pain_medication)
            self.wait_for_sync(2)
            self.select_dass21_answer()
            self.wait_for_sync(2)
            self.select_cssr_answer()
            self.wait_for_sync(2)
            self.reject_declaration()
            self.wait_for_sync(2)


        # self.select_seeking_treatment()



        # for key, value in TypeformXpath.pain_area.items():
        #     # print(f"{key}: {value}")
        #     self.select_pain_area(key,value)




        # self.select_suffering_condition()
        # self.enter_medicare_number(medicare_number)
        # self.enter_reference_number(reference_number)
        # self.select_where_did_you_hear_about_us()
        # self.select_declaration()
        # self.switching_default_frame()

