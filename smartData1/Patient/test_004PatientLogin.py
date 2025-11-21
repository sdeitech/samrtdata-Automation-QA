import string
import random

import allure
import pytest

from smartData1.BaseTest import BaseTest
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from PageObjects.smartData1.Profile.ProfileHomePage import ProfileHomePage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from Utilities import data_reader


class TestPatientLogin(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_Patient_Profile_002, smartData1-689 : To verify to create the new user & Update the details with "
                  "valid data in Profile.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientLogin.xlsx", "SignUp"))
    def test_update_profile(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                            medicare_number, reference_number):
        try:
            # self.patient_signup_and_logout(addr,confirm,dob,"testpatient@yopmail.com",firstname,lastname,medicare_number,password,phone,reference_number,"TestData/smartData1/PatientLogin.xlsx","SignUp")

            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)
            random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            profile_page.update_po_box(random_text)
            ph = ''.join(random.choices(string.digits, k=8))
            profile_page.update_phone_number(ph)
            profile_page.verify_success_msg()
            side_nav.click_home_page()

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title(
        "TC_Patient_Profile_003, smartData1-689 : To verify that a user cannot edit their profile with invalid data.")
    def test_update_mailing_address_with_invalid(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)
            profile_page.update_mailing_address("Invalid")
            profile_page.verify_success_msg()
            profile_page.verify_existing_mailing_address()
            side_nav.click_home_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title("TC_Patient_Profile_004, smartData1-689 : To verify that submitting with blank data for required "
                  "fields should give a warning")
    def test_update_mailing_address_empty(self):
        try:
            # self.patient_signup_and_logout(addr,confirm,dob,"testpatient@yopmail.com",firstname,lastname,medicare_number,password,phone,reference_number,"TestData/smartData1/PatientLogin.xlsx","SignUp")

            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            #login_page.navigate_to_signup_page()
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)
            profile_page.update_mailing_address(" ")
            profile_page.verify_no_success_msg()
            profile_page.verify_error_shown_mailing_address()
            side_nav.click_home_page()

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title("TC_Patient_Profile_005, smartData1-689 : To verify that a user cannot edit their profile with data "
                  "exceeding maximum character limit")
    def test_update_po_box_large_text(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=250))
            # self.patient_signup_and_logout(addr,confirm,dob,"testpatient@yopmail.com",firstname,lastname,medicare_number,password,phone,reference_number,"TestData/smartData1/PatientLogin.xlsx","SignUp")

            # login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            # login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)

            profile_page.update_po_box(random_string)
            profile_page.verify_success_msg()
            profile_page.verify_exising_po_box_data(random_string[:127])
            side_nav.click_home_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title("TC_Patient_Profile_007, smartData1-689 :To verify that a user's profile is updated after adding "
                  "valid data")
    def test_update_phone_number(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            # self.patient_signup_and_logout(addr,confirm,dob,"testpatient@yopmail.com",firstname,lastname,medicare_number,password,phone,reference_number,"TestData/smartData1/PatientLogin.xlsx","SignUp")

            # login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            # login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)
            ph = ''.join(random.choices(string.digits, k=8))
            profile_page.update_phone_number(ph)
            profile_page.verify_success_msg()
            profile_page.verify_exising_phone_number(ph)
            side_nav.click_home_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title(
        "TC_Patient_Profile_011, smartData1-689 :To verify that a user cannot edit phone number more than 32 ch")
    def test_update_phone_number_to_max(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
            # self.patient_signup_and_logout(addr,confirm,dob,"testpatient@yopmail.com",firstname,lastname,medicare_number,password,phone,reference_number,"TestData/smartData1/PatientLogin.xlsx","SignUp")

            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(2)
            profile_page = ProfileHomePage(self.driver)

            profile_page.update_phone_number(random_string)
            profile_page.verify_success_msg()
            profile_page.verify_exising_phone_number_data(random_string[:31])
            side_nav.click_home_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=7)
    @allure.title(
        "TC_Patient_Profile_015, smartData1-689 :To verify validation message given when clicking on 'save changes' button without making any changes")
    def test_no_update_and_save_changes(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(2)
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_save_change_button()
            side_nav.click_home_page()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    @allure.title(
        "TC_Patient_Profile_014, smartData1-689 :To verify that all fields are editable except Mailing Address")
    def test_fields_are_not_editable(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientLogin.xlsx", "Login")
            # login_page.navigate_to_signup_page()
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_profile()
            side_nav.wait_for_sync(5)
            profile_page = ProfileHomePage(self.driver)

            profile_page.verify_name_gender_dob_not_editable()

            # Move back to home page after testing the feature
            side_nav.click_home_page()
        except:
            assert False

    def patient_signup_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                  phone, reference_number, excelfilename, sheet_name):
        signup_page = SignUpPage(self.driver, excelfilename, sheet_name)
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        signup_page.logout()
