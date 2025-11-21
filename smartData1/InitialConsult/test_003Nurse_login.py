import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader


class TestLogin(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title("Test Nurse login with valid credentials")
    def test_login_with_valid_credentials(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Nurse_Login")
            login_page.login_into_application()
        except:
            assert False

