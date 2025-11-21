import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from Utilities.age_calculator import Calculate_Year


class TestPatientSignsUp(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_021, smartData1-651 :To verify to create the patient by decline the forms")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUpDummy"))
    def test_signup_with_consent_form_as_no(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                            medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpDummy")
            signup_page.navigate_to_signup_page()
            signup_page.create_new_account("test21@yopmail.com", "fname", "lname", dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.verify_do_not_qualify_cannabis()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title(
        "TC_SignupPatient_024, smartData1-651 :To verify to create the patient account & once we click on No then "
        "should able to reset the form & create the account")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUpDummy"))
    def test_signup_consent_form_no_reset_form(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpDummy")
            signup_page.navigate_to_signup_page()
            signup_page.create_new_account("test024@yopmail.com", "fname", "lname", dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.verify_consent_form_reset_account()

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title(
        "TC_SignupPatient_022, smartData1-651 :To verify to create the Patient In long format")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUpDummy"))
    def test_signup_more_than_256_chars(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                        medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUpDummy")
            signup_page.navigate_to_signup_page()
            signup_page.verify_no_errors_shown_for_large_email(dob)
            signup_page.verify_errors_shown_for_large_email_fname_lname(addr, phone, password, confirm)
        except:
            assert False
