import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Profile.ProfilePage import ProfilePage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader



class TestsmartData158(BaseTest):
    @pytest.mark.smoke
    @allure.title("smartData1-58: Nurse Portal: Navigation Menu Updates")
    def test_navigation_in_nurse_portal(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login",
                                                    2, 1)
            search_appointment.verify_navigation_dropdown()
        except:
            assert False

