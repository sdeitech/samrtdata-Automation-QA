import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from Utilities.age_calculator import Calculate_Year


class TestPatientSignUp(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_012, smartData1-650: To verify to create Patient  With all condition in password")
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

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title(
        "TC_SignupPatient_013, smartData1-650 :To verify to create Patient With less condition in Password as per validation message")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_less_condition_password(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                                 medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_new_account("test-13@yopmail.com", firstname, lastname, dob, addr, phone)
            signup_page.password_condition_not_met("noconditionpassword", "noconditionpassword")

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title(
        "TC_SignupPatient_014, smartData1-650 :To verify to create the user then email should duplicate email in small/capital format when adding duplicate email")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_duplicate_email_exists(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                                medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_new_account_with_email_already_exists()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title(
        "TC_SignupPatient_016, smartData1-650 :To verify to create the user then  Password should  be case sensetive  in Password  & new Password")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_password_case_sensitive(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                                 medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_new_account("test16@yopmail.com", firstname, lastname, dob, addr, phone)
            signup_page.password_wont_match("Disp@123", "disp@123")
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title(
        "TC_SignupPatient_018, smartData1-650 :To verify to Create the Patient with less that 18 years with exact 18 year old")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_exact_18_years(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                   medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_account_with_18_years("test8@yopmail.com", firstname, lastname,
                                                     Calculate_Year.get_date_before_num_years(self, 18, 0))

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title(
        "TC_SignupPatient_019, smartData1-650 :To  verify to Create the Patient with less that 18 years with exact 18+1 year old")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_18_plus_one_year(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                     medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_account_with_18_years("test19@yopmail.com", firstname, lastname,
                                                     Calculate_Year.get_date_before_num_years(self, 18, 1))
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title(
        "TC_SignupPatient_020, smartData1-650 :To verify to Create the Patient with less that 18 years with exact 18-1day year old")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_18_minus_one_year(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                      medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.navigate_to_signup_page()
            signup_page.create_account_with_less_than_18("test20@yopmail.com", firstname, lastname,
                                                         Calculate_Year.get_date_before_num_years(self, 18, -1))
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
