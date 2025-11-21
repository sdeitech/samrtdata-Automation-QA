import allure
import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from smartData1.BaseTest import BaseTest
from PageObjects.Comman.SignUp.SignUpXpath import SignUpPageXpath
from PageObjects.smartData1.Profile.ProfilePage import ProfilePage
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage
from PageObjects.smartData1.OnlineStoreModal.OnlineStorePage import OnlineStorePage
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from Utilities import data_reader



class TestsmartData1221(BaseTest):
    @pytest.mark.smoke
    @allure.title("smartData1-221: Add modal to 'Online Store' menu item")
    def test_add_online_store_modal(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1/Release1.1.xlsx", "Login")
            login_page.login_into_application()
            sidenav = SideNavPage(self.driver)
            sidenav.click_online_store()
            store = OnlineStorePage(self.driver)
            store.click_shop_modal()

        except:
            assert False

