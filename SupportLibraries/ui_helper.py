
import os
import time
import logging
import random
import string
from traceback import print_stack

import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from Utilities import logger_utility as log_utils


class UIHelpers:
    def __init__(self, driver):
        self.driver = driver

    log = log_utils.custom_logger(logging.INFO)

    def get_title(self):
        page_title = ""
        try:
            page_title = self.driver.title
            if page_title is None:
                self.log.error("Page title value is empty.")
        except:
            self.log.error("Exception occurred while retrieving the page title.")
        return page_title

    def get_locator_type(self, locator_type):
        try:
            locator_type = locator_type.lower()

            if locator_type == "id":
                return By.ID
            elif locator_type == "xpath":
                return By.XPATH
            elif locator_type == "name":
                return By.NAME
            elif locator_type == "class":
                return By.CLASS_NAME
            elif locator_type == "link":
                return By.LINK_TEXT
            elif locator_type == "partiallink":
                return By.PARTIAL_LINK_TEXT
        except:
            self.log.error("Locator Type '" + locator_type + "' is not listed.")

    def wait_for_element_to_be_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except Exception as e:
            self.log.error("Exception occurred while waiting for element to be present.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_is_not_present",
                          attachment_type=allure.attachment_type.PNG)
            raise e
            # return False

    def wait_for_all_elements_to_be_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            elements = WebDriverWait(self.driver, max_time_out,
                                     ignored_exceptions=[StaleElementReferenceException]).until(
                EC.presence_of_all_elements_located((self.get_locator_type(locator_type), locator_properties))
            )
            return elements
        except Exception as e:
            self.log.error("Exception occurred while waiting for all elements to be present.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_is_not_present",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def wait_for_element_to_be_clickable(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.element_to_be_clickable((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except Exception as e:
            self.log.error("Exception occurred while waiting for element to be clickable.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_is_not_present",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def wait_for_element_to_be_displayed(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.visibility_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            self.log.error("Exception occurred while waiting for element to be visible.")
            return False

    def wait_for_element_to_be_invisible(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            WebDriverWait(self.driver, max_time_out, ignored_exceptions=[StaleElementReferenceException]).until(
                EC.invisibility_of_element_located((self.get_locator_type(locator_type), locator_properties))
            )
            return True
        except:
            return False

    def is_element_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        flag = False
        try:
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element present with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                flag = True
            else:
                self.log.error(
                    "Element not present with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during element identification.")
        return flag

    def is_button_disabled(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            self.driver.implicitly_wait(0)  # Temporarily set implicit wait to 0
            elements = self.driver.find_elements(getattr(By, locator_type.upper()), locator_properties)

            if len(elements) == 0:
                self.log.error(
                    f"Button not found with locator_properties: {locator_properties} and locator_type: {locator_type}")
                allure.attach(self.driver.get_screenshot_as_png(), name="button_not_found",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception("Button not found.")
            else:
                button = elements[0]
                if button.get_attribute("disabled"):
                    self.log.info(
                        f"Button is disabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
                    allure.attach(self.driver.get_screenshot_as_png(), name="button_disabled",
                                  attachment_type=allure.attachment_type.PNG)
                    return True
                else:
                    self.log.error(
                        f"Button is enabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
                    allure.attach(self.driver.get_screenshot_as_png(), name="button_enabled",
                                  attachment_type=allure.attachment_type.PNG)
                    raise Exception("Button is enabled")
        except Exception as e:
            self.log.error(
                f"Error occurred while checking if button is disabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
            self.log.error("Exception occurred during button status check.")
            allure.attach(self.driver.get_screenshot_as_png(), name="ERROR:button_check_failed",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="ERROR:exception_message", attachment_type=allure.attachment_type.TEXT)
            raise e

    def is_input_disabled(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            # Temporarily set implicit wait to 0
            self.driver.implicitly_wait(0)
            elements = self.driver.find_elements(getattr(By, locator_type.upper()), locator_properties)

            if len(elements) == 0:
                self.log.error(
                    f"Input element not found with locator_properties: {locator_properties} and locator_type: {locator_type}")
                allure.attach(self.driver.get_screenshot_as_png(), name="input_not_found",
                              attachment_type=allure.attachment_type.PNG)
                raise Exception("Input element not found.")
            else:
                input_element = elements[0]
                is_disabled = input_element.get_attribute("disabled") or input_element.get_attribute(
                    "aria-disabled") == "true" or input_element.get_attribute("readonly")
                if is_disabled:
                    self.log.info(
                        f"Input element is disabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
                    allure.attach(self.driver.get_screenshot_as_png(), name="input_disabled",
                                  attachment_type=allure.attachment_type.PNG)
                    return True
                else:
                    self.log.info(
                        f"Input element is enabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
                    allure.attach(self.driver.get_screenshot_as_png(), name="input_enabled",
                                  attachment_type=allure.attachment_type.PNG)
                    raise Exception("Input is editable")
        except Exception as e:
            self.log.error(
                f"Error occurred while checking if input element is disabled with locator_properties: {locator_properties} and locator_type: {locator_type}")
            self.log.error("Exception occurred during input element status check.")
            allure.attach(self.driver.get_screenshot_as_png(), name="ERROR:input_check_failed",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="ERROR:exception_message", attachment_type=allure.attachment_type.TEXT)
            raise e
        finally:
            # Restore the original implicit wait time
            self.driver.implicitly_wait(max_time_out)

    def verify_element_not_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        flag = False
        try:
            if self.wait_for_element_to_be_invisible(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element invisible with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                flag = True
            else:
                self.log.error(
                    "Element is visible with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during element to be invisible.")
        return flag

    def is_element_displayed(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            if self.wait_for_element_to_be_displayed(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Element found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return True
            else:
                self.log.error(
                    "Element not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                return False
        except:
            self.log.error("Exception occurred during element identification.")
            return False

    def is_element_clickable(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            self.wait_for_element_to_be_clickable(locator_properties, locator_type, max_time_out)
            self.log.info("Element is clickable with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(self.driver.get_screenshot_as_png(), name="element_is_clickable",
                          attachment_type=allure.attachment_type.PNG)
            return True
        except Exception as e:
            self.log.error("Element is not clickable with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            self.log.error("Exception occurred during element identification.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_is_not_clickable",
                          attachment_type=allure.attachment_type.PNG)
            raise e
            # return False


    def is_element_checked(self, locator_properties, locator_type="xpath", max_time_out=10):
        flag = False
        try:
            if self.is_element_present(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                if element.is_selected():
                    self.log.info(
                        "Element is selected/ checked with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
                    flag = True
                else:
                    self.log.error(
                        "Element is not selected/ checked with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            flag = False
        return flag

    def verify_elements_located(self, locator_dict, max_timeout=10):
        flag = False
        result = []
        try:
            for locator_prop in locator_dict.keys():
                prop_type = locator_dict[locator_prop]
                if self.wait_for_element_to_be_present(locator_prop, prop_type, max_timeout):
                    self.log.info(
                        "Element found with locator_properties: " + locator_prop + " and locator_type: " + locator_dict[
                            locator_prop])
                    flag = True
                else:
                    self.log.error(
                        "Element not found with locator_properties: " + locator_prop + " and locator_type: " +
                        locator_dict[locator_prop])
                    flag = False
                result.append(flag)
        except Exception as ex:
            self.log.error("Exception occurred during element identification: ", ex)

        if False in result:
            return False
        else:
            return True

    def check_element(self, locator_properties, locator_type="xpath", max_time_out=10):
        element = None
        try:
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                element = self.driver.find_element(locator_type, locator_properties)
                self.log.info(
                    "Element found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error(
                    "Element not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except Exception as e:
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="check_element_exception",
                          attachment_type=allure.attachment_type.PNG)
            self.log.error("Exception occurred during getting element.")
        return element

    def get_element(self, locator_properties, locator_type="xpath", max_time_out=10):
        element = None
        try:
            self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out)
            element = self.driver.find_element(locator_type, locator_properties)
            self.log.info(
                    "Element found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except Exception as e:
            self.log.error(
                "Element not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            self.log.error("Exception occurred during element identification.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_not_present",
                          attachment_type=allure.attachment_type.PNG)
            raise e
        return element

    def get_element_list(self, locator_properties, locator_type="xpath", max_time_out=10):
        element = None
        try:
            # self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out)
            element = self.driver.find_elements(locator_type, locator_properties)
            self.log.info(
                    "Elements found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except Exception as e:
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_not_present",
                          attachment_type=allure.attachment_type.PNG)
            self.log.error(
                "Elements not found with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            self.log.error("Exception occurred during getting elements.")
            raise e
        return element

    def get_text_from_element(self, locator_properties, locator_type="xpath", max_time_out=10):
        result_text = ""
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            result_text = element.text
            if len(result_text) == 0:
                result_text = element.get_attribute("innerText")
            elif len(result_text) != 0:
                self.log.info("The text is: '" + result_text + "'")
                result_text = result_text.strip()
        except:
            self.log.error("Exception occurred during text retrieval.")
            print_stack()
        return result_text

    def get_element_text(self, locator_properties, locator_type="xpath", max_time_out=10):
        text = ""
        try:
            self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out)
            element = self.driver.find_element(locator_type, locator_properties)
            text = element.text
            self.log.info(
                "Text retrieved from element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except Exception as e:
            self.log.error(
                "Failed to retrieve text from element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            self.log.error("Exception occurred during text retrieval.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:element_text_not_retrieved",
                          attachment_type=allure.attachment_type.PNG)
            raise e
        return text

    def get_attribute_value_from_element(self, attribute_name, locator_properties, locator_type="xpath",
                                         max_time_out=10):
        attribute_value = ""
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            attribute_value = element.get_attribute(attribute_name)
            if attribute_value is not None:
                self.log.info(attribute_name.upper() + " value is: " + attribute_value)
            else:
                self.log.error(attribute_name.upper() + " value is empty.")
        except:
            self.log.error("Exception occurred during attribute value retrieval.")
        return attribute_value

    def mouse_click_action(self, locator_properties, locator_type="xpath", max_time_out=20):
        try:
            self.is_element_clickable(locator_properties, locator_type, max_time_out)
            self.scroll_into_element(locator_properties)
            element = self.get_element(locator_properties, locator_type, max_time_out)
            element.click()
            self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(self.driver.get_screenshot_as_png(), name="click_screenshot",
                              attachment_type=allure.attachment_type.PNG)
            # else:
        except Exception as e:
            self.log.error("Exception occurred during mouse click action.")
            self.log.error(
                "Unable to click on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="click_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def move_to_element_and_click(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            self.is_element_clickable(locator_properties, locator_type, max_time_out)
            element = self.get_element(locator_properties, locator_type, max_time_out)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)

        except Exception as e:
            self.log.error("Exception occurred during mouse click action.")
            self.log.error(
                "Unable to click on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="click_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def wait_and_click(self, element):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(element)
            element.click()
            allure.attach(self.driver.get_screenshot_as_png(), name="wait_and_click_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            self.wait_for_sync(2)
        except Exception as e:
            self.log.error("Exception occurred during mouse click action.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="wait_and_click_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="wait_and_click_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    def toggle_checkbox(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            self.scroll_into_element(locator_properties)
            current_state = self.driver.execute_script("return arguments[0].checked;", element)
            new_state = not current_state
            self.driver.execute_script("arguments[0].checked = arguments[1];", element, new_state)
            self.log.info(f"Checkbox toggled to {new_state} for element with locator_properties: {locator_properties} and locator_type: {locator_type}")
            allure.attach(self.driver.get_screenshot_as_png(), name="checkbox_screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error("Exception occurred during checkbox toggle action.")
            self.log.error(f"Unable to toggle checkbox with locator_properties: {locator_properties} and locator_type: {locator_type}")
            allure.attach(str(e), name="checkbox_toggle_error", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.driver.get_screenshot_as_png(), name="checkbox_toggle_error_screenshot", attachment_type=allure.attachment_type.PNG)
            raise e

    def select_option_by_value(self, option_value, dropdown_locator_properties, dropdown_locator_type="xpath", max_time_out=10):
        try:
            dropdown_element = self.get_element(dropdown_locator_properties, dropdown_locator_type, max_time_out)
            self.scroll_into_element(dropdown_locator_properties)
            select = Select(dropdown_element)
            select.select_by_value(option_value)
            self.log.info("Selected option with value '{}' from dropdown with locator_properties: {} and locator_type: {}".format(
                option_value, dropdown_locator_properties, dropdown_locator_type))
            allure.attach(self.driver.get_screenshot_as_png(), name="select_option_by_value_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error("Exception occurred during selecting option by value from dropdown.")
            self.log.error("Unable to select option with value '{}' from dropdown with locator_properties: {} and locator_type: {}".format(
                option_value, dropdown_locator_properties, dropdown_locator_type))
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="select_option_by_value_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e


    def scroll_into_element(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            self.driver.execute_script("return arguments[0].scrollIntoView();", element)
            if self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out):
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during scrolling to element.")

    def scroll_to_end_of_page(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.wait_for_sync(5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.log.info("Scrolled to the end of the page.")
        except:
            self.log.error("Exception occurred during scrolling to the end of the page.")

    def mouse_click_action_on_element_present(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            if self.is_element_present(locator_properties, locator_type, max_time_out):
                element = self.get_element(locator_properties, locator_type, max_time_out)
                element.click()
                self.log.info(
                    "Clicked on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            else:
                self.log.error(
                    "Unable to click on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
        except:
            self.log.error("Exception occurred during mouse click action.")



    def send_text_action(self, text_value, locator_properties, locator_type="xpath", max_time_out=10):
        element = None
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            self.scroll_into_element(locator_properties)
            element.clear()
            element.send_keys(text_value)
            self.log.info(
                "Sent data to the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(self.driver.get_screenshot_as_png(), name="input_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error(
                "Unable to send data on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="input_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def enter_text_action(self, text_value, locator_properties, locator_type="xpath", max_time_out=10):
        element = None
        try:
            element = self.get_element(locator_properties, locator_type, max_time_out)
            self.scroll_into_element(locator_properties)
            element.clear()
            element.send_keys(text_value)
            element.send_keys(Keys.ENTER)
            self.log.info(
                "Sent data to the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type + " and pressed Enter.")
            allure.attach(self.driver.get_screenshot_as_png(), name="input_screenshot",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error(
                "Unable to send data on the element with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="input_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    @allure.step("Verify validation of expected text: {expected}")
    def verify_validation_text(self, xpath, expected):
        try:
            self.log.info(f"Starting verify_invalid with xpath: {xpath} and expected value: {expected}")
            actual = self.get_element_text(xpath)
            self.log.info(f"Actual value obtained: {actual}")

            if expected.lower() == actual.lower():
                self.log.info(f"Expected value '{expected}' matches actual value '{actual}'. Verification passed.")
                allure.attach(self.driver.get_screenshot_as_png(), name="validation_screenshot",
                              attachment_type=allure.attachment_type.PNG)
                assert True
            else:
                error_message = f"Expected value '{expected}' does not match actual value '{actual}'. Verification failed."
                self.log.error(error_message)
                raise AssertionError(error_message)
        except Exception as e:
            self.log.error(f"Exception occurred in verify_invalid with xpath: {xpath} and expected value: {expected}")
            self.log.error(f"Exception details: {e}")
            allure.attach(self.driver.get_screenshot_as_png(), name="error_validation_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="verify_invalid_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    def verify_text_contains(self, actual_text, expected_text):
        if expected_text.lower() in actual_text.lower():
            self.log.info("### TEXT CONTAINS VERIFICATION PASSED !!!")
            return True
        else:
            self.log.error("### TEXT VERIFICATION FAILED:\nActual Text --> {}\nExpected Text --> {}"
                           .format(actual_text, expected_text))
            return False


    def verify_text_match(self, actual_text, expected_text):
        if expected_text.lower() == actual_text.lower():
            self.log.info("### TEXT VERIFICATION PASSED !!!")
            return True
        else:
            self.log.error("### TEXT VERIFICATION FAILED:\nActual Text --> {}\nExpected Text --> {}"
                           .format(actual_text, expected_text))
            return False

    def click_on_link(self, click_link):
        try:
            self.mouse_click_action(click_link,locator_type="link",max_time_out=5)
            #element = self.driver.find_element_by_link_text(click_link)
            # element.click()
            # self.driver.find_element_by_partial_link_text(click_link).click()
            # self.wait_for_sync(10)
            # self.driver.find_element_by_link_text(click_link).click()
            self.wait_for_sync(20)
        except:
            self.log.error("Unable to find the given link ", click_link)
            allure.attach("Unable to click on given link", name="Link_Exception",
                          attachment_type=allure.attachment_type.TEXT)
            return False

    def take_screenshots(self, file_name_initials):
        file_name = file_name_initials + "." + str(round(time.time() * 1000)) + ".png"
        cur_path = os.path.abspath(os.path.dirname(__file__))
        screenshot_directory = os.path.join(cur_path, r"../Logs/Screenshots/")
        destination_directory = os.path.join(screenshot_directory, file_name)
        try:
            if not os.path.exists(screenshot_directory):
                os.makedirs(screenshot_directory)
            self.driver.save_screenshot(destination_directory)
            self.log.info("Screenshot saved to directory: " + destination_directory)
        except Exception as ex:
            self.log.error("### Exception occurred:: ", ex)
            print_stack()

        return destination_directory


    def page_scrolling(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")


    # def switch_to_created_object_frame(self, locator_properties, locator_type="xpath", max_time_out=10):
    #     try:
    #         frames = self.get_element_list("//iframe")
    #         for frame in frames:
    #             frame_name = frame.get_attribute('name')
    #             if frame_name is not None:
    #                 self.driver.switch_to.frame(frame_name)
    #                 result = self.is_element_present(locator_properties, locator_type, max_time_out)
    #                 if not result:
    #                     self.driver.switch_to.default_content()
    #                     continue
    #
    #                 else:
    #                     self.log.info("Element found on frame: " + str(frame_name))
    #                     break
    #             else:
    #                 self.driver.switch_to.default_content()
    #                 continue
    #
    #     except:
    #         self.log.error("Element not present on the page.")
    #
    #
    # def switch_to_default_content(self):
    #     try:
    #         self.driver.switch_to.default_content()
    #     except:
    #         self.log.error("Exception occurred while switching to default content..")

    def switch_to_iframe(self, locator_properties, locator_type="xpath", max_time_out=10):
        try:
            # Wait for the iframe to be present
            self.wait_for_element_to_be_present(locator_properties, locator_type, max_time_out)
            # Find the iframe element
            iframe = self.get_element(locator_properties, locator_type, max_time_out)
            # Switch to the iframe
            self.driver.switch_to.frame(iframe)
            self.log.info("Switched to iframe with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(self.driver.get_screenshot_as_png(), name="switch_to_iframe",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error("Exception occurred while switching to iframe.")
            self.log.error("Unable to switch to the iframe with locator_properties: " + locator_properties + " and locator_type: " + locator_type)
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:switch_to_iframe",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            self.log.info("Switched to default content (main document).")
            allure.attach(self.driver.get_screenshot_as_png(), name="switch_to_default_content",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            self.log.error("Exception occurred while switching to default content.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="ERROR:switch_to_default_content",
                          attachment_type=allure.attachment_type.PNG)
            raise e


    def wait_for_sync(self, seconds):
        time.sleep(seconds)


    def press_action_key(self, key=Keys.ENTER):
        actions = ActionChains(self.driver)
        actions.key_down(key).key_up(key).perform()

    def logout(self):
        try:
            #self.click_on_link("Logout")
            self.wait_for_sync(20)
            #self.mouse_click_action("//div[@class='w-100 d-md-block d-none ']/ul/li/a/span")
            self.mouse_click_action("//div[@class='navigation-menu']/div")
            self.wait_for_sync(20)
            self.mouse_click_action("//ul[@class='dropdown-menu dropdown-menu-lg-end show']/li[3]")
            self.wait_for_sync(20)
        except:
            self.log.error("Exception occurred while Logging out")




    def navigate_to_url(self, url, element):
        flag = False
        try:
            self.driver.get(url)
            if self.is_element_displayed(element):
                flag = True
        except:
            flag = False
            self.log.error("Exception occurred while navigating to the url.")

        return flag

    def refresh_page(self):
        self.driver.refresh()

    def current_window(self):
        """
        Log the URL of the current window.
        """
        try:
            # Get the current window's URL
            self.wait_for_sync(3)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.wait_for_sync(8)
            current_url = self.driver.current_url

            # Log the URL
            self.log.info(f"Current window URL: {current_url}")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{current_url}__screenshot",
                          attachment_type=allure.attachment_type.PNG)

            return current_url

        except Exception as e:
            self.log.error("Exception occurred while retrieving the current window URL.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="log_current_window_url_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def refresh_page(self):
        try:
            self.driver.refresh()
            self.log.info("Page refreshed successfully.")
        except Exception as e:
            self.log.error("Failed to refresh the page.")
            raise e

    def close_current_window(self):
        """
        Close the current window and log the action.
        """
        try:
            # Wait before switching to the window
            self.wait_for_sync(3)

            # current_url = self.driver.current_url
            self.log.info(f"Closed window with URL: {self.driver.current_url}")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"{self.driver.current_url}__closed_window_screenshot",
                                        attachment_type=allure.attachment_type.PNG)
            # Close the current window
            self.driver.close()

            self.wait_for_sync(5)
            # Switch back to the first window (or any other window, if needed)
            self.driver.switch_to.window(self.driver.window_handles[0])

            # Log the closure

            # allure.attach(self.driver.get_screenshot_as_png(), name=f"{current_url}__closed_window_screenshot",
            #               attachment_type=allure.attachment_type.PNG)

            self.wait_for_sync(3)
            # Switch back to the first window (or any other window, if needed)
            # self.driver.switch_to.window(self.driver.current_url)

        except Exception as e:
            self.log.error("Exception occurred while closing the current window.")
            allure.attach(str(e), self.driver.get_screenshot_as_png(), name="log_close_window_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e
    @staticmethod
    def string_generator(string_size=8, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(string_size))


    @staticmethod
    def digit_generator(string_size=10, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(string_size))