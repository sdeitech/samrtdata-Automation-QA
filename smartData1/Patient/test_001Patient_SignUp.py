import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader


class TestSignUp(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_001, smartData1-635: To verify to Sign up using valid data")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_valid_credentials(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            self.patient_signup_and_logout(addr, confirm, dob, "test12@yopmail.com", firstname, lastname,
                                           medicare_number, password,
                                           phone, reference_number)
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.depends(on=['test_signup_with_valid_credentials'])
    @pytest.mark.run(order=2)
    @allure.title("TC_SignupPatient_002, smartData1-635: To verify to Sign up using invalid data, DOB adding in "
                  "invalid format  by typing the details")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpInvalidDOB"))
    def test_signup_with_invalid_date_of_birth(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
            signup_page.navigate_to_signup_page()
            signup_page.verify_invalid(email, firstname, lastname, dob, addr, phone, password, confirm,
                                       SignUpPageXpath.invalid_dob, "Must be at least 18 years old to register.")
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=3)
    @pytest.mark.depends(on=['test_signup_with_valid_credentials'])
    @allure.title("TC_SignupPatient_003, smartData1-635: To verify to Sign up using blank data")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpInvalidDOB"))
    def test_signup_with_blank_data(self, email, firstname, lastname, dob, addr, phone, password, confirm, verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "dummy")
            signup_page.navigate_to_signup_page()
            signup_page.verify_empty_data(email, firstname, lastname, "", addr, " ", password, confirm,
                                          SignUpPageXpath.empty_phone_number, "Phone number cannot be empty")
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=4)
    @pytest.mark.depends(on=['test_signup_with_valid_credentials'])
    @allure.title(
        "TC_SignupPatient_004, smartData1-635 :To verify Sign Up using duplicate email  That already with Existing "
        "Patient & other user types")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpDuplicateEmail"))
    def test_signup_with_duplicate_email(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                         verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpDuplicateEmail")
            signup_page.navigate_to_signup_page()
            signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm,
                                               SignUpPageXpath.duplicate_email,
                                               "User already exists with this email id.")
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=8)
    @pytest.mark.depends(on=['test_signup_with_valid_credentials'])
    @allure.title(
        "TC_SignupPatient_008: To verify to Create Patient account with  new & confirm Password not matched")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpWrongPassword"))
    def test_signup_with_wrong_confrim_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                                verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpWrongPassword")
            signup_page.navigate_to_signup_page()
            signup_page.verify_invalid_password("test3@yopmail.com", firstname, lastname, dob, addr, phone, password,
                                                confirm + "NotMatching", SignUpPageXpath.wrong_password, verify)
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=6)
    @allure.title("TC_SignupPatient_006, smartData1-635: To verify to create account for patient it should login to "
                  "application using Patient login")
    def test_login_after_signUp(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            login_page.click_login_now()
            login_page.login_with_given_password("Disp@123")
            login_page.logout()
        except:
            assert False

    @pytest.mark.regression
    @pytest.mark.run(order=7)
    @allure.title("TC_SignupPatient_007, smartData1-635: To verify to Create Patient account with valid password")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpWrongPassword"))
    def test_patient_signUp(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                            verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpWrongPassword")
            signup_page.navigate_to_signup_page()
            signup_page.verify_invalid_password("test1@yopmail.com", firstname, lastname, dob, addr, phone, "  Disp@ ",
                                                "  Disp@ ", SignUpPageXpath.wrong_password,
                                                "The password must contain at least 1 digit, 1 uppercase letter, 1 lowercase letter, and 1 symbol.")

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    @allure.title("TC_SignupPatient_009, smartData1-635: To verify to Create Patient account with with invalid password")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpWrongPassword"))
    def test_signup_with_invalid_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                          verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpWrongPassword")
            signup_page.navigate_to_signup_page()
            signup_page.verify_invalid_password("test2@yopmail.com", firstname, lastname, dob, addr, phone, "Password",
                                                "Password", SignUpPageXpath.wrong_password,
                                                "The password must contain at least 1 digit, 1 uppercase letter, 1 lowercase letter, and 1 symbol.")
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    @allure.title("TC_SignupPatient_010, smartData1-635: To verify to Create Patient account with with blank password")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx",
                                                             "SignUpWrongPassword"))
    def test_signup_with_blank_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                        verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpWrongPassword")
            signup_page.navigate_to_signup_page()
            signup_page.verify_invalid_password(email, firstname, lastname, dob, addr, phone, "",
                                                " ", SignUpPageXpath.wrong_password,
                                                "This password is too short. It must contain at least 8 characters.")
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=11)
    @allure.title("TC_SignupPatient_011, smartData1-635: To verify to Create Patient account with by adding space in "
                  "password.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_space_in_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            self.patient_signup_and_logout(addr, " Disp@ 123 ", dob, "test123@yopmail.com", firstname, lastname,
                                           medicare_number, " Disp@ 123 ",
                                           phone, reference_number)
        except:
            assert False

    def patient_signup_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                  phone, reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        signup_page.logout()
