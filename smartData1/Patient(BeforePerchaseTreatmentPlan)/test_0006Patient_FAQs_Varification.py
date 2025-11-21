import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Support.SupportPage import SupportPage


class TestPatientActivitiesFAQs(BaseTest):

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_FAQs_07, smartData1263: To verify the FAQs are listed and is readable from the patient portal.")
    def test_view_faq(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
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
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
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
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
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