import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.PatientDashboard.PatientDashboardPage import PatientDashboardPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage

class TestsmartData1153(BaseTest):

    @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_smartData1-153_001: To verify patient redirect to shop website in new windows when clicking on “shop vapouriser” Button")
    def test_shop_vapouriser(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_shop_vaporiser_btn("1")
        except:
            assert False

    @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_smartData1-153_002: To verify patient redirect to shop website in new windows when clicking on “shop accessories” Button")
    def test_shop_accessories(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_shop_accessories_btn("1")
        except:
            assert False

    @pytest.mark.skip
    @pytest.mark.smoke
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
        except:
            assert False

    @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "TC_smartData1-221_002: To verify modal gets disable on clicking on “close“ button from modal ")
    def test_online_store_modal_close_btn(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_online_store()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_modal_close_btn()
        except:
            assert False

    @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "TC_smartData1-221_003: To verify patient redirect to shop website in new windows when clicking on “shop vaporiser” Button from modal ")
    def test_shop_vaporiser_from_modal(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_online_store()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_shop_vaporiser_btn("2")
        except:
            assert False

    @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title(
        "TC_smartData1-221_004: To verify patient redirect to shop website in new windows when clicking on “shop accessories” Button from modal ")
    def test_shop_accessories_from_modal(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_nav = SideNavPage(self.driver)
            side_nav.click_online_store()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.click_shop_accessories_btn("2")
        except:
            assert False

    @pytest.mark.skip
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

    @pytest.mark.skip
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

    @pytest.mark.skip
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
    #@pytest.mark.skip
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