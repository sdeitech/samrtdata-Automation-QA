import random
import string
import allure
import pytest

from smartData1.BaseTest import BaseTest
from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.NurseDashboard.NurseDashboardPage import NurseDashboardPage


class TestNurseProfile(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    @allure.title("TC_Nurse_Profile_001, smartData1-615 :To verify that the required fields are mandatory")
    def test_nurse_profile_field_mandatory(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Profile")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.click_nurse_profile()
            nurse_page.verify_last_name_star()
            nurse_page.verify_first_name_star()
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    @allure.title("TC_Nurse_Profile_002, smartData1-615 :To verify that the input fields are editible")
    def test_nurse_profile_editable(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.click_nurse_profile()
            rand_text = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
            nurse_page.update_first_name(rand_text)
            nurse_page.update_last_name(rand_text)
            nurse_page.click_save_changes_button()
            nurse_page.verify_profile_update_success_message()
            nurse_page.verify_last_name(rand_text)
            nurse_page.verify_first_name(rand_text)
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    @allure.title("TC_Nurse_Profile_003, smartData1-615 :To verify that submitting the form with empty name or invalid "
                  "format field displays a validation message")
    def test_nurse_profile_update_empty_values(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.click_nurse_home_page_link()
            nurse_page.click_nurse_profile()
            nurse_page.update_first_name("")
            nurse_page.update_last_name("")
            nurse_page.click_save_changes_button()
            nurse_page.verify_profile_update_success_not_present()
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @allure.title("TC_Nurse_Profile_004, smartData1-615 :To verify that the input fields accepts valid input format")
    def test_nurse_profile_update_valid_data(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.click_nurse_profile()
            nurse_page.update_first_name("Shruti")
            nurse_page.update_last_name("Sahatpure")
            nurse_page.click_save_changes_button()
            nurse_page.verify_profile_update_success_message()
            nurse_page.verify_last_name("Sahatpure")
            nurse_page.verify_first_name("Shruti")
            assert True
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @allure.title(
        "TC_Nurse_Profile_005, smartData1-615 :To verify when click on backward buton it should redirected to home "
        "screen")
    def test_nurse_back_button_page_title(self):
        try:
            nurse_page = NurseDashboardPage(self.driver)
            nurse_page.click_nurse_home_page_link()
            nurse_page.click_nurse_profile()
            nurse_page.navigate_back()
            nurse_page.verify_upcoming_consult_title("Today's Consults")
            assert True
        except:
            assert False
