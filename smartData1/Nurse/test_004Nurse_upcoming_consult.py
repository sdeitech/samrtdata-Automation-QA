import allure
import pytest

from smartData1.BaseTest import BaseTest
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.NurseDashboard.NurseDashboardPage import NurseDashboardPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from Utilities import data_reader

# Initialize with random numbers for count of consults, so when it updates in test, it does update real numbers
before_upcoming_consults_number = 25
after_upcoming_consults_number = 20
before_missed_consults_number = 25
after_missed_consults_number = 20
before_patient_status = "test"
after_patient_status = "test"
before_team_consults_number = 100
after_team_consults_number = 10


def update_consults_number(nurse_page):
    global after_upcoming_consults_number
    after_upcoming_consults_number = nurse_page.get_upcoming_consults_number()
    global after_missed_consults_number
    after_missed_consults_number = nurse_page.get_missed_consults_number()
    global after_team_consults_number
    after_team_consults_number = nurse_page.get_team_consults_number()


class TestUpcomingConsultByNurse(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.dependency(depends=['first'], scope='class')
    @pytest.mark.run(order=2)
    @allure.title("TC_Upcoming_Appointment_010, smartData1-701 :To verify the sidebar upcoming appointment counter "
                  "updates (decreases) when patient is marked as 'Patient Reviewed - Not Prescribed'.")
    def test_upcoming_appointment_decreases_after_patient_not_prescribed(self):
        try:

            nurse_page = NurseDashboardPage(self.driver)
            global before_upcoming_consults_number
            before_upcoming_consults_number = nurse_page.get_upcoming_consults_number()
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp6", 2,
                                               1)
            nurse_page.search_consultations(email_id)
            nurse_page.click_patient_review_button()
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.click_patient_reviewed_not_prescribed()
            actual = nurse_page.get_upcoming_consults_number()
            if int(before_upcoming_consults_number) - 1 == int(actual):
                assert True
            else:
                assert False, f"Expected was {before_upcoming_consults_number} but actual is {actual}"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='first', scope='class')
    @allure.title("TC_Upcoming_Appointment_011, smartData1-701 :To verify Treatment No. is updating as per the number "
                  "of successful appointment completion made by the patient.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp4"))
    def test_treatment_patient_number(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                      medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, "test1@yopmail.com", "fname", "lname",
                                               medicare_number,
                                               password, phone,
                                               reference_number, "TestData/smartData1/PatientNurse.xlsx", "SignUp4")

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp4", 2, 1)
            nurse_page.search_consultations(email_id)
            expected = nurse_page.get_treatment_number()
            if int(expected) == 0:
                assert True
            else:
                assert False, f"Expected to get the treatment number from element"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    @pytest.mark.dependency(name='approved', scope='class')
    @allure.title(
        "TC_Upcoming_Appointment_012, smartData1-701 :To verify to create the consultation it should show based on NEw & follow up consultation.")
    def test_status_changed_to_prescribed_for_follow_up_patients(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "approved_patient", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.verify_patient_status_updated("Prescribed")
            nurse_page.verify_patient_approval_letter_present()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(depends=['first'], scope='class')
    @allure.title("TC_Upcoming_Appointment_013, smartData1-701 :To verify to search using valid name & email address.")
    def test_search_using_name(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)

            first_name = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp4", 2, 2)
            nurse_page.search_consultations(first_name)
            expected = nurse_page.get_treatment_number()
            if int(expected) == 0:
                assert True
            else:
                assert False, f"Expected to get the treatment number from element"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    #  @pytest.mark.dependency(depends=['first'], scope='class')
    @allure.title("TC_Upcoming_Appointment_014, smartData1-701 :To verify to search using valid name & email address "
                  "in invalid format.")
    def test_search_using_invalid_name(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.search_consultations("SomeInvalid Name and Not exist patient")
            nurse_page.verify_review_button_not_present()
        except:
            assert False, "Expected review Button NOT to be present"

    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    #  @pytest.mark.dependency(depends=['first'], scope='class')
    @allure.title("TC_Upcoming_Appointment_015, smartData1-701 :To verify to search using capital small & adding space "
                  "before name.")
    def test_search_using_capital_small_email(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            name = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp9", 2, 3)
            nurse_page.search_consultations("  " + name.upper() + " ")
            expected = nurse_page.get_treatment_number()
            if int(expected) == 0:
                assert True
            else:
                assert False, f"Expected to get the treatment number from element"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    @pytest.mark.dependency(name='second', scope='class')
    @allure.title("TC_Upcoming_Appointment_019, smartData1-701 :To verify the appointment status changes from Awaiting "
                  "Approval to Pathology Requested when nurse requests pathology.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp9"))
    def test_status_changed_to_pathology_requested(self, email, firstname, lastname, dob, addr, phone, password,
                                                   confirm, medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, "test1@yopmail.com", "fname", "lname",
                                               medicare_number,
                                               password, phone,
                                               reference_number, "TestData/smartData1/PatientNurse.xlsx", "SignUp9")

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp9", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.click_patient_review_button()
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.click_pathology_requested()
            treatment_plan.fill_data_and_save_changes()
            nurse_page.click_nurse_home_page_link()
            nurse_page.search_consultations(email_id)
            nurse_page.verify_patient_status_updated("Pathology Requested")
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    @pytest.mark.dependency(name='approved', scope='class')
    @allure.title("TC_Upcoming_Appointment_018, smartData1-701 :To verify the appointment status changes from Awaiting "
                  "Approval to Prescribed when approver approves the treatment plan.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp5"))
    def test_status_changed_to_awaiting_approval(self, email, firstname, lastname, dob, addr, phone, password,
                                                 confirm, medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, "test1@yopmail.com", "fname", "lname",
                                               medicare_number,
                                               password, phone,
                                               reference_number, "TestData/smartData1/PatientNurse.xlsx", "SignUp5")

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp4", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.click_patient_review_button()
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.select_treatment_plan()
            nurse_page.click_nurse_home_page_link()
            nurse_page.click_consulted_patients()
            nurse_page.click_awaiting_approval_link()
            nurse_page.search_consultations(email_id)
            nurse_page.verify_patient_status_changed("Awaiting Approval")
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=7)
    @pytest.mark.dependency(name='approved', scope='class')
    @pytest.mark.parametrize(
        "email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
        "reference_number",
        data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp6"))
    @allure.title("TC_Upcoming_Appointment_017, smartData1-701 :To verify the appointment status changes from "
                  "'Awaiting Approval' to 'Consultation pending' when navigating to appointment details screen and "
                  "returning back to today's appointment list.")
    def test_status_changed_to_consultation_pending(self, email, firstname, lastname, dob, addr, phone, password,
                                                    confirm, medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, "test7@yopmail.com", "fname", "lname",
                                               medicare_number,
                                               password, phone,
                                               reference_number, "TestData/smartData1/PatientNurse.xlsx", "SignUp6")

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp6", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.click_patient_review_button()
            nurse_page.click_consultations_link()
            nurse_page.click_upcoming_consults_link()
            nurse_page.search_consultations(email_id)
            nurse_page.verify_patient_status_updated("Consultation Pending")
        except:
            assert False

    def signup_new_patient_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                      phone,
                                      reference_number, path, sheet):
        signup_page = SignUpPage(self.driver, path, sheet)
        # Incase Previous user NOT logged out
        signup_page.logout()
        signup_page.navigate_to_signup_page()
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        calendly_page.logout()
        calendly_page.navigate_to_signup_page()

    def nurse_login_update_consults_number(self):
        nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
        nurse_login.login_into_application()
        nurse_page = NurseDashboardPage(self.driver)
        global before_upcoming_consults_number
        before_upcoming_consults_number = nurse_page.get_upcoming_consults_number()
        global before_missed_consults_number
        before_missed_consults_number = nurse_page.get_missed_consults_number()
        global before_team_consults_number
        before_team_consults_number = nurse_page.get_team_consults_number()
        nurse_page.logout()
        nurse_page.navigate_to_signup_page()
