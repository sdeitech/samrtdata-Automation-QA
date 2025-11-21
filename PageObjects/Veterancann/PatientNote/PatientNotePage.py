import random

from PageObjects.smartData2.PatientNote.PatientNoteXpath import PatientNoteXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class PatientNotePage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter Medicare Number: {medicare_number}")
    def enter_medicare_number(self, medicare_number):
        try:
            self.wait_for_sync(2)
            self.send_text_action(medicare_number, PatientNoteXpath.medicare_number)
        except Exception as e:
            allure.attach(str(e), name="enter_medicare_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Expiry date: {expiry_date}")
    def enter_expiry_date(self, expiry_date):
        try:
            self.wait_for_sync(2)
            self.send_text_action(expiry_date, PatientNoteXpath.expiry_date)
        except Exception as e:
            allure.attach(str(e), name="enter_expiry_date_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Reference Number: {reference_number}")
    def enter_reference_number(self, reference_number):
        try:
            self.wait_for_sync(2)
            self.send_text_action(reference_number, PatientNoteXpath.reference_number)
        except Exception as e:
            allure.attach(str(e), name="enter_reference_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Enter IHI Number: {ihi_number}")
    def enter_ihi_number(self, ihi_number):
        try:
            self.wait_for_sync(2)
            self.send_text_action(ihi_number, PatientNoteXpath.ihi_number)
        except Exception as e:
            allure.attach(str(e), name="enter_ihi_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What's your occupation?: {occupation}")
    def enter_occupation(self, occupation):
        try:
            self.wait_for_sync(2)
            self.send_text_action(occupation, PatientNoteXpath.occupation)
        except Exception as e:
            allure.attach(str(e), name="enter_occupation_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What's your weight: {weight}")
    def enter_weight(self, weight):
        try:
            self.wait_for_sync(2)
            self.send_text_action(weight, PatientNoteXpath.weight)
        except Exception as e:
            allure.attach(str(e), name="enter_weight_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What's your height: {height}")
    def enter_height(self, height):
        try:
            self.wait_for_sync(2)
            self.send_text_action(height, PatientNoteXpath.height)
        except Exception as e:
            allure.attach(str(e), name="enter_height_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Are you a")
    def select_are_you_a(self):
        try:
            self.wait_for_sync(2)
            self.toggle_checkbox(PatientNoteXpath.smoker)
            self.wait_for_sync(2)
            self.toggle_checkbox(PatientNoteXpath.drinker)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_are_you_a_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Rate the patients symptoms (out of 10): {option_value}")
    def select_patient_symptoms(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), PatientNoteXpath.patient_symptom_select)
        except Exception as e:
            allure.attach(str(e), name="select_patient_symptoms_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Allergies or Drug Sensitivities: {allergies}")
    def enter_allergies(self, allergies):
        try:
            self.wait_for_sync(2)
            self.send_text_action(allergies, PatientNoteXpath.allergies)
        except Exception as e:
            allure.attach(str(e), name="enter_allergies_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Describe the patients Sleep: {sleep}")
    def describe_sleep(self, sleep):
        try:
            self.wait_for_sync(2)
            self.send_text_action(sleep, PatientNoteXpath.sleep)
        except Exception as e:
            allure.attach(str(e), name="describe_sleep_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("What Alternative Therapies has the patient tried: {therapies}")
    def enter_therapies(self, therapies):
        try:
            self.wait_for_sync(2)
            self.send_text_action(therapies, PatientNoteXpath.therapies)
        except Exception as e:
            allure.attach(str(e), name="enter_therapies_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Year Diagnosed: {diagnosed_year}")
    def enter_year_diagnosed(self, diagnosed_year):
        try:
            self.wait_for_sync(2)
            self.send_text_action(diagnosed_year, PatientNoteXpath.year_of_diagnosed)
        except Exception as e:
            allure.attach(str(e), name="enter_year_diagnosed_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Previous practice or general practitioner: {practitioner}")
    def enter_previous_practitioner(self, practitioner):
        try:
            self.wait_for_sync(2)
            self.send_text_action(practitioner, PatientNoteXpath.previous_practitioner)
        except Exception as e:
            allure.attach(str(e), name="enter_previous_practitioner_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter What is the name of the medication/s, minerals or supplements you have previously tried and currently taking?: {medications}")
    def enter_previous_medications(self, medications):
        try:
            self.wait_for_sync(2)
            self.send_text_action(medications, PatientNoteXpath.medications)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_previous_medications_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Describe the patients symptoms: {symptoms}")
    def describe_symptoms(self, symptoms):
        try:
            self.wait_for_sync(2)
            self.send_text_action(symptoms, PatientNoteXpath.symptoms)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="describe_symptoms_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    # below options are for smartData2

    @allure.step("Enter The patient has presented with symptoms of chronic pain with pain detailed as follows: {chronic_pain}")
    def chronic_pain_symptoms(self, chronic_pain):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.chronic_pain)
            self.send_text_action(chronic_pain, PatientNoteXpath.chronic_pain)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="chronic_pain_symptoms_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "List the medical condition(s) being treated with medical cannabis: {medical_condition}")
    def enter_medical_condition(self, medical_condition):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.medical_condition)
            self.send_text_action(medical_condition, PatientNoteXpath.medical_condition)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_medical_condition_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Select Has DVA approved funding for this client via a previous Tier 2 application for medicinal cannabis?")
    def select_funding_approved(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.dva_funding_1)
            self.mouse_click_action(PatientNoteXpath.dva_funding_1)
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.dva_funding_2)
            self.mouse_click_action(PatientNoteXpath.dva_funding_2)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_funding_approved_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Please list attempted treatment(s) and their outcomes: {attempted_treatments}")
    def enter_attempted_treatments(self, attempted_treatments):
        try:
            self.wait_for_sync(2)
            self.send_text_action(attempted_treatments, PatientNoteXpath.attempted_treatments)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_attempted_treatments_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Please specify the reason(s) for re-application: {reapplication_reason}")
    def enter_reapplication_reason(self, reapplication_reason):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.reapplication_check_1)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.reapplication_check_2)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.reapplication_check_3)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.reapplication_check_4)
            self.wait_for_sync(2)
            self.send_text_action(reapplication_reason, PatientNoteXpath.reapplication_reason)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_reapplication_reason_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Please report on the outcomes of this therapy including objective treatment results: {therapy_outcomes}")
    def enter_therapy_outcomes(self, therapy_outcomes):
        try:
            self.wait_for_sync(2)
            self.send_text_action(therapy_outcomes, PatientNoteXpath.therapy_outcomes)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_therapy_outcomes_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step(
        "Please report on the ongoing monitoring of the patient's mental health issues: {mental_health_monitoring}")
    def enter_mental_health_monitoring(self, mental_health_monitoring):
        try:
            self.wait_for_sync(2)
            self.send_text_action(mental_health_monitoring, PatientNoteXpath.mental_health_monitoring)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_mental_health_monitoring_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise
    @allure.step("Click on Update Button")
    def clicking_update_btn(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.update_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.update_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_update_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Save Button")
    def clicking_save_btn(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.save_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.save_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_save_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Update Treatment Plan Button")
    def clicking_update_plan_btn(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.update_treatment_plan_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.update_treatment_plan_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_update_plan_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Next Button")
    def clicking_next_btn(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(PatientNoteXpath.next_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(PatientNoteXpath.next_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_next_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise




    @allure.step("Saving/Updating Patient Notes with valid data")
    def create_patient_notes_with_valid_data(self, medicare_number, expiry_date, reference_number, ihi_number, occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms):
        self.enter_medicare_number(medicare_number)
        self.enter_expiry_date(expiry_date)
        self.enter_reference_number(reference_number)
        self.enter_ihi_number(ihi_number)
        self.enter_occupation(occupation)
        self.enter_weight(weight)
        self.enter_height(height)
        self.select_are_you_a()
        self.select_patient_symptoms(self.generate_random_number())
        self.enter_allergies(allergies)
        self.describe_sleep(sleep)
        self.enter_therapies(therapies)
        self.enter_year_diagnosed(diagnosed_year)
        # self.enter_previous_practitioner(practitioner)
        self.enter_previous_medications(medications)
        self.describe_symptoms(symptoms)
        self.clicking_update_btn()

    @allure.step("Saving/Updating Patient Notes with valid data")
    def create_veteran_patient_notes_with_valid_data(self, medicare_number, expiry_date, reference_number, ihi_number,
                                             occupation, weight, height, allergies, sleep, therapies, diagnosed_year,
                                             practitioner, medications, symptoms, chronic_pain, medical_condition, attempted_treatments, reapplication_reason, therapy_outcomes, mental_health_monitoring):
        # self.enter_medicare_number(medicare_number)
        # self.enter_expiry_date(expiry_date)
        # self.enter_reference_number(reference_number)
        # self.enter_ihi_number(ihi_number)
        # self.enter_occupation(occupation)
        # self.enter_weight(weight)
        # self.enter_height(height)
        # self.select_are_you_a()
        # self.select_patient_symptoms(self.generate_random_number())
        # self.enter_allergies(allergies)
        # self.describe_sleep(sleep)
        # self.enter_therapies(therapies)
        # self.enter_year_diagnosed(diagnosed_year)
        # self.enter_previous_practitioner(practitioner)
        # self.enter_previous_medications(medications)
        # self.describe_symptoms(symptoms)
        self.chronic_pain_symptoms(chronic_pain)
        self.enter_medical_condition(medical_condition)
        self.select_funding_approved()
        self.enter_attempted_treatments(attempted_treatments)
        self.enter_reapplication_reason(reapplication_reason)
        self.enter_therapy_outcomes(therapy_outcomes)
        self.enter_mental_health_monitoring(mental_health_monitoring)
        self.clicking_save_btn()

    @allure.step("Update Treatment Plan")
    def update_treatment_plan(self, expiry_date, reference_number):
        self.clicking_update_plan_btn()
        self.enter_expiry_date(expiry_date)
        self.enter_reference_number(reference_number)
        self.clicking_next_btn()


    def generate_random_number(self):
        return random.randint(1, 10)
