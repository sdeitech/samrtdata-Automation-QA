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
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_021, smartData1-550 :To verify to create the patient by decline the forms")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number", data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "SignUp"))
    def test_signup_with_consent_form_as_no(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/InitialConsult.xlsx","SignUp")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.verify_do_not_qualify_cannabis()

        except:
            assert False
