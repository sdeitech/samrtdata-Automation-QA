import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Support.SupportPage import SupportPage



class TestSupport(BaseTest):
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

    @pytest.mark.smoke
    @allure.title("TC_FAQs_10, smartData1263: To verify the Live chat feature can be accessed from the Support page.")
    def test_view_live_chat(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            sidenav.click_support()
            faq = SupportPage(self.driver)
            faq.view_live_chat()
        except:
            assert False