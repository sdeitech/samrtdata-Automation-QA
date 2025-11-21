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

class TestsmartData1513(BaseTest):


    @pytest.mark.smoke
    @allure.title(
        "smartData1-513: If nurse has approved the treatment plan, then user should not be able to cancel/reschedule the appointment.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx",
                                                             "SignUp"))
    def test_signup(self, email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, reference_number):
        try:
            signup_page = SignUpPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
            signup_page.set_password(password, confirm)
            typeform_page = TypeformPage(self.driver)
            typeform_page.enter_typeform_details(medicare_number, reference_number)
            calendly_page = CalendlyPage(self.driver)
            calendly_page.calendly_book_appointment()
        except:
            assert False



    @pytest.mark.smoke
    @allure.title("Test select valid Treatment Plan from nurse portal")
    @pytest.mark.parametrize(
        "medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms",
        data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "Upcoming_Appointment"))
    def test_select_valid_treatment_plan(self, medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            update_patient_note = PatientNotePage(self.driver)
            update_patient_note.create_patient_notes_with_valid_data(medicare_number, expiry_date, reference_number,
                                                                     ihi_number, occupation, weight, height, allergies,
                                                                     sleep, therapies, diagnosed_year, practitioner,
                                                                     medications, symptoms)
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.select_treatment_plan()
        except:
            assert False

    @pytest.mark.smoke
    @allure.title("Verify user should not be able to cancel")
    @pytest.mark.parametrize(
        "dashboard_txt, consultation_txt",
        data_reader.get_data_from_excel("TestData/smartData1/Release1.1.xlsx", "smartData1513"))
    def test_user_not_able_to_cancel(self, dashboard_txt, consultation_txt):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            dashboard = PatientDashboardPage(self.driver)
            dashboard.view_information_guide()
            dashboard.verify_non_cancel_dashboard(dashboard_txt)
            sidenav.click_consultation()
            dashboard.verify_non_cancel_consultation(consultation_txt)

        except:
            assert False

