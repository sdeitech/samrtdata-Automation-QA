import allure
import pytest

from smartData1.BaseTest import BaseTest
from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.Profile.ProfileHomePage import ProfileHomePage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage


class TestPatientLoginToChangePassword(BaseTest):
    ''' These Tests run according to given order
    Changes the Patient password and again resets back to original at end of test
    Prerequites : Reads data from Login Page, where
    Patient already signed Up and updated the sheet '''

    @pytest.mark.smoke
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
    @allure.title("TC_ChangePassword_002, smartData1-563 :To verify to change the Password Length < 8 Characters")
    def test_update_password_less_than_8_char(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_navigation_bar = SideNavPage(self.driver)
            side_navigation_bar.click_profile()
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_password_link()
            profile_page.profile_update_password_less_than_8_chars("Disp@123", "abcde67", "abcde67")
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_ChangePassword_003, smartData1-563 :To verify to change password with No Uppercase Letter")
    def test_update_password_no_upper_case(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_navigation_bar = SideNavPage(self.driver)
            side_navigation_bar.click_profile()
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_password_link()
            profile_page.profile_update_password_all_lower_case("Disp@123", "lower_case@123", "lower_case@123")
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_ChangePassword_004, smartData1-563 :To verify to change password with No Number")
    def test_update_password_no_number(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_navigation_bar = SideNavPage(self.driver)
            side_navigation_bar.click_profile()
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_password_link()
            profile_page.profile_update_password_no_number("Disp@123", "UPPER_CASE@lowerCase", "UPPER_CASE@lowerCase")
        except:
            assert False

    # @pytest.mark.skip
    @pytest.mark.smoke
    @allure.title("TC_ChangePassword_005, smartData1-563 :To verify to change password with No lowercase Letter")
    def test_update_password_no_lower_case(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "smartData1153")
            login_page.login_into_application()
            side_navigation_bar = SideNavPage(self.driver)
            side_navigation_bar.click_profile()
            profile_page = ProfileHomePage(self.driver)
            profile_page.click_password_link()
            profile_page.profile_update_password_all_upper_case("Disp@123", "UPPER_CASE@123", "UPPER_CASE@123")
        except:
            assert False

