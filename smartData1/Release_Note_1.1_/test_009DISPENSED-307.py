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



class TestsmartData1307(BaseTest):
    @pytest.mark.smoke
    @allure.title("smartData1-307: Approver/Doctor Portal: Navigation Updates")
    def test_navigation_in_approver_portal(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login",
                                                    2, 1)
            search_appointment.verify_navigation_dropdown()
        except:
            assert False

