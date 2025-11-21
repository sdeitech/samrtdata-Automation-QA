import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.DropdownNavigation.DropdownNavigationPage import DropdownNavigationPage
from PageObjects.smartData1.DropdownNavigation.DropdownNavigationXpath import DropdownNavigationXpath
from Utilities import data_reader


class TestApproverDropdownNavigation(BaseTest):

    @pytest.mark.smoke
    @allure.title("TC_smartData1-307_001: To verify approver name in navigation menu")
    @pytest.mark.parametrize("approver, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1647"))
    def test_verify_dropdown_approver_navigation(self, approver, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.verify_name(approver, DropdownNavigationXpath.drpdwn_name)
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-307_002: To verify navigation menu is working")
    def test_verify_approver_navigation_is_working(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.verify_navigation_dropdown()
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-307_003: To verify on clicking “profile“ from navigation menu user is redirected to profile page")
    @pytest.mark.parametrize("approver, profile, password, logout", data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1647"))
    def test_verify_approver_navigation_profile_menu(self, approver, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_profile_menu()
            navigation.verify_name(profile, DropdownNavigationXpath.verify_profile)
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-307_004: To verify on clicking “password“ from navigation menu user is redirected to change password page")
    @pytest.mark.parametrize("approver, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1647"))
    def test_verify_approver_navigation_password_menu(self, approver, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_password_menu()
            navigation.verify_name(password, DropdownNavigationXpath.verify_password)
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-307_005: To verify user is logged out from the application on clicking “logout” from navigation menu ")
    @pytest.mark.parametrize("approver, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1647"))
    def test_verify_approver_navigation_logout(self, approver, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_logout()
            navigation.verify_name(logout, DropdownNavigationXpath.verify_logout)
        except:
            assert False
