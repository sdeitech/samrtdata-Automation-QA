from PageObjects.Dispensed.DropdownNavigation.DropdownNavigationXpath import DropdownNavigationXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader


class DropdownNavigationPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on dropdown navigation")
    def click_navigation_dropdown(self):
        try:
            self.mouse_click_action(DropdownNavigationXpath.naviagtion_drpdwn)
        except Exception as e:
            allure.attach(str(e), name="click_navigation_dropdown_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Profile menu from dropdown navigation")
    def click_profile_menu(self):
        try:
            self.mouse_click_action(DropdownNavigationXpath.profile_menu)
        except Exception as e:
            allure.attach(str(e), name="click_profile_menu_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Click on Password menu from dropdown navigation")
    def click_password_menu(self):
        try:
            self.mouse_click_action(DropdownNavigationXpath.password_menu)
        except Exception as e:
            allure.attach(str(e), name="click_password_menu_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Logout from dropdown navigation")
    def click_logout(self):
        try:
            self.mouse_click_action(DropdownNavigationXpath.logout)
        except Exception as e:
            allure.attach(str(e), name="click_logout_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Verify Dropdown name")
    def verify_name(self, expected, xpath):
        try:
            actual = self.get_element_text(xpath)
            expe = str(expected)
            print("actual: "+actual )
            print("expected :"+expe)
            if expe == actual:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_name_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Verify navigation is working or not")
    def verify_navigation_dropdown(self):
        try:
            self.get_element(DropdownNavigationXpath.naviagtion_drpdwn_menus)
        except Exception as e:
            allure.attach(str(e), name="verify_navigation_dropdown_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise
