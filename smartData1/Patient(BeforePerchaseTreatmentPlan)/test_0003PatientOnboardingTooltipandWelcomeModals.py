import allure
import pytest
import string
import random

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.smartData1.PatientDashboard.PatientDashboardPage import PatientDashboardPage


class TestPatientActivitiesOnbordingTooltip(BaseTest):

    @pytest.mark.smoke
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

    @pytest.mark.smoke
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

    @pytest.mark.smoke
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

    @pytest.mark.smoke
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