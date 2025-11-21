import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.Payment.PaymentPage import PaymentPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader


class TestPurchaseTreatmentPlan(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    @allure.title("Test Purchase Treatment Plan from patient portal")
    # @pytest.mark.parametrize("username, password", data_reader.get_data_from_excel("TestData/smartData1.xlsx", "Login"))
    def test_purchase_treatment_plan(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login")
            login_page.login_into_application()
            payment = PaymentPage(self.driver)
            payment.make_payment_to_purchase_treatment_plan_with_valid_data()

        except:
            assert False



