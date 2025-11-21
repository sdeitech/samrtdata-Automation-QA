import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.PatientNote.PatientNotePage import PatientNotePage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader
from PageObjects.smartData1.PatientDashboard.PatientDashboardPage import PatientDashboardPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage

class TestsmartData1134(BaseTest):


    @pytest.mark.smoke
    @allure.title("smartData1-134: Patient Portal: Onboarding Tooltip and Welcome Modals")
    def test_tooltip(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            dashboard = PatientDashboardPage(self.driver)
            dashboard.view_tooltip()
        except:
            assert False

