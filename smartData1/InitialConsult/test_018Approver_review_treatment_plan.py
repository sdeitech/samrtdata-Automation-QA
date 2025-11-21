import allure
import pytest

from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.TreatmentPlan.TreatmentPlanPage import TreatmentPlan
from Utilities import data_reader


class TestReviewTreatmentPlan(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title(
        "TC_Approver_Review_002, smartData1-586 :Patient-Login To verfy to Approve the treatment plan once approved from approver side")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp"))
    def test_approver_approves_treatment_plan1(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, email, firstname, lastname, medicare_number,
                                               password, phone,
                                               reference_number)
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title(
        "TC_Approver_Review_002, smartData1-586 :Nurse login  - To verfy to Approve the treatment plan once approved "
        "from approver side")
    def test_approver_approves_treatment_plan2(self):
        try:
            self.login_as_nurse_approve_treatment_logout()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title(
        "TC_Approver_Review_002, smartData1-586 :Nurse login  - To verfy to Approve the treatment plan once approved "
        "from approver side")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp"))
    def test_approver_approves_treatment_plan3(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                               medicare_number, reference_number):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                    1)
            search_appointment.search_consultations()
            search_appointment.view_pending_prescription()
            modify_treatment_plan = TreatmentPlan(self.driver)
            modify_treatment_plan.click_start_treatment_plan()
            modify_treatment_plan.verify_treatment_plan_message()

        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    @allure.title(
        "TC_Approver_Review_009, smartData1-586 : To verify when Start the treatment plan should remove from review "
        "appication list")
    def test_patient_not_seen_under_review(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                    1)
            search_appointment.search_consultations()
            # Patient record Should NOT be visible
            search_appointment.patient_profile_not_present()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title("TC_Approver_Review_011, smartData1-586 :To verify OrderNo.,Name,Status,Doctor,Consultation Time")
    def test_row_details(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                    1)
            search_appointment.search_consultations()
            search_appointment.verify_patient_nurse_row_header()
        except:
            assert False

    @pytest.mark.run(order=4)
    @allure.title(
        "TC_Approver_Review_013, smartData1-586 :To verify to check the plan details as per Plan: "
        "Indica-and-Sativa-Flower in Plan Sumnmary details. ")
    def test_treatment_plan_details(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                    1)
            search_appointment.search_consultations()
            search_appointment.view_pending_prescription()
            search_appointment.verify_treatment_plan_details()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    @allure.title(
        "TC_Approver_Review_003 smartData1-586 :Patient Login, To verfy to Approve the treatment plan once rejected from approver side")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp"))
    def test_approver_reject_treatment_plan1(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                             medicare_number, reference_number):
        try:
            self.signup_new_patient_and_logout(addr, confirm, dob, email, firstname, lastname, medicare_number,
                                               password, phone,
                                               reference_number)
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=11)
    @allure.title(
        "TC_Approver_Review_003, smartData1-586 :Nurse Login, To verfy to Approve the treatment plan once rejected from approver side")
    def test_approver_reject_treatment_plan2(self):
        try:
            self.login_as_nurse_approve_treatment_logout()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=12)
    @allure.title(
        "TC_Approver_Review_003, smartData1-586 :Approver Login and Reject, To verfy to Approve the treatment plan once rejected from approver side")
    def test_approver_reject_treatment_plan3(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Approver_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2,
                                                    1)
            search_appointment.search_consultations()
            search_appointment.view_pending_prescription()
            modify_treatment_plan = TreatmentPlan(self.driver)
            modify_treatment_plan.click_reject_treatment_plan()
            modify_treatment_plan.verify_reject_treatment_plan_message()
        except:
            assert False

    def signup_new_patient_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                      phone,
                                      reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        calendly_page.logout()

    def login_as_nurse_approve_treatment_logout(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp", 2, 1)
            search_appointment.search_consultations()
            search_appointment.review_application()
            treatment_plan = TreatmentPlan(self.driver)
            treatment_plan.select_treatment_plan_defined()
            treatment_plan.logout()
        except:
            assert False
