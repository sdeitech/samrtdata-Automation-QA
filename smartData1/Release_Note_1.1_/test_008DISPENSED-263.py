import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.Support.SupportPage import SupportPage



class TestsmartData1263(BaseTest):
    @pytest.mark.smoke
    @allure.title("smartData1-263: Patient Portal: Support/Support, open Support section")
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
    @allure.title("smartData1-263: Verify Welcome Guide PDF file in support section")
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
    @allure.title("smartData1-263: Verify LIVE CHAT from support section")
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