import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from PageObjects.smartData1.PatientDashboard.PatientDashboardPage import PatientDashboardPage


class TestPatientActivitiesRescheduleAndCancel(BaseTest):

    @pytest.mark.smoke
    @allure.title(
        "Test Case ID_smartData1-513_001: To verify when Patient booked the appointment then should able to reschedule")
    @pytest.mark.parametrize(
        "email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, reference_number",
        data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                        "SignUp"))
    def test_reschedule_appointment(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                    medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details(medicare_number, reference_number)
            calendly_page = CalendlyPage(self.driver)
            calendly_page.calendly_book_appointment()
            dashboard = PatientDashboardPage(self.driver)
            ##calendly_page.refresh_page()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "Test Case ID_smartData1-513_003: To verify when Patient booked the appointment then should able to cancel")
    def test_cancel_appointment(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            calendly_page = CalendlyPage(self.driver)
            # calendly_page.calendly_book_appointment()
            calendly_page.cancel_upcomming_appointment()
            calendly_page.refresh_page()
        except:
            assert False

    def patient_signup_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                  phone, reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx",
                                        "Login")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        signup_page.logout()