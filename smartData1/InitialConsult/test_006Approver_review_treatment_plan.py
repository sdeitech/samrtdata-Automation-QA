import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan

class TestReviewTreatmentPlan(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    @allure.title("Test Modify Treatment Plan from Approver")
    # @pytest.mark.parametrize("search_user_appointment",
    #                          data_reader.get_data_from_excel("TestData/smartData1.xlsx", "Review_Treatment_Plan"))
    def test_modify_treatment_plan(self,):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.view_pending_prescription()
            modify_treatment_plan = TreatmentPlan(self.driver)
            modify_treatment_plan.modify_treatment_plan()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    @allure.title("Test Start Treatment Plan")
    # @pytest.mark.parametrize("search_user_appointment",
    #                          data_reader.get_data_from_excel("TestData/smartData1.xlsx", "Review_Treatment_Plan"))
    def test_start_treatment_plan(self,):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.view_pending_prescription()
            start_treatment_plan = TreatmentPlan(self.driver)
            start_treatment_plan.click_start_treatment_plan()
        except:
            assert False

