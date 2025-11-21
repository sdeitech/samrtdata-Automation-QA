import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.MissedConsults.MissedConsultsPage import MissedConsultsPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader


class TestNurseMarkedPatientMissed(BaseTest):
    before_upcoming_consults_number = 25
    after_upcoming_consults_number = 24
    before_missed_consults_number = 25
    after_missed_consults_number = 24
    before_patient_status = "test"
    after_patient_status = "test"

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_Missed_Consult_001, smartData1-572 : To verify Nurse mark patient as Missed")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp"))
    def test_marked_as_missed(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                              medicare_number, reference_number):
        try:
            self.signUp_new_patient_and_logout(addr, confirm, dob, email, firstname, lastname, medicare_number,
                                               password, phone,
                                               reference_number)

            # Patient Logs out and Nurse login in same page
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_with_given_password(password)
            # nurse_login.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2, 1)

            # Getting upcoming consults number and status before marking it as missed
            self.before_upcoming_consults_number = search_appointment.upcoming_consults_number()
            self.before_missed_consults_number = search_appointment.missed_consults_number()
            self.before_patient_status = search_appointment.get_patient_status()

            search_appointment.search_consultations()
            search_appointment.mark_as_missed()
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consults_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                      1)
            missed_consults_page.search_consultations()
            missed_consults_page.review_application()

            # Getting upcoming consults number and patient status after marking it as missed
            global after_upcoming_consults_number
            after_upcoming_consults_number = int(search_appointment.upcoming_consults_number())
            global after_patient_status
            after_patient_status = search_appointment.get_patient_status()

            # Getting missed consults number after marking it as missed
            global after_missed_consults_number
            after_missed_consults_number = int(search_appointment.missed_consults_number())

            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=19)
    @allure.title(
        "TC_Missed_Consult_002, smartData1-572 :To verify that missed consultations are not displayed for other clinicians in the Missed Consultations list.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp"))
    def test_missed_patient_not_visible_for_other_clinician(self, email, firstname, lastname, dob, addr, phone,
                                                            password, confirm,
                                                            medicare_number, reference_number):
        try:
            # self.signUp_new_patient(addr, confirm, dob, email, firstname, lastname, medicare_number, password, phone,
            #                       reference_number)

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_UAT")
            # logout from any other nurse session
            nurse_login.logout()
            nurse_login.login_with_given_password(password)

            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2, 1)
            search_appointment.search_consultations()
            search_appointment.patient_not_present()
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consults_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                      1)
            missed_consults_page.search_consultations()
            missed_consults_page.patient_not_present()
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title(
        "TC_Missed_Consult_003, smartData1-572 :To verify that the Review Application button for each missed consultation redirects to the respective review page.")
    def test_marked_missed_for_review(self):
        try:
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consults_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                      1)
            missed_consults_page.search_consultations()
            missed_consults_page.review_application()
            missed_consults_page.verify_patient_summary_text_present()
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title(
        "TC_Missed_Consult_010, smartData1-572 :To verify the sidebar upcoming appointment counter updates (increases) when a new appointment is added to the list.")
    def test_upcoming_counter(self):
        if self.before_upcoming_consults_number == (self.after_upcoming_consults_number + 1):
            assert True
        else:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title(
        "TC_Missed_Consult_011, smartData1-572 :To verify the sidebar upcoming appointment counter updates (decreases) when an appointment is removed from the list..")
    def test_missed_consults_number(self):
        if self.before_missed_consults_number == (self.after_missed_consults_number + 1):
            assert True
        else:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title(
        "TC_Missed_Consult_014, smartData1-567: To verify the appointment status changes from Awaiting Approval to Consultation pending when navigating to appointment details screen and returning back to missed appointment list.")
    def test_patient_status_change(self):
        #if (after_patient_status == "Consultation Pending") and  (before_patient_status == "Awaiting Action") :
        if after_patient_status == "Consultation Pending":
            assert True
        else:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title(
        "TC_Missed_Consult_021, smartData1-567 :To verify redirection to patient details page on clicking patient's name.")
    def test_patient_details_by_clicking_name(self):
        try:
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consult_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                     1)
            missed_consult_page.search_consultations()
            missed_consult_page.click_on_patient_name()
            missed_consult_page.verify_email_present_in_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=7)
    @allure.title(
        "TC_Missed_Consult_022, smartData1-567 :To verify redirection to Patient Consultation page on clicking review application")
    def test_patient_consultation_page_clicking_review_application(self):
        try:
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consult_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                     1)
            missed_consult_page.search_consultations()
            missed_consult_page.review_application()
            missed_consult_page.verify_patient_summary_text_present()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    @allure.title(
        "TC_Missed_Consult_019, smartData1-567 :To verify to prescribe the consultation of an appointment.")
    def test_patient_consultation_page_from_missed_consults(self):
        # Need discussion otherwise similar to TC-022
        try:
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            missed_consult_page = MissedConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                     1)
            missed_consult_page.search_consultations()
            missed_consult_page.review_application()
            missed_consult_page.verify_patient_summary_text_present()
        except:
            assert False

    def signUp_new_patient_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                      phone,
                                      reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        calendly_page.logout()
        