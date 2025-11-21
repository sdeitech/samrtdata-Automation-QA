import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Profile.ProfilePage import ProfilePage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader



class TestsmartData1313(BaseTest):
    @pytest.mark.smoke
    @allure.title("TC_smartData1-313_003: To verify to show the Medicare number correct or not on profile page")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "SignUp"))
    def test_signup_with_valid_credentials(self, email, firstname, lastname, dob, addr, phone, password, confirm,
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

    # @pytest.mark.smoke
    # @allure.title("Verify added 'medicare number' of smartData1-313")
    # @pytest.mark.parametrize(
    #         "medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms",
    #         data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "Upcoming_Appointment"))
    # def test_verify_medicare_number(self, medicare_number, expiry_date, reference_number,
    #                                                              ihi_number, occupation, weight, height, allergies,
    #                                                              sleep, therapies, diagnosed_year, practitioner,
    #                                                              medications, symptoms):
    #     try:
    #         login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
    #         login_page.login_into_application()
    #         search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login",
    #                                                     2, 1)
    #         search_appointment.search_consultations()
    #         search_appointment.view_profile()
    #
    #         profile = ProfilePage(self.driver)
    #         profile.verify_medicare(medicare_number)
    #         profile.verify_reference(reference_number)
    #     except:
    #         assert False