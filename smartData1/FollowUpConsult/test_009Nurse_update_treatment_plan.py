import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.Payment.PaymentPage import PaymentPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan
from Utilities import data_reader
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.smartData1.PatientNote.PatientNotePage import PatientNotePage


class TestUpdateTreatmentPlan(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=12)
    @allure.title("Test update treatment plan of follow appointment patient from nurse portal")
    @pytest.mark.parametrize(
        "medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms",
        data_reader.get_data_from_excel("TestData/smartData1/FollowUpConsult.xlsx", "Upcoming_Appointment"))
    def test_update_treatment_plan(self, medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/FollowUpConsult.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/FollowUpConsult.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            update_plan = PatientNotePage(self.driver)
            update_plan.update_treatment_plan(expiry_date, reference_number)
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.update_treatment_plan()
        except:
            assert False



