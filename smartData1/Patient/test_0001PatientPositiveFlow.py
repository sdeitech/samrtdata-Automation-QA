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


class TestPatientActivities(BaseTest):

    @pytest.mark.smoke
    # @pytest.mark.skip
    @pytest.mark.run(order=1)
    @allure.title("TC_SignupPatient_001, smartData1-635: To verify to Sign up using valid data")
    @pytest.mark.parametrize(
        "email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, reference_number",
        data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                        "SignUp"))
    def test_signup_with_valid_credentials(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                           medicare_number, reference_number):
        try:
            self.patient_signup_and_logout(addr, confirm, dob, "test12@yopmail.com", firstname, lastname,
                                           medicare_number, password,
                                           phone, reference_number)
        except:
            assert False


    # @pytest.mark.skip
    @pytest.mark.regression
    @pytest.mark.run(order=2)
    @allure.title("TC_SignupPatient_006, smartData1-635: To verify to create account for patient it should login to "
                  "application using Patient login")
    def test_login_after_signUp(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "SignUp")
            login_page.click_login_now()
            login_page.login_with_given_password("Disp@123")
           # login_page.logout()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title(
        "TC_smartData1-153_001: To verify patient redirect to shop website in new windows when clicking on “shop vapouriser” Button")
    def test_shop_vapouriser(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_shop_vaporiser_btn("1")
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title(
        "TC_smartData1-221_001: To verify modal is visible on clicking “online store“ from side menu")
    def test_online_store_modal_visible(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_online_store()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.verify_modal_visibility()
            dashboard.click_modal_close_btn()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title(
        "TC_smartData1-134_001: To verify Onboarding Tooltip and Welcome Modals is visible on clicking “View Information Guide” icon")
    def test_onboarding_tooltip_visible(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_tooltip_icon()
            dashboard.verify_tooltip_visibility()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title(
        "TC_smartData1-134_002: To verify Onboarding Tooltip and Welcome Modals navigation(Next and Previous Buttons) is working properly")
    def test_onboarding_tooltip_navigation(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_tooltip_icon()
            dashboard.click_next_btn()
            dashboard.click_next_btn()
            dashboard.click_next_btn()
            dashboard.click_next_btn()
            dashboard.click_previous_btn()
            dashboard.click_previous_btn()
            dashboard.click_previous_btn()
            dashboard.click_previous_btn()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=7)
    @allure.title(
        "TC_smartData1-134_003: To verify Onboarding Tooltip and Welcome Modals closes when clicked on Get Started button")
    def test_onboarding_tooltip_closes_on_get_started(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.view_tooltip()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    @allure.title(
        "TC_smartData1-134_004: To verify Onboarding Tooltip and Welcome Modals closes when clicked on outside of modal")
    def test_onboarding_tooltip_close(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_tooltip_icon()
            dashboard.click_outside_modal()
        except:
            assert False

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

    # @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    @allure.title("TC_ChangePassword_001, smartData1-563 :To verify to change with valid Password")
    def test_update_password_with_valid_data(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_navigation_bar = SideNavPage(self.driver)
            side_navigation_bar.click_profile()
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_password_link()
            profile_page.update_password("Password@12", "Disp@123", "Disp@123")
            side_navigation_bar.click_profile()
            profile_page.click_password_link()
            profile_page.update_password("Disp@123", "Password@12", "Password@12")
            profile_page.profile_update_password_text()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "Test Case ID_smartData1-513_001: To verify when Patient booked the appointment then should able to reschedule")
    @pytest.mark.parametrize(
        "email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, reference_number",
        data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                        "SignUp"))
    def test_reschedule_appointment(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                    medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details(medicare_number, reference_number)
            calendly_page = CalendlyPage(self.driver)
            calendly_page.calendly_book_appointment()
            dashboard = PatientDashboardPage(self.driver)
            ##calendly_page.refresh_page()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "Test Case ID_smartData1-513_003: To verify when Patient booked the appointment then should able to cancel")
    def test_cancel_appointment(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            calendly_page = CalendlyPage(self.driver)
            # calendly_page.calendly_book_appointment()
            calendly_page.cancel_upcomming_appointment()
            calendly_page.refresh_page()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_FAQs_07, smartData1263: To verify the FAQs are listed and is readable from the patient portal.")
    def test_view_faq(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            sidenav.click_support()
            faq = SupportPage(self.driver)
            faq.all_faqs()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_FAQs_08, smartData1263: To verify the available document can be viewed from the FAQ section.")
    def test_view_welcome_guide_pdf(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            sidenav.click_support()
            faq = SupportPage(self.driver)
            faq.view_pdf()
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_FAQs_10, smartData1263: To verify the Live chat feature can be accessed from the Support page.")
    def test_view_live_chat(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            sidenav.click_support()
            faq = SupportPage(self.driver)
            # faq.view_live_chat()
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