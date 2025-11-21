import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader


class TestSignUp(BaseTest):
    # @pytest.mark.smoke
    # # @pytest.mark.run(order=1)
    # @allure.title("TC_SignupPatient_001: To verify to Sign up using valid data")
    # @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
    #                          "reference_number", data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    # def test_signup_with_valid_credentials(self, email, firstname, lastname, dob, addr, phone, password, confirm,
    #                                        medicare_number, reference_number):
    #     try:
    #         signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login")
    #         signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
    #         signup_page.set_password(password, confirm)
    #         typeform_page = TypeformPage(self.driver)
    #         typeform_page.enter_typeform_details(medicare_number, reference_number)
    #         calendly_page = CalendlyPage(self.driver)
    #         calendly_page.calendly_book_appointment()
    #     except:
    #         assert False

    @pytest.mark.regression
    # @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_002: To verify to Sign up using invalid data, DOB adding in invalid format  by typing the details")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUpInvalidDOB"))
    def test_signup_with_invalid_date_of_birth(self, email, firstname, lastname, dob, addr, phone, password, confirm, verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
            signup_page.verify_invalid(email, firstname, lastname, dob, addr, phone, password, confirm, SignUpPageXpath.invalid_dob, verify)
        except:
            assert False


    # @pytest.mark.regression
    # # @pytest.mark.run(order=1)
    # @allure.title(
    #     "TC_SignupPatient_003: To verify to Sign up using blank data")
    # @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
    #                          data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUpInvalidDOB"))
    # def test_signup_with_blank_data(self, email, firstname, lastname, dob, addr, phone, password, confirm,verify):
    #     try:
    #         signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
    #         signup_page.verify_empty_data(email, firstname, lastname, "", addr, "", password, confirm,)
    #     except:
    #         assert False
    #
    #
    # @pytest.mark.regression
    # # @pytest.mark.run(order=1)
    # @allure.title(
    #     "TC_SignupPatient_004: To verify Sign Up using duplicate email  That already with Existing Patient & other user types")
    # @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
    #                          data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
    #                                                          "SignUpDuplicateEmail"))
    # def test_signup_with_duplicate_email(self, email, firstname, lastname, dob, addr, phone, password, confirm,
    #                                            verify):
    #     try:
    #         signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
    #         signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm, SignUpPageXpath.duplicate_email, verify)
    #     except:
    #         assert False
    #
    #
    # @pytest.mark.regression
    # # @pytest.mark.run(order=1)
    # @allure.title(
    #     "TC_SignupPatient_008: To verify to Create Patient account with  new & confirm Password not matched")
    # @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
    #                          data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
    #                                                          "SignUpWrongPassword"))
    # def test_signup_with_wrong_confrim_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
    #                                            verify):
    #     try:
    #         signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
    #         signup_page.verify_invalid_password(email, firstname, lastname, dob, addr, phone, password, confirm, SignUpPageXpath.wrong_password, verify)
    #     except:
    #         assert False