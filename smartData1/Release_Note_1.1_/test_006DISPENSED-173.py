import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from Utilities import data_reader


class TestsmartData1173(BaseTest):


    @pytest.mark.regression
    # @pytest.mark.run(order=1)
    @allure.title(
        "smartData1-173: Duplicate email entries to be restricted from portal(smartData1+smartData2)")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                                             "SignUpDuplicateEmail"))
    def test_signup_with_duplicate_email(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "dummy")
            signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm, SignUpPageXpath.duplicate_email, verify)
        except:
            assert False


