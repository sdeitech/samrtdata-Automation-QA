import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.Payment.PaymentPage import PaymentPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage


class TestBookFollowUpAppointment(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=11)
    @allure.title("Test booking follow-up appointment from patient portal")
    # @pytest.mark.parametrize("username, password", data_reader.get_data_from_excel("TestData/smartData1.xlsx", "Login"))
    def test_book_followup_appointment(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/FollowUpConsult.xlsx", "Login")
            login_page.login_into_application()
            calendly = CalendlyPage(self.driver)
            calendly.calendly_book_appointment_from_patient_portal()

        except:
            assert False



