import allure
import pytest

from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from Utilities import data_reader


class TestsmartData1173(BaseTest):


    @pytest.mark.regression
    # @pytest.mark.run(order=2)
    @allure.title(
        "Testcase_smartData1-173_003: To verify add duplicate email in capital format")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                                             "SignUpDuplicateEmailCapital"))
    def test_signup_with_duplicate_email_capital_format(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "dummy")
            signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm, SignUpPageXpath.duplicate_email, verify)
        except:
            assert False

    @pytest.mark.regression
    # @pytest.mark.run(order=2)
    @allure.title(
        "Testcase_smartData1-173_004: To verify add duplicate email in small format")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                                             "SignUpDuplicateEmailSmall"))
    def test_signup_with_duplicate_email_small_format(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                         verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "dummy")
            signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm,
                                               SignUpPageXpath.duplicate_email, verify)
        except:
            assert False

    @pytest.mark.regression
    # @pytest.mark.run(order=2)
    @allure.title(
        "Testcase_smartData1-173_005: To verify add duplicate email by adding space before email")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, verify",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                                             "SignUpDuplicateEmailSpace"))
    def test_signup_with_duplicate_email_adding_space(self, email, firstname, lastname, dob, addr, phone, password,
                                                      confirm,
                                                      verify):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "dummy")
            signup_page.verify_duplicate_email(email, firstname, lastname, dob, addr, phone, password, confirm,
                                               SignUpPageXpath.duplicate_email, verify)
        except:
            assert False

