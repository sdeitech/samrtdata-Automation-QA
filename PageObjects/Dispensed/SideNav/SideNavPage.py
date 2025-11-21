
from PageObjects.Dispensed.SideNav.SideNavXpath import SideNavXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader

class SideNavPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    # @allure.step("Searching patient appointment using email")
    # def search_consultations(self):
    #     try:
    #         self.enter_text_action(self.email_address, SearchConsultsXpath.search_box)
    #     except Exception as e:
    #         allure.attach(str(e), name="search_consultations_exception", attachment_type=allure.attachment_type.TEXT)
    #         raise

    @allure.step("Clicking on Consultations dropdown")
    def click_consultation(self):
        try:
            self.mouse_click_action(SideNavXpath.consultations)
        except Exception as e:
            allure.attach(str(e), name="click_consultation_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Home page")
    def click_home_page(self):
        try:
            self.mouse_click_action(SideNavXpath.home_page)
        except Exception as e:
            allure.attach(str(e), name="click_home_page_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Missed Consults")
    def click_missed_consults(self):
        try:
            self.mouse_click_action(SideNavXpath.missed_consults)
        except Exception as e:
            allure.attach(str(e), name="click_missed_consults_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Click on Profile link in side navigation bar")
    def click_profile(self):
        try:
            self.mouse_click_action(SideNavXpath.profile_link)
        except Exception as e:
            allure.attach(str(e), name="click_profile_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Clicking on Support")
    def click_support(self):
        try:
            self.mouse_click_action(SideNavXpath.support)
        except Exception as e:
            allure.attach(str(e), name="click_support_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Online Store")
    def click_online_store(self):
        try:
            self.mouse_click_action(SideNavXpath.online_store)
        except Exception as e:
            allure.attach(str(e), name="click_online_store_exception", attachment_type=allure.attachment_type.TEXT)
            raise

