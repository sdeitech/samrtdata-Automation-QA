from selenium.common.exceptions import NoSuchElementException
from SupportLibraries.base_helper import BaseHelpers
import allure

class DummyPagess(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    unclick = "//button[@id='wLkBf']"

    @allure.step("click unclickable button")
    def unclickable(self):
        try:
            self.wait_for_sync(5)
            self.mouse_click_action(self.unclick)
        except Exception as e:
            allure.attach(str(e), name="enter_mail_address_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Set Password for new account")
    def dummy(self):
        self.unclickable()
