import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.DropdownNavigation.DropdownNavigationPage import DropdownNavigationPage
from PageObjects.smartData1.DropdownNavigation.DropdownNavigationXpath import DropdownNavigationXpath
from Utilities import data_reader


class TestNurseDropdownNavigation(BaseTest):


    @pytest.mark.smoke
    @allure.title("TC_smartData1-58_001: To verify nurse name in navigation menu")
    @pytest.mark.parametrize("nurse, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1642"))
    def test_verify_dropdown_nurse_navigation(self, nurse, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.verify_name(nurse, DropdownNavigationXpath.drpdwn_name)
        except:
            assert False


    @pytest.mark.smoke
    @allure.title("TC_smartData1-58_002: To verify navigation menu is working")
    def test_verify_nurse_navigation_is_working(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.verify_navigation_dropdown()
        except:
            assert False


    @pytest.mark.smoke
    @allure.title("TC_smartData1-58_003: To verify on clicking “profile“ from navigation menu user is redirected to profile page")
    @pytest.mark.parametrize("nurse, profile, password, logout", data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1642"))
    def test_verify_nurse_navigation_profile_menu(self, nurse, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_profile_menu()
            navigation.verify_name(profile, DropdownNavigationXpath.verify_profile)
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-58_004: To verify on clicking “password“ from navigation menu user is redirected to change password page")
    @pytest.mark.parametrize("nurse, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1642"))
    def test_verify_nurse_navigation_password_menu(self, nurse, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_password_menu()
            navigation.verify_name(password, DropdownNavigationXpath.verify_password)
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("TC_smartData1-58_005: To verify user is logged out from the application on clicking “logout” from navigation menu ")
    @pytest.mark.parametrize("nurse, profile, password, logout",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1642"))
    def test_verify_nurse_navigation_logout(self, nurse, profile, password, logout):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            navigation = DropdownNavigationPage(self.driver)
            navigation.click_navigation_dropdown()
            navigation.click_logout()
            navigation.verify_name(logout, DropdownNavigationXpath.verify_logout)
        except:
            assert False
