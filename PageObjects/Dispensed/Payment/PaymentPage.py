
from PageObjects.Dispensed.Payment.PaymentXpath import PaymentXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class PaymentPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on Purchase Treatment Plan button")
    def click_on_purchase_treatment_plan_btn(self):
        try:
            self.scroll_into_element(PaymentXpath.purchase_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(PaymentXpath.purchase_btn)
        except Exception as e:
            allure.attach(str(e), name="click_on_purchase_treatment_plan_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Proceed to Checkout button")
    def click_on_proceed_to_checkout_btn(self):
        try:
            self.scroll_into_element(PaymentXpath.checkout_btn)
            self.wait_for_sync(5)
            self.mouse_click_action(PaymentXpath.checkout_btn)
        except Exception as e:
            allure.attach(str(e), name="click_on_proceed_to_checkout_btn_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Next button")
    def click_next_btn(self):
        try:
            self.mouse_click_action(PaymentXpath.next_btn)
        except Exception as e:
            allure.attach(str(e), name="click_next_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Credit Card Number: {credit_card_number}")
    def enter_credit_card_number(self, credit_card_number):
        try:
            self.send_text_action(credit_card_number, PaymentXpath.card_number)
        except Exception as e:
            allure.attach(str(e), name="enter_credit_card_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Credit Card Number: {credit_card_number}")
    def enter_credit_card_number(self, credit_card_number):
        try:
            self.send_text_action(credit_card_number, PaymentXpath.card_number)
        except Exception as e:
            allure.attach(str(e), name="enter_credit_card_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Owner Name: {owner_name}")
    def enter_owner_name(self, owner_name):
        try:
            self.send_text_action(owner_name, PaymentXpath.owner)
        except Exception as e:
            allure.attach(str(e), name="enter_owner_name_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Expiry Date: {expiry_date}")
    def enter_expiry_date(self, expiry_date):
        try:
            self.send_text_action(expiry_date, PaymentXpath.expiry)
        except Exception as e:
            allure.attach(str(e), name="enter_expiry_date_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter CVV number: {cvv}")
    def enter_cvv(self, cvv):
        try:
            self.send_text_action(cvv, PaymentXpath.cvv)
        except Exception as e:
            allure.attach(str(e), name="enter_cvv_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Submit button")
    def click_submit_btn(self):
        try:
            self.mouse_click_action(PaymentXpath.next_btn)
        except Exception as e:
            allure.attach(str(e), name="click_submit_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Make payment to purchase treatment plan with valid data")
    def make_payment_to_purchase_treatment_plan_with_valid_data(self):
        self.click_on_purchase_treatment_plan_btn()
        self.click_on_proceed_to_checkout_btn()
        self.click_next_btn()
        self.click_next_btn()
        self.enter_credit_card_number("4111 1111 1111 1111")
        self.enter_owner_name("Test Owner")
        self.enter_expiry_date("11/2026")
        self.enter_cvv("420")
        self.click_submit_btn()

