
from PageObjects.Comman.Login.LoginXpath import LoginPageXpath
from SupportLibraries.base_helper import BaseHelpers
from Utilities import data_reader
import allure

class LoginPage(BaseHelpers):
    def __init__(self, driver, path, sheet):
        super().__init__(driver)
        login_data = data_reader.get_data_from_excel(path, sheet)
        self.username = login_data[0][0]
        self.password = login_data[0][1]

    @allure.step("Click on Log In Now")
    def click_login_now(self):
        try:
            self.mouse_click_action(LoginPageXpath.log_in_now_link)
        except Exception as e:
            allure.attach(str(e), name="click_login_now_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter email address: {email}")
    def enter_email_address(self, email):
        try:
            self.send_text_action(email, LoginPageXpath.email_address)
        except Exception as e:
            allure.attach(str(e), name="enter_email_address_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter password: {password}")
    def enter_password(self, password):
        try:
            self.send_text_action(password, LoginPageXpath.password)
        except Exception as e:
            allure.attach(str(e), name="enter_password_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking Login Button")
    def clicking_on_login(self):
        try:
            self.mouse_click_action(LoginPageXpath.login_btn)
        except Exception as e:
            allure.attach(str(e), name="clicking_on_login_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking Logout Button")
    def clicking_on_logout(self):
        try:
            self.mouse_click_action(LoginPageXpath.login_link)
        except Exception as e:
            allure.attach(str(e), name="clicking_on_logut_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify Login")
    def verify_login(self, expected):
        try:
            actual = self.get_element_text(LoginPageXpath.logout_btn)
            if expected.lower() == actual.lower():
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_login_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Back to Login")
    def logout_and_login(self):
        try:
            self.wait_for_sync(2)
            # self.mouse_click_action(LoginPageXpath.login_link)
            self.clicking_on_logut()
            self.enter_email_address(self.username)  # Use instance variable self.username
            self.enter_password(self.password)  # Use instance variable self.password
            self.clicking_on_login()
            self.verify_login("Logout")
            allure.attach(self.driver.get_screenshot_as_png(), name="logout_and_login",
                          attachment_type=allure.attachment_type.PNG)
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="error_logout_and_login",
                          attachment_type=allure.attachment_type.PNG)
            self.log.error("Exception occurred while Login and Logout")

    @allure.step("Login into the application")
    def login_into_application(self):
        self.click_login_now()
        self.enter_email_address(self.username)  # Use instance variable self.username
        self.enter_password(self.password)  # Use instance variable self.password
        self.clicking_on_login()
        self.verify_login("Logout")

    @allure.step("Verify wrong Login")
    def wrong_login(self):
        expected = "Password incorrect - Please enter a correct email address and password. Note that password is case-sensitive."
        self.click_login_now()
        self.enter_email_address(self.username)  # Use instance variable self.username
        self.enter_password(self.password)  # Use instance variable self.password
        self.clicking_on_login()
        self.verify_validation_text(LoginPageXpath.wrong_login, expected)

    def login_with_given_password(self,password):
        self.enter_email_address(self.username)  # Use instance variable self.username
        self.enter_password(password)  # Use instance variable self.password
        self.clicking_on_login()
        self.wait_for_sync(10)
        #self.verify_login("Logout")
