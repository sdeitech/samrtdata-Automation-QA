from SupportLibraries.base_helper import BaseHelpers
from PageObjects.Dispensed.Profile.ProfileXpath import ProfileXpath

import allure


class ProfileHomePage(BaseHelpers):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Clicking on Password tab")
    def click_password_link(self):
        try:
            # self.click_on_link(ProfileXpath.password)
            self.mouse_click_action(ProfileXpath.password_xpath)
        except Exception as e:
            allure.attach(str(e), name="click_password_link", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Update password with lower case letters")
    def profile_update_password_all_lower_case(self, old_password, new_password, confirm_password):
        try:
            self.send_text_action(old_password, ProfileXpath.old_password)
            self.send_text_action(new_password, ProfileXpath.new_password)
            self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_req1)
            expected = self.get_error_text("password_one_upper_case")
            if actual == expected:
                assert True
            else:
                assert False, f"Expected was {expected} But actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="profile_password_all_lower_case_letters",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Update password with no numbers")
    def profile_update_password_no_number(self, old_password, new_password, confirm_password):
        try:
            self.send_text_action(old_password, ProfileXpath.old_password)
            self.send_text_action(new_password, ProfileXpath.new_password)
            self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_req1)
            expected = self.get_error_text("password_one_digit")
            if actual == expected:
                assert True
            else:
                assert False, f"Expected was {expected} But actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="profile_password_all_lower_case_letters",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Update password with commonly used")
    def profile_update_password_with_commonly_used(self, old_password, new_password, confirm_password):
        try:
            self.send_text_action(old_password, ProfileXpath.old_password)
            self.send_text_action(new_password, ProfileXpath.new_password)
            self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_req1)
            expected = self.get_error_text("password_special_char")
            if expected[:30] == actual[:30]:
                assert True
            else:
                assert False, f"Expected was {expected} But actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="profile_password_commonly_used",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Update password with lower case letters")
    def profile_update_password_all_upper_case(self, old_password, new_password, confirm_password):
        try:
            self.send_text_action(old_password, ProfileXpath.old_password)
            self.send_text_action(new_password, ProfileXpath.new_password)
            self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_req1)
            expected = self.get_error_text("password_one_lower_case")
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="profile_password_all_lower_case_letters",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach()
            raise

    @allure.feature("Update password with less than 8 chars")
    def profile_update_password_less_than_8_chars(self, old_password, new_password, confirm_password):
        try:
            self.wait_for_sync(2)
            self.click_password_link()
            # Need to comment below line - New changes in Code - No need to press Update button
            # self.update_password(old_password, new_password, confirm_password)
            self.send_text_action(old_password, ProfileXpath.old_password)
            self.send_text_action(new_password, ProfileXpath.new_password)
            self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_req1)
            expected = self.get_error_text("password_min_8_char")
            if actual == expected:
                assert True
            else:
                assert False, f"Expected was {expected} But actual is {actual} "
        except Exception as e:
            allure.attach(str(e), name="profile_password_less_than_8_chars",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach()
            raise

    @allure.feature("Read Updated password success message")
    def profile_update_password_text(self):
        try:
            self.wait_for_sync(2)
            actual = self.get_text_from_element(ProfileXpath.password_updated_success_txt)
            expected = "Password Changed Successfully!"
            if actual == expected:
                assert True
            else:
                assert False, f"Expected was {expected} But actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="profile_password_success_txt",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach()
            raise

    def update_password(self, old_password, new_password, confirm_password):
        self.send_text_action(old_password, ProfileXpath.old_password)
        self.send_text_action(new_password, ProfileXpath.new_password)
        self.send_text_action(confirm_password, ProfileXpath.new_password_confirm)
        self.mouse_click_action(ProfileXpath.save_changes)
        self.wait_for_sync(5)

    @allure.feature("Update p.o.Box with some data")
    def update_po_box(self, some_text):
        try:
            self.send_text_action(some_text, ProfileXpath.p_o_box_xpath)
            # Need to go to end of page to find the save button - new changes in Release 1.3
            self.scroll_to_end_of_page()
            self.mouse_click_action(ProfileXpath.update_info)
        except:
            self.log.info("Update of p.o.box was not successful")
            assert False

    @allure.feature("Click on save changes button")
    def click_save_change_button(self):
        try:
            self.scroll_to_end_of_page()
            self.is_button_disabled(ProfileXpath.update_info)
        except:
            self.log.info("Clicking on Save Changes was not successful")
            assert False

    @allure.feature("Update phone number with some data")
    def update_phone_number(self, phone_number):
        try:
            self.send_text_action(phone_number, ProfileXpath.phone_number_xpath)
            self.scroll_to_end_of_page()
            self.mouse_click_action(ProfileXpath.update_info)
        except:
            self.log.info("Update of phone number was not successful")
            assert False

    @allure.feature("Verify DoB, First Name, Last Name and Gender are NOT editable")
    def verify_name_gender_dob_not_editable(self):
        try:
            element = self.get_element(ProfileXpath.first_name_xpath)
            actual = element.get_attribute('readonly')
            self.log.info(f" Expected : readonly but actual is : {actual}")
            if actual == 'true':
                assert True
            else:
                assert False
            element = self.get_element(ProfileXpath.last_name_xpath)
            actual = element.get_attribute('readonly')
            self.log.info(f" Expected : readonly but actual is : {actual}")
            if actual == 'true':
                assert True
            else:
                assert False
            element = self.get_element(ProfileXpath.dob_xpath)
            actual = element.get_attribute('readonly')
            self.log.info(f" Expected : readonly but actual is : {actual}")

            if actual == 'true':
                assert True
            else:
                assert False
            element = self.get_element(ProfileXpath.gender_xpath)
            actual = element.get_attribute('disabled')
            self.log.info(f" Expected : readonly but actual is : {actual}")
            if actual == 'true':
                assert True
            else:
                assert False
        except Exception as e:
            self.log.info("First Name,Last Name are editable - Expected is disabled")
            allure.attach(str(e), name="fields_editable", attachment_type=allure.attachment_type.TEXT)
            assert False

    @allure.feature("Update mailing with some data")
    def update_mailing_address(self, someText):
        try:
            self.send_text_action(someText, ProfileXpath.address_xpath)
            self.scroll_to_end_of_page()
            self.mouse_click_action(ProfileXpath.update_info)
        except:
            self.log.info("Update of mailing was not successful")
            assert False

    @allure.feature("Verify the profile update message")
    def verify_success_msg(self):
        expected = "Profile updated successfully."
        try:
            actual = self.get_text_from_element(ProfileXpath.success_msg_xpath)
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="profile_link_po_box_update", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the profile update message NOT present as Expected")
    def verify_no_success_msg(self):
        try:
            self.verify_element_not_present(ProfileXpath.success_msg_xpath)
        except Exception as e:
            allure.attach(str(e), name="element_present_not_expected", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the error shown when no mailing address entered")
    def verify_error_shown_mailing_address(self):
        try:
            actual = self.get_text_from_element(ProfileXpath.empty_mailing_address_xpath)
            expected = self.get_error_text("empty_mailing_address")
            if actual == expected:
                assert True
            else:
                assert False, f" Expected is {expected} But actual is {actual}"
        except Exception as e:
            allure.attach(str(e), name="Mailing_address_error", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the current mailing address")
    def verify_existing_mailing_address(self):
        expected = "Sydney Road, Campbellfield VIC, Australia"
        try:
            element = self.get_element(ProfileXpath.address_xpath)
            actual = element.get_attribute('value')
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="profile_address_update", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the updated p.o box details")
    def verify_exising_po_box_data(self, expected):
        try:
            element = self.get_element(ProfileXpath.p_o_box_xpath)
            actual = element.get_attribute('value')
            self.log.info(f" Expected value is {expected} but actual is {actual}")
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="profile_address_update", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the updated phone number details")
    def verify_exising_phone_number_data(self, expected):
        try:
            element = self.get_element(ProfileXpath.phone_number_xpath)
            actual = element.get_attribute('value')
            self.log.info(f" Expected value is {expected} but actual is {actual}")
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="phone_number_data", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.feature("Verify the updated phone number details")
    def verify_exising_phone_number(self, expected):
        try:
            element = self.get_element(ProfileXpath.phone_number_xpath)
            actual = element.get_attribute('value')
            self.log.info(f" Expected value is {expected} but actual is {actual}")
            if actual == expected:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="profile_address_update", attachment_type=allure.attachment_type.TEXT)
            raise

    '''
    @allure.step("Clicking on Profile link to update password")
    def profile_update_password(self, contact_number):
        try:
            self.wait_for_sync(5)
            self.click_on_link(ProfileXpath.password)
            self.wait_for_sync(5)
            self.send_text_action(contact_number, PatientHomePageXpath.phone_number_textarea)
            self.mouse_click_action(ProfileXpath.submit_btn)
        except Exception as e:
            allure.attach(str(e), name="profile_link_po_box_update", attachment_type=allure.attachment_type.TEXT)
            raise

    
    @allure.step("Clicking on Profile link to update phone number ")
    def click_profile_update_phone_number(self, contact_number):
        try:
            self.wait_for_sync(5)
            self.click_on_link(PatientHomePageXpath.profile_link)
            self.wait_for_sync(5)
            self.send_text_action(contact_number, PatientHomePageXpath.phone_number_textarea)
            self.mouse_click_action(PatientHomePageXpath.submit_btn)
        except Exception as e:
            allure.attach(str(e), name="profile_link_po_box_update", attachment_type=allure.attachment_type.TEXT)
            raise
    '''
