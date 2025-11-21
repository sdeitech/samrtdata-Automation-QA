
from PageObjects.smartData2.ClinicalNote.ClinicalNoteXpath import ClinicalNoteXpath
from SupportLibraries.base_helper import BaseHelpers
import allure

class ClinicalNotesPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on Add Clinical Note")
    def click_add_clinical_note(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(ClinicalNoteXpath.add_clinical_note_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(ClinicalNoteXpath.add_clinical_note_btn)
        except Exception as e:
            allure.attach(str(e), name="enter_DOB_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Add Description inside clinical note textarea: {description}")
    def enter_description(self, description):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(ClinicalNoteXpath.clinical_note_textarea)
            self.wait_for_sync(2)
            self.send_text_action(description, ClinicalNoteXpath.clinical_note_textarea)
        except Exception as e:
            allure.attach(str(e), name="enter_description_exception", attachment_type=allure.attachment_type.TEXT)
            raise
    @allure.step("Clicking on Save button")
    def click_on_save(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(ClinicalNoteXpath.save_btn)
            self.wait_for_sync(2)
            self.mouse_click_action(ClinicalNoteXpath.save_btn)
        except Exception as e:
            allure.attach(str(e), name="click_on_save_exception", attachment_type=allure.attachment_type.TEXT)
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


    def create_clinical_note(self, description):
        self.click_add_clinical_note()
        self.enter_description(description)
        self.click_on_save()
