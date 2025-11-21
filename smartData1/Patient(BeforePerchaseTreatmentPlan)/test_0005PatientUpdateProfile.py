import allure
import pytest
import string
import random

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from PageObjects.smartData1.PatientDashboard.PatientDashboardPage import PatientDashboardPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Profile.ProfileHomePage import ProfileHomePage
from PageObjects.smartData1.Support.SupportPage import SupportPage


class TestPatientActivitiesUpdatePrifile(BaseTest):

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=9)
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



    def patient_signup_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                  phone, reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx",
                                        "Login")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        signup_page.logout()