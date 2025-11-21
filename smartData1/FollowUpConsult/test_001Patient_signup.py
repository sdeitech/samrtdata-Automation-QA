import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader


class TestSignUp(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_001: To verify to Sign up using valid data")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/FollowUpConsult.xlsx", "SignUp"))
    def test_signup_with_valid_credentials(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/FollowUpConsult.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details(medicare_number, reference_number)
            calendly_page = CalendlyPage(self.driver)
            calendly_page.calendly_book_appointment()
        except:
            assert False
