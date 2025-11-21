import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
import logging


class TestSignUp(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title("TC_SignupPatient_024, smartData1-550 :To verify to create the patient account & once we click on No then should able to reset the form & create the account")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_consent_form_no_reset_form(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.verify_consent_form_reset_account()

        except:
            assert False



