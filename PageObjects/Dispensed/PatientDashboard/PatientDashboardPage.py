import random

from PageObjects.Dispensed.PatientDashboard.PatientDashboardXpath import PatientDashboardXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class PatientDashboardPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Tooltip icon")
    def click_tooltip_icon(self):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientDashboardXpath.tooltip_icon)
        except Exception as e:
            allure.attach(str(e), name="click_tooltip_icon_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Next Button")
    def click_next_btn(self):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientDashboardXpath.next_btn)
        except Exception as e:
            allure.attach(str(e), name="click_next_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Previous Button")
    def click_previous_btn(self):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientDashboardXpath.previous_btn)
        except Exception as e:
            allure.attach(str(e), name="click_previous_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Get Started Button")
    def click_get_started_btn(self):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientDashboardXpath.get_started_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="click_get_started_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Text")
    def verify_text(self, expected, xpath):
        try:
            actual = self.get_element_text(xpath)
            if expected.lower() == actual.lower():
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_text_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View Information Guide")
    def view_information_guide(self):
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.click_get_started_btn()

    @allure.step("View Tooltip")
    def view_tooltip(self):
        self.click_tooltip_icon()
        self.view_information_guide()

    @allure.step("Verify non cancelable from text from dashboard tab")
    def verify_non_cancel_dashboard(self, expected):
        self.verify_text(expected, PatientDashboardXpath.cancel_verify)

    @allure.step("Verify non cancelable from text from consultation tab")
    def verify_non_cancel_consultation(self, expected):
        self.verify_text(expected, PatientDashboardXpath.consultation_cancel_verify)


    @allure.step("Click on Shop Vaporiser button")
    def click_shop_vaporiser_btn(self, position):
        try:
            xpath= str(PatientDashboardXpath.shop_vaporiser+"["+position+"]")
            self.wait_for_sync(2)
            self.scroll_into_element(xpath)
            self.wait_for_sync(2)
            self.mouse_click_action(xpath)
            self.verify_shop()
        except Exception as e:
            allure.attach(str(e), name="click_shop_vaporiser_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Shop Accessories button")
    def click_shop_accessories_btn(self, position):
        try:
            xpath = str(PatientDashboardXpath.shop_accessories + "[" + position + "]")
            self.wait_for_sync(2)
            self.scroll_into_element(xpath)
            self.wait_for_sync(2)
            self.mouse_click_action(xpath)
            self.verify_shop()
        except Exception as e:
            allure.attach(str(e), name="click_shop_accessories_btn_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Shop")
    def verify_shop(self):
        try:
            self.current_window()
            self.close_current_window()
        except Exception as e:
            allure.attach(str(e), name="verify_shop_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click Close Button of online store modal")
    def click_modal_close_btn(self):
        try:
            self.wait_for_sync(2)
            self.mouse_click_action(PatientDashboardXpath.modal_close_btn)
        except Exception as e:
            allure.attach(str(e), name="click_modal_close_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify modal is visible or not ")
    def verify_modal_visibility(self):
        try:
            self.wait_for_sync(2)
            self.wait_for_element_to_be_displayed(PatientDashboardXpath.online_store_modal)
        except Exception as e:
            allure.attach(str(e), name="verify_modal_visibility_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Tooltip is visible or not ")
    def verify_tooltip_visibility(self):
        try:
            self.wait_for_sync(2)
            self.wait_for_element_to_be_displayed(PatientDashboardXpath.onboard_tooltip_modal)
        except Exception as e:
            allure.attach(str(e), name="verify_tooltip_visibility_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    def click_outside_modal(self):
        try:
            # Use JavaScript to click outside the modal (e.g., on the body element)
            self.driver.execute_script("document.querySelector('body').click();")
            self.log.info("Clicked outside the modal to close it.")

            # Attach a screenshot after the action
            allure.attach(self.driver.get_screenshot_as_png(), name="click_outside_modal_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            # Log any error that occurs
            self.log.error("Exception occurred while clicking outside the modal.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="click_outside_modal_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e
