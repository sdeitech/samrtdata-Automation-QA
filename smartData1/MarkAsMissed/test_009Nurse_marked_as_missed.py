import pytest

from PageObjects.Comman.Login.LoginPage import LoginPage
from smartData1.BaseTest import BaseTest
from PageObjects.smartData1.SearchConsults.SearchConsultsPage import SearchConsultsPage
from PageObjects.smartData1.SideNav.SideNavPage import SideNavPage


class TestMarkedAsMissed(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.run(order=11)
    def test_marked_as_missed(self):
        try:
            login_page = LoginPage(self.driver, "TestData/smartData1.xlsx", "Nurse_Login")
            login_page.login_into_application()
            search_appointment = SearchConsultsPage(self.driver, "TestData/smartData1.xlsx", "Login", 2, 1)
            search_appointment.search_consultations()
            search_appointment.mark_as_missed()
            side_nav = SideNavPage(self.driver)
            side_nav.click_consultation()
            side_nav.click_missed_consults()
            search_appointment.search_consultations()
            search_appointment.review_application()
            assert True
        except:
            assert False
