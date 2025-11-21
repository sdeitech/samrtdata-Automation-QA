
from PageObjects.Dispensed.Profile.ProfileXpath import ProfileXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from Utilities import data_reader

class ProfilePage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)



    @allure.step("Verify medicare number")
    def verify_medicare(self, expected):
        try:
            actual = self.get_element_text(ProfileXpath.medicare_value)
            expe = str(expected)
            print("actual: "+actual )
            print("expected :"+expe)
            if expe == actual:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_medicare_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Verify reference number")
    def verify_reference(self, expected):
        try:
            actual = self.get_element_text(ProfileXpath.reference_value)
            expe = str(expected)
            print("actual: " + actual)
            print("expected :" + expe)
            if expe == actual:
                assert True
            else:
                assert False
        except Exception as e:
            allure.attach(str(e), name="verify_reference_exception", attachment_type=allure.attachment_type.TEXT)
            raise


