import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader
from PageObjects.smartData1.PatientNote.PatientNotePage import PatientNotePage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan
from PageObjects.smartData1.ClinicalNote.ClinicalNotePage import ClinicalNotesPage


class TestUpcomingConsults(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title("Test Update Patient notes with valid data")
    @pytest.mark.parametrize(
        "medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms",
        data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "Upcoming_Appointment"))
    def test_update_valid_patient_note_for_upcoming_consults(self, medicare_number, expiry_date, reference_number, ihi_number, occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login",2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            update_patient_note = PatientNotePage(self.driver)
            update_patient_note.create_patient_notes_with_valid_data(medicare_number, expiry_date, reference_number, ihi_number, occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms)
        except:
            assert False


    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title("Test create Clinical Notes with valid data")
    @pytest.mark.parametrize(
        "clinical_notes",
        data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "clinical_notes"))
    def test_create_valid_clinical_notes(self, clinical_notes):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            clinical_note = ClinicalNotesPage(self.driver)
            clinical_note.create_clinical_note(clinical_notes)
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title("Test select valid Treatment Plan")
    # @pytest.mark.parametrize(
    #     "medicare_number, expiry_date, reference_number, ihi_number,occupation, weight, height, allergies, sleep, therapies, diagnosed_year, practitioner, medications, symptoms",
    #     data_reader.get_data_from_excel("TestData/smartData1/InitialConsult.xlsx", "Upcoming_Appointment"))
    def test_select_valid_treatment_plan(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.select_treatment_plan()
        except:
            assert False