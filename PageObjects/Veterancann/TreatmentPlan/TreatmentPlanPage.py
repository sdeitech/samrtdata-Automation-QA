import random

from PageObjects.smartData2.TreatmentPlan.TreatmentPlanXpath import TreatmentPlanXpath
from PageObjects.smartData2.PatientNote.PatientNoteXpath import PatientNoteXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class TreatmentPlan(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Enter Medicare Number: {medicare_number}")
    def enter_medicare_number(self, medicare_number):
        try:
            self.wait_for_sync(2)
            self.send_text_action(medicare_number, PatientNoteXpath.medicare_number)
        except Exception as e:
            allure.attach(str(e), name="enter_medicare_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Expiry date: {expiry_date}")
    def enter_expiry_date(self, expiry_date):
        try:
            self.wait_for_sync(2)
            self.send_text_action(expiry_date, PatientNoteXpath.expiry_date)
        except Exception as e:
            allure.attach(str(e), name="enter_expiry_date_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter Reference Number: {reference_number}")
    def enter_reference_number(self, reference_number):
        try:
            self.wait_for_sync(2)
            self.send_text_action(reference_number, PatientNoteXpath.reference_number)
        except Exception as e:
            allure.attach(str(e), name="enter_reference_number_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Select Treatment Plan button")
    def click_select_treatment_plan(self):
        try:
            self.wait_for_sync(5)
            self.scroll_into_element(TreatmentPlanXpath.select_treatment_plan_btn)
            self.wait_for_sync(4)
            self.mouse_click_action(TreatmentPlanXpath.select_treatment_plan_btn)
        except Exception as e:
            allure.attach(str(e), name="click_select_treatment_plan_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Modify Treatment Plan button")
    def click_modify_treatment_plan(self):
        try:
            self.wait_for_sync(5)
            self.scroll_into_element(TreatmentPlanXpath.modify_quantity_btn)
            self.wait_for_sync(4)
            self.mouse_click_action(TreatmentPlanXpath.modify_quantity_btn)
        except Exception as e:
            allure.attach(str(e), name="click_select_treatment_plan_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Start Treatment Plan button")
    def click_start_treatment_plan(self):
        try:
            self.wait_for_sync(5)
            self.scroll_into_element(TreatmentPlanXpath.start_treatment_plan_btn)
            self.wait_for_sync(4)
            self.mouse_click_action(TreatmentPlanXpath.start_treatment_plan_btn)
        except Exception as e:
            allure.attach(str(e), name="click_start_treatment_plan_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Confirm button")
    def click_confirm_btn(self):
        try:
            self.mouse_click_action(TreatmentPlanXpath.confirm_btn)
        except Exception as e:
            allure.attach(str(e), name="click_confirm_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Balance Oil - 30ml")
    def select_balance_oil(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_balance_oil)
        except Exception as e:
            allure.attach(str(e), name="select_balance_oil_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Select CBD Oil - 30ml")
    def select_cbd_oil(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_cbd_oil)
        except Exception as e:
            allure.attach(str(e), name="select_cbd_oil_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Hybrid 50:50 Vape Cartridge")
    def select_hybrid_vape_cart(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_hybrid_vape_cart)
        except Exception as e:
            allure.attach(str(e), name="select_hybrid_vape_cart_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Hybrid Flower")
    def select_hybrid_flower(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_hybrid_flower)
        except Exception as e:
            allure.attach(str(e), name="select_hybrid_flower_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Indica Vape Cartridge")
    def select_indica_vape_cart(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_indica_vape_cat)
        except Exception as e:
            allure.attach(str(e), name="select_indica_vape_cart_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Indica Flower")
    def select_indica_flower(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_indica_flower)
        except Exception as e:
            allure.attach(str(e), name="select_indica_flower_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Sativa Flower")
    def select_sativa_flower(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_sativa_flower)
        except Exception as e:
            allure.attach(str(e), name="select_sativa_flower_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select sativa Vape Cartridge")
    def select_sativa_vape_cart(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.select_sativa_vape_cat)
        except Exception as e:
            allure.attach(str(e), name="select_sativa_vape_cart_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Next Button")
    def click_next_btn(self):
        try:
            self.mouse_click_action(TreatmentPlanXpath.next_btn)
        except Exception as e:
            allure.attach(str(e), name="click_next_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on Update Button")
    def click_update_btn(self):
        try:
            self.mouse_click_action(TreatmentPlanXpath.update_btn)
        except Exception as e:
            allure.attach(str(e), name="click_update_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Clicking Approve button")
    def click_approve_btn(self):
        try:
            self.scroll_to_end_of_page()
            self.wait_for_sync(2)
            self.scroll_into_element(TreatmentPlanXpath.approve_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(TreatmentPlanXpath.approve_btn)
        except Exception as e:
            allure.attach(str(e), name="click_approve_btn_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    # @allure.step("Verify Login")
    # def verify_login(self, expected):
    #     try:
    #         actual = self.get_element_text(LoginPageXpath.logout_btn)
    #         if expected.lower() == actual.lower():
    #             assert True
    #         else:
    #             assert False
    #     except Exception as e:
    #         allure.attach(str(e), name="verify_login_exception", attachment_type=allure.attachment_type.TEXT)
    #         raise

    @allure.step("Select treatment plan products")
    def select_product(self):
        self.select_balance_oil(self.generate_random_number())
        self.select_cbd_oil(self.generate_random_number_cbd())
        self.select_hybrid_vape_cart(self.generate_random_number())
        self.select_hybrid_flower(self.generate_random_number())
        self.select_indica_vape_cart(self.generate_random_number())
        self.select_indica_flower(self.generate_random_number())
        self.select_sativa_flower(self.generate_random_number())
        self.select_sativa_vape_cart(self.generate_random_number())
        # self.click_update_btn()
        # self.click_approve_btn()

    @allure.step("Select smartData2 Balance Oil 10:10")
    def select_veteran_balance_oil_1010(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_balance_oil_1010)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_balance_oil_1010_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select smartData2 Balance Oil 25:25")
    def select_veteran_balance_oil_2525(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_balance_oil_2525)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_balance_oil_2525_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select smartData2 Hybrid Flower")
    def select_veteran_hybrid_flower(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_hybrid_flower)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_hybrid_flower_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Indica Flower THC")
    def select_veteran_indica_flower_thc(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_indica_flower_thc)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_indica_flower_thc_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Pure Isolate CBD100 oil(100mg/ml CBD)")
    def select_veteran_pure_isolate_cbd_100(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_pure_isolate_cbd_100)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_pure_isolate_cbd_100_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Pure Isolate CBD220 oil(220 mg/mL CBD)")
    def select_veteran_pure_isolate_cbd_220(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_pure_isolate_cbd_220)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_pure_isolate_cbd_220_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select Sativa Flower THC")
    def select_veteran_sativa_flower_thc(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_sativa_flower_thc)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_sativa_flower_thc_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select THC Oil30mL")
    def select_veteran_thc_oil(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_thc_oil)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_thc_oil_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Full-spectrum CBD100 oil")
    def select_veteran_full_spectrum_cbd_100(self, option_value):
        try:
            self.wait_for_sync(2)
            self.select_option_by_value(str(option_value), TreatmentPlanXpath.veteran_full_spectrum_cbd_100)
        except Exception as e:
            allure.attach(str(e), name="select_veteran_full_spectrum_cbd_100_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Select treatment plan products")
    def select_smartData2_product(self):
        self.select_veteran_balance_oil_1010(self.generate_random_number())
        self.select_veteran_full_spectrum_cbd_100(self.generate_random_number_cbd())
        self.select_veteran_balance_oil_2525(self.generate_random_number())
        self.select_veteran_hybrid_flower(self.generate_random_number())
        self.select_veteran_indica_flower_thc(self.generate_random_number())
        self.select_veteran_pure_isolate_cbd_100(self.generate_random_number())
        self.select_veteran_pure_isolate_cbd_220(self.generate_random_number())
        self.select_veteran_sativa_flower_thc(self.generate_random_number())
        self.select_veteran_thc_oil(self.generate_random_number())

    @allure.step("Select treatment plan product and approve")
    def select_treatment_plan(self):
        self.click_select_treatment_plan()
        self.click_confirm_btn()
        self.select_product()
        self.click_next_btn()
        self.click_approve_btn()

    @allure.step("Update treatment plan product and approve")
    def update_treatment_plan(self):
        # self.click_select_treatment_plan()
        # self.click_confirm_btn()
        self.select_product()
        self.click_next_btn()
        self.click_approve_btn()


    @allure.step("Select smartData2 treatment plan product and approve")
    def select_smartData2_treatment_plan(self, medicare_number, expiry_date, reference_number):
        self.click_select_treatment_plan()
        # self.click_confirm_btn()
        self.enter_medicare_number(medicare_number)
        self.enter_expiry_date(expiry_date)
        self.enter_reference_number(reference_number)
        self.select_smartData2_product()
        self.click_next_btn()
        self.click_approve_btn()

    def modify_treatment_plan(self):
        self.click_modify_treatment_plan()
        self.select_product()
        self.click_update_btn()
        self.click_approve_btn()



    def generate_random_number(self):
        return random.randint(0, 15)

    def generate_random_number_cbd(self):
        return random.randint(0, 9)