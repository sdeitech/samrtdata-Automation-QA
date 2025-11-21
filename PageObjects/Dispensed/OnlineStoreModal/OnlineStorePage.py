
from PageObjects.Dispensed.OnlineStoreModal.OnlineStoreXpath import OnlineStoreXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class OnlineStorePage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on Shop Vaporiser button")
    def click_shop_vaporiser_btn(self):
        try:
            self.mouse_click_action(OnlineStoreXpath.shop_vaporiser)
        except Exception as e:
            allure.attach(str(e), name="click_shop_vaporiser_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Shop Accessories button")
    def click_shop_accessories_btn(self):
        try:
            self.mouse_click_action(OnlineStoreXpath.shop_accessories)
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

    @allure.step("Click on Close button")
    def click_close_btn(self):
        try:
            self.mouse_click_action(OnlineStoreXpath.close_btn)
        except Exception as e:
            allure.attach(str(e), name="click_close_btn_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Getting into Shops")
    def click_shop_modal(self):
        self.click_shop_vaporiser_btn()
        self.verify_shop()
        self.click_shop_accessories_btn()
        self.verify_shop()
        self.click_close_btn()








