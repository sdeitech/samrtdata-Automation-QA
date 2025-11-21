import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from Utilities import data_reader


class TestLogin(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title("Test Patient login with valid credentials")
    def test_login_with_valid_credentials(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/InitialConsult.xlsx", "Login")
            login_page.login_into_application()
        except:
            assert False

