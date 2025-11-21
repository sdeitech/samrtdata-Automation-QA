import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.PatientNote.PatientNotePage import PatientNotePage
from PageObjects.smartData1.Profile.ProfilePage import ProfilePage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from PageObjects.smartData1.PatientNote.PatientNoteXpath import PatientNoteXpath



class TestNurseViewPatientProfile(BaseTest):


    @pytest.mark.smoke
    @allure.title("TC_smartData1-313_001: To verify with medicare number field is optional in patient onboard typeform")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "SignUp"))
    def test_verify_medicare_number_is_optional_in_typeform(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details("", reference_number)
        except:
            assert False


    @pytest.mark.smoke
    @allure.title("TC_smartData1-313_002: To verify with required Medicare number is field in nurse review treatment plan")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "SignUp"))
    def test_verify_medicare_number_is_required_in_patient_note_form(self, email, firstname, lastname, dob, addr,
                                                                       phone, password, confirm,
                                                                       medicare_number, reference_number):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login",
                                                            2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            update_patient_note = PatientNotePage(self.driver)
            update_patient_note.verify_medicare_number("")
        except:
            assert False


    @pytest.mark.smoke
    @allure.title("TC_smartData1-313_003: To verify to show the Medicare number correct or not on profile page")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "SignUp"))
    def test_verify_medicare_number_of_patient_profile_from_nurse_side(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details(medicare_number, reference_number)
            calendly_page = CalendlyPage(self.driver)
            calendly_page.calendly_book_appointment()
            signup_page.logout()
            signup_page.navigate_to_signup_page()
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login",
                                                    2, 1)
            search_appointment.search_consultations()
            search_appointment.view_profile()

            profile = ProfilePage(self.driver)
            profile.verify_medicare(medicare_number)
            profile.verify_reference(reference_number)
        except:
            assert False