from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjects.Comman.TestProd.Typeform.TypeformXpath import TypeformXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class TypeformPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Switching to type form frame")
    def switching_to_type_form_frame(self):
        try:
            self.switch_to_iframe(TypeformXpath.type_form_frame)
            self.wait_for_sync(5)
        except Exception as e:
            allure.attach(str(e), name="switching_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Validating age")
    def validating_age(self):
        try:
            self.mouse_click_action(TypeformXpath.yes_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="validating_age_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Which of the following describes your relationship to cannabis:This question is required.")
    def select_relation_to_cannabis(self):
        try:
            self.mouse_click_action(TypeformXpath.i_am_new_to_cannabis_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_relation_to_cannabis_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please tick the box if any of the following are true.")
    def select_box(self):
        try:
            self.mouse_click_action(TypeformXpath.select_true_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_box_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("Selecting: Please select what you suffer from")
    def select_suffer(self):
        try:
            self.mouse_click_action(TypeformXpath.suffer_from_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_suffer_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please email a referral letter from your specialist")
    def select_referral_letter(self):
        try:
            self.mouse_click_action(TypeformXpath.click_to_proceed_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_referral_letter_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Please select any conditions or secondary conditions you are suffering from, for which you are seeking treatment.This question is required.")
    def select_suffering_condition(self):
        try:
            # self.mouse_click_action(TypeformXpath.pain_btn)
            # self.driver.find_element(By.XPATH, TypeformXpath.pain_btn).click()
            self.wait_and_click(TypeformXpath.pain_btn)
            # self.wait_and_click(TypeformXpath.pain_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_suffering_condition_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: What is your Medicare Number(optional): {medicare_number}")
    def enter_medicare_number(self, medicare_number):
        try:
            self.enter_text_action("123123", TypeformXpath.medicare_textarea)
            self.mouse_click_action(TypeformXpath.medicare_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_medicare_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Enter: Individual Reference Number (optional): {reference_number}")
    def enter_reference_number(self, reference_number):
        try:
            self.enter_text_action(reference_number, TypeformXpath.reference_textarea)
            self.mouse_click_action(TypeformXpath.reference_ok_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="enter_reference_number_exception",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Selecting: Where did you hear about us?")
    def select_where_did_you_hear_about_us(self):
        try:
            self.mouse_click_action(TypeformXpath.radio_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_where_did_you_hear_about_us_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Declaration: I have answered all questions truthfully/to the best of my knowledge.")
    def select_declaration(self):
        try:
            self.mouse_click_action(TypeformXpath.i_accept_btn)
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="select_declaration_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Switching to default frame")
    def switching_default_frame(self):
        try:
            self.switch_to_default_content()
            self.wait_for_sync(2)
        except Exception as e:
            allure.attach(str(e), name="switching_default_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Entering details into typeform")
    def enter_typeform_details(self, medicare_number, reference_number):
        self.switching_to_type_form_frame()
        self.validating_age()
        self.send_text_action(self.string_generator(),"//input[@id='dd82c182-e018-45d0-92c4-37f608fd19d9']")
        self.send_text_action(self.string_generator(), "//input[@id='d7ad48b6-ccf7-4034-9876-c8bc5b9ec985']")
        self.enter_text_action("0412 345 678", "//input[@id='fee397cc-277d-41c3-933d-b9ca72e59946']")
        self.mouse_click_action("//div[@data-qa='choice']")
        self.wait_for_sync(1)
        self.enter_text_action(self.string_generator(), "//input[@placeholder='Type your answer here...']")
        self.mouse_click_action("//div[@data-value-string='3837c3ae-1dd9-4fef-8c6e-25526475a848']")
        self.wait_for_sync(1)
        self.enter_text_action("55","//input[@placeholder='Type your answer here...']")
        self.wait_for_sync(5)
        # self.enter_text_action("155","//input[@placeholder='Type your answer here...']")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='7320fedd-9a7d-4451-90c6-3a5d732c9c69']")
        self.mouse_click_action("//div[@data-value-string='81e7f8a6-cde9-4345-93e9-af15f9d18b03']")
        self.mouse_click_action("//div[@data-value-string='3a88e9c4-63e7-4fda-ba3b-dacd8522c21f']")
        self.select_suffer()
        self.select_referral_letter()
        self.mouse_click_action("//div[@id='block-b0d66366-c8e1-448b-b67b-43d13cb70b20']//button")
        self.mouse_click_action("//div[@id='block-alternativetherapies']//button")
        self.mouse_click_action("//div[@data-value-string='b15f4a4d-8e53-4d5e-8843-d6c018034899']")
        self.wait_for_sync(2)
        self.mouse_click_action("(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]")
        self.wait_for_sync(2)
        self.mouse_click_action("//div[@data-value-string='have_any_allergies_or_sensitive_to_medicine-no']")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='89e38988-1bdc-4ecf-b4d5-d6fbf39e5d9f']")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='9b3f6e0f-be0f-4144-9a77-b629c0aa020c-yes']")
        self.wait_for_sync(1)
        self.enter_text_action("98765432101", "//textarea")
        self.wait_for_sync(1)
        self.enter_text_action("10/2030", "//input[@placeholder='Type your answer here...']")
        self.wait_for_sync(1)
        self.mouse_click_action("(//div[@role='checkbox'])[1]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//div[@role='checkbox'])[2]")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@id='block-veteranconditions']//button")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='61a86511-87eb-4c4e-886f-67e23c202bad']")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='e2599bad-c5af-4dc0-bd91-b98c75309722']")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@id='block-30323811-7406-4c65-88ac-2b50b4750712']//button")
        self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='9d399772-d076-4dca-b893-a330997c460f'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='9bfd873b-08ac-4f7b-95d8-a110a600f839'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='a727a8bd-cd53-45a6-8a17-10dc6b31b17e'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='27805cee-4e35-4084-ae9f-e1612a22aa21'])[4]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]")
        self.wait_for_sync(1)
        self.enter_text_action("Testing", "//textarea")
        self.wait_for_sync(1)
        self.mouse_click_action("//input[@placeholder='Type or select an option']")
        self.wait_for_sync(1)
        self.mouse_click_action("(//li)[4]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='8458b311-2006-4fd6-acb6-7a6c41c933b0'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='b9e5ac28-ec5f-4e46-b71c-2a54da5ba770'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='b9c08232-e1f5-413a-8ede-e465555fdeb6'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='a6b25475-4165-47c8-91c1-c2d5b42f0d6e'])[4]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='6f107cf8-b05f-4542-9c3c-e612c576e69e'])[5]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='8b727156-9056-4dc8-a86a-14610f711d08'])[6]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='69ace60c-1682-4930-886f-699af7b873a3'])[7]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]")
        self.wait_for_sync(1)
        self.enter_text_action("Testing", "//input[@placeholder='Type your answer here...']")
        self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='80964fe3-289e-4a57-9840-0562e66f9279'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='79f97fcc-e186-47bc-a708-3bdda34b6fab'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='342b7a10-1cdd-4622-9152-42f33d4815cf'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='937dcc37-9c2c-400b-b83d-f6c3b9491d20'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='704d1a31-dbcf-402c-b679-c31f23a15fa2'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='abe37c4d-4ef0-4349-9e32-9b17cafb8a3b'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='5cbffe87-14a5-4dca-aa32-ae1741666656'])[1]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]")
        self.wait_for_sync(1)


        self.mouse_click_action("(//input[@name='8b21a19b-5d1b-4783-b2ae-917e4fd7aa53'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='773432c2-52d6-4463-91f3-ea4046b0e25f'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='7ec34811-0cd0-489c-be61-7532257e9a2f'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='34d9e26d-7620-4e3c-a5ee-85bd35a5cff5'])[4]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='5090746a-466a-4237-a2d4-fa4df20e8b7c'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='aa275559-6440-4c74-ada1-0be7257fbe99'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='ad511530-c80d-4223-9dc4-45615a16fc46'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='d5bcbfae-84f1-4571-8c0d-1b331421019e'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='324f0cfb-1135-4b2e-ad47-60473e5f93b3'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='9ae2641f-f9fe-4535-9716-f1282015411f'])[4]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='b222d74a-0724-4b5e-b2de-a3b4b69f1e17'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='0f4e1d90-cfad-45da-aa01-70df704d732f'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='d0f9d164-6ad9-44ac-9ae1-1ff004141b94'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='828f75c0-e62d-4009-bf38-2b67443481de'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='89dfb0d1-0273-4e67-8e5d-f57a1c218528'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='ba6bea88-bd0f-4d3c-9dd7-eb2261e6626c'])[4]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='d86d58dc-5708-4173-88f2-a0acab57be68'])[3]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='fae724a1-5515-4b84-a4d8-b5cfe9a10376'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='902e2890-0b2f-4ae3-a8b3-719574dc77ca'])[1]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='597c6894-50e1-47ab-9aa0-43646ebcd85d'])[2]")
        # self.wait_for_sync(1)
        self.mouse_click_action("(//input[@name='acd832c2-ac23-4864-8324-eb04cb28c70d'])[3]")
        self.wait_for_sync(1)
        self.mouse_click_action("(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]")
        self.wait_for_sync(1)
        self.mouse_click_action("//div[@data-value-string='declaration_answers_2-accept']")
        self.wait_for_sync(8)




        # self.select_suffering_condition()
        #
        #
        #
        #
        # self.wait_for_sync(5)
        # self.select_relation_to_cannabis()
        # self.select_box()
        # self.select_suffer()
        # self.select_referral_letter()
        # self.select_suffering_condition()
        # self.enter_medicare_number(medicare_number)
        # self.enter_reference_number(reference_number)
        # self.select_where_did_you_hear_about_us()
        # self.select_declaration()
        # self.switching_default_frame()

