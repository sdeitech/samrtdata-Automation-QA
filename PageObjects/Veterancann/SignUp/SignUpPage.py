import random
import string
from datetime import datetime
from PageObjects.smartData2.SignUp.SignUpXpath import SignUpPageXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader

class SignUpPage(BaseHelpers):
    def __init__(self, driver, path, sheet):
        super().__init__(driver)
        self.path = path
        self.sheet = sheet

    def add_random_string_to_email(self, email):
        # Split the email address into the local part and the domain part
        local_part, domain_part = email.split('@')

        # Generate a random string of desired length (e.g., 8 characters)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        # Construct the new email address with the random string
        new_email = f"{local_part}+{random_string}@{domain_part}"

        return new_email

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        try:
            # unique_email = self.add_random_string_to_email(email)
            data_reader.set_cell_data(self.path, self.sheet, 2, 1, email)
            self.send_text_action(email, SignUpPageXpath.email)
        except Exception as e:
            allure.attach(str(e), name="enter_email_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter firstname: {firstname}")
    def enter_firstname(self, firstname):
        try:
            current_datetime = datetime.now()

            # Format date and time into string
            date_time_string = current_datetime.strftime("%Y-%m-%d")
            self.send_text_action(firstname + date_time_string, SignUpPageXpath.fname)
        except Exception as e:
            allure.attach(str(e), name="enter_firstname_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter lastname: {lastname}")
    def enter_lastname(self, lastname):
        try:
            # Get current date and time
            current_datetime = datetime.now()

            # Format date and time into string
            date_time_string = current_datetime.strftime("%H:%M:%S")
            self.send_text_action(lastname + date_time_string, SignUpPageXpath.lname)
        except Exception as e:
            allure.attach(str(e), name="enter_lastname_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter DOB: {dob}")
    def enter_dob(self, dob):
        try:
            self.send_text_action(dob, SignUpPageXpath.dob)
        except Exception as e:
            allure.attach(str(e), name="enter_DOB_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting mailing address: {address}")
    def enter_mail_address(self, address):
        try:
            self.scroll_into_element(SignUpPageXpath.mail_addr)
            self.wait_for_sync(1)
            self.send_text_action(address, SignUpPageXpath.mail_addr)
            self.wait_for_sync(1)
            self.move_to_element_and_click(SignUpPageXpath.mail_addr_list)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_mail_address_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Phone number: {phone}")
    def enter_phone_number(self, phone):
        try:
            self.send_text_action(phone, SignUpPageXpath.phone)
        except Exception as e:
            allure.attach(str(e), name="enter_phone_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Gender")
    def select_gender(self):
        try:
            self.mouse_click_action(SignUpPageXpath.male_btn)
            self.mouse_click_action(SignUpPageXpath.male_btn)
        except Exception as e:
            allure.attach(str(e), name="select_gender_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Next Step Button")
    def clicking_next_step_button(self):
        try:
            self.wait_for_sync(3)
            self.mouse_click_action(SignUpPageXpath.next_step_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_next_step_button_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Set Password: {password}")
    def enter_password(self, password):
        try:
            self.send_text_action(password, SignUpPageXpath.password)
        except Exception as e:
            allure.attach(str(e), name=" enter_password_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Set Password: {confirmation}")
    def enter_password_confirmation(self, confirmation):
        try:
            data_reader.set_cell_data(self.path, "Login", 2, 2, confirmation)
            self.send_text_action(confirmation, SignUpPageXpath.password_confirmation)
        except Exception as e:
            allure.attach(str(e), name="enter_password_confirmation_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking on Next Step Button")
    def clicking_signup_button(self):
        try:
            self.mouse_click_action(SignUpPageXpath.signup_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_signup_button_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Invalid")
    def verify_invalid_txt(self, xpath, expected):
        try:
            self.log.info(f"Starting verify_invalid with xpath: {xpath} and expected value: {expected}")
            actual = self.get_element_text(xpath)
            self.log.info(f"Actual value obtained: {actual}")

            if expected.lower() == actual.lower():
                self.log.info(f"Expected value '{expected}' matches actual value '{actual}'. Verification passed.")
                assert True
            else:
                error_message = f"Expected value '{expected}' does not match actual value '{actual}'. Verification failed."
                self.log.error(error_message)
                raise AssertionError(error_message)
        except Exception as e:
            self.log.error(f"Exception occurred in verify_invalid with xpath: {xpath} and expected value: {expected}")
            self.log.error(f"Exception details: {e}")
            allure.attach(str(e), name="verify_invalid_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Typing lower case confirm password")
    def password_wont_match(self, password,confirmation):
        self.enter_password(password)
        self.enter_password_confirmation(confirmation)
        try:
            if self.get_text_from_element(SignUpPageXpath.password_condition_message) == "The two password fields didn’t match.":
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="Entering_confirm_password",attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("To verify to Create the Patient with less than 18 years old")
    def create_account_with_less_than_18(self, email, firstname, lastname, dob):
        self.enter_email(self.add_random_string_to_email(email))
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_dob(dob)
        try:
            if self.get_text_from_element(
                    SignUpPageXpath.age_limit_text_element) == "Must be at least 18 years old to register.":
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="Entering_confirm_password",
                  attachment_type=allure.attachment_type.TEXT)

    @allure.step("Sign Up into application with email which already exists")
    def create_new_account_with_email_already_exists(self, email):
        try:
            self.enter_email(email)
            self.enter_firstname(email)
            if self.get_text_from_element(
                    SignUpPageXpath.email_exists_text_element) == "User already exists with this email id.":
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="enter_email_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify password minimum criteria set")
    def password_condition_not_met(self, password, confirmation):
        self.enter_password(password)
        self.enter_password_confirmation(confirmation)
        try:
            if self.get_text_from_element(
                    SignUpPageXpath.password_condition_message) == "The password must contain at least 1 digit, 1 uppercase letter, 1 lowercase letter, and 1 symbol.":
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="clicking_signup_button_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Disable Button")
    def verify_disable(self, xpath):
        try:
            self.is_button_disabled(xpath)
        except Exception as e:
            allure.attach(str(e), name="verify_disable_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    # @allure.step("Sign Up into application with email: {email}, firstname: {firstname}, lastname: {lastname}")
    @allure.step("Create new Account")
    def create_new_account(self, email, firstname, lastname, dob, address, phone):
        self.enter_email(self.add_random_string_to_email(email))
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_dob(dob)
        self.enter_mail_address(address)
        self.enter_phone_number(phone)
        self.select_gender()
        self.clicking_next_step_button()

    @allure.step("Set Password for new account")
    def set_password(self, password, confirmation):
        self.enter_password(password)
        self.enter_password_confirmation(confirmation)
        self.clicking_signup_button()

    @allure.step("Verify invalid")
    def verify_invalid(self, email, firstname, lastname, dob, address, phone, password, confirmation, xpath, verify,):
        self.create_new_account(email, firstname, lastname, dob, address, phone)
        self.set_password(password, confirmation)
        self.verify_invalid_txt(xpath, verify)

    @allure.step("Verify invalid")
    def verify_duplicate_email(self, email, firstname, lastname, dob, address, phone, password, confirmation, xpath, verify, ):
        self.enter_email(email)
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_dob(dob)
        self.enter_mail_address(address)
        self.enter_phone_number(phone)
        self.select_gender()
        # self.clicking_next_step_button()
        # self.set_password(password, confirmation)
        self.verify_invalid_txt(xpath, verify)

    @allure.step("Verify empty data")
    def verify_empty_data(self, email, firstname, lastname, dob, address, phone, password, confirmation):
        self.enter_email(self.add_random_string_to_email(email))
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_dob(dob)
        self.enter_mail_address(address)
        self.enter_phone_number(phone)
        self.select_gender()
        self.verify_disable(SignUpPageXpath.next_step_btn)

    @allure.step("Verify empty data")
    def verify_invalid_password(self, email, firstname, lastname, dob, address, phone, password, confirmation, xpath, verify):
        self.create_new_account(email, firstname, lastname, dob, address, phone)
        self.enter_password(password)
        self.enter_password_confirmation(confirmation)
        self.verify_invalid_txt(xpath, verify)
        self.verify_disable(SignUpPageXpath.signup_btn)


    @allure.step("Create new Account for smartData2 patient")
    def create_new_smartData2_account(self, email, dob, address):
        self.enter_email(self.add_random_string_to_email(email))
        # self.enter_firstname(firstname)
        # self.enter_lastname(lastname)
        self.enter_dob(dob)
        self.enter_mail_address(address)
        # self.enter_phone_number(phone)
        # self.select_gender()
        self.clicking_next_step_button()

    @allure.step("Create new Account for smartData2 patient with blank data")
    def create_new_smartData2_account_with_blank_data(self, email, dob, xpath):
        self.enter_email(email)
        self.enter_dob(dob)
        self.verify_disable(xpath)
