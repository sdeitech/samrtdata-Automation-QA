import allure
import pytest

from smartData1.BaseTest import BaseTest
from PageObjects.Comman.Calendly.CalendlyPage import CalendlyPage
from PageObjects.Comman.Login.LoginPage import LoginPage
from PageObjects.smartData1.NurseDashboard.NurseDashboardPage import NurseDashboardPage
from PageObjects.Comman.SignUp.SignUpPage import SignUpPage
from PageObjects.smartData1.Typeform.TypeformPage import TypeformPage
from Utilities import data_reader

# Initialize with random numbers for count of consults, so when it updates in test, it does update real numbers
before_upcoming_consults_number = 25
after_upcoming_consults_number = 20
before_missed_consults_number = 25
after_missed_consults_number = 20
before_patient_status = "test"
after_patient_status = "test"
before_team_consults_number = 100
after_team_consults_number = 10

''' Create this method as static and can be called when needed '''
def update_consults_number(nurse_page):
    global after_upcoming_consults_number
    after_upcoming_consults_number = nurse_page.get_upcoming_consults_number()
    global after_missed_consults_number
    after_missed_consults_number = nurse_page.get_missed_consults_number()
    global after_team_consults_number
    after_team_consults_number = nurse_page.get_team_consults_number()


class TestNurseUpcomingConsult(BaseTest):

    @pytest.mark.smoke
    @pytest.mark.dependency(name='first', scope='class')
    @pytest.mark.run(order=2)
    @allure.title("TC_Upcoming_Appointment_002, smartData1-708 :To verify the fresh appointment status is 'Awaiting "
                  "Approval' by default.")
    @pytest.mark.parametrize("email, firstname, lastname, dob, addr, phone, password, confirm, medicare_number, "
                             "reference_number",
                             data_reader.get_data_from_excel("TestData/smartData1/PatientNurse.xlsx", "SignUp3"))
    def test_upcoming_patient_status(self, email, firstname, lastname, dob, addr, phone, password, confirm,
                                     medicare_number, reference_number):
        try:
            self.nurse_login_update_consults_number()
            self.signup_new_patient_and_logout(addr, confirm, dob, "test1@yopmail.com", firstname, lastname,
                                               medicare_number,
                                               password, phone,
                                               reference_number)

            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)

            update_consults_number(nurse_page)

            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp3", 2,
                                               1)
            nurse_page.search_consultations(email_id)
            nurse_page.verify_patient_nurse_row_header("TestData/smartData1/PatientNurse.xlsx", "SignUp3")
        except:
            assert False


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=['first'], scope='class')
    @pytest.mark.run(order=3)
    @allure.title("TC_Upcoming_Appointment_003, smartData1-708 :To verify new tag is attached with patient name who's "
                  "new to system.")
    def test_new_image_for_new_patient(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp3", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.verify_new_image_present()
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=['first'], scope='class')
    @allure.title("TC_Upcoming_Appointment_004, smartData1-708 :To verify the sidebar upcoming appointment counter "
                  "updates (increases) when a new appointment is added to the list.")
    def test_upcoming_consult_number(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            current_consult_number = nurse_page.get_upcoming_consults_number()
            global before_upcoming_consults_number
            if int(current_consult_number) == (int(before_upcoming_consults_number) + 1):
                assert True
            else:
                assert False, f"The current consult number is : {current_consult_number} and global value is {before_upcoming_consults_number}"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    @pytest.mark.dependency(depends=['first'], scope='class')
    @allure.title("TC_Upcoming_Appointment_005, smartData1-708 :To verify the sidebar upcoming appointment counter "
                  "updates (decreases) when a new appointment is removed from the list.")
    def test_upcoming_consult_number_decreases(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            current_consult_number = nurse_page.get_upcoming_consults_number()
            global after_upcoming_consults_number
            if int(current_consult_number) == int(after_upcoming_consults_number):
                assert True
            else:
                assert False, f"The current consult number is : {current_consult_number} and global value is {after_upcoming_consults_number-1}"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.dependency(depends=['first'], scope='class')
    @pytest.mark.run(order=7)
    @allure.title("TC_Upcoming_Appointment_007, smartData1-708 :To verify appointments get removed when clicking on "
                  "the missed appointment button.")
    def test_upcoming_consult_reduced_after_clicking_missed(self):
        try:
            nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
            nurse_login.login_into_application()
            nurse_page = NurseDashboardPage(self.driver)
            global before_missed_consults_number
            before = nurse_page.get_missed_consults_number()
            before_missed_consults_number = before
            nurse_page.log.info(f"Before Missed consult number {before}")
            email_id = nurse_page.get_email_id("TestData/smartData1/PatientNurse.xlsx", "SignUp3", 2, 1)
            nurse_page.search_consultations(email_id)
            nurse_page.mark_as_missed()
            actual = nurse_page.get_missed_consults_number()
            if (int(before) + 1) == int(actual):
                assert True
            else:
                assert False, f"Expected was {before} + 1 but actual is {actual}"
        except:
            assert False

    @pytest.mark.smoke
    @pytest.mark.dependency(depends=['first'], scope='class')
    @pytest.mark.run(order=8)
    @allure.title("TC_Upcoming_Appointment_008, smartData1-708 :To verify the sidebar upcoming appointment counter "
                  "updates (decreases) when clicking on the missed appointment button.")
    def test_upcoming_consult_decreased_after_clicking_missed(self):
        try:
            global after_upcoming_consults_number
            nurse_page = NurseDashboardPage(self.driver)
            actual = nurse_page.get_upcoming_consults_number()
            if (int(after_upcoming_consults_number)-1) == int(actual):
                assert True
            else:
                assert False, f"Expected was {after_upcoming_consults_number} - 1 but actual is {actual}"
        except:
            assert False


    @pytest.mark.smoke
    @pytest.mark.dependency(depends=['first'], scope='class')
    @pytest.mark.run(order=9)
    @allure.title("TC_Upcoming_Appointment_009, smartData1-708 :To verify the sidebar missed appointment counter "
                  "updates (increases) when clicking on the missed appointment button.")
    def test_missed_consult_increased_after_clicking_missed(self):
        try:
            global before_missed_consults_number
            nurse_page = NurseDashboardPage(self.driver)
            actual = nurse_page.get_missed_consults_number()
            if (int(before_missed_consults_number)+1) == int(actual):
                assert True
            else:
                assert False, f"Expected was {before_missed_consults_number} + 1 but actual is {actual}"
        except:
            assert False

    def signup_new_patient_and_logout(self, addr, confirm, dob, email, firstname, lastname, medicare_number, password,
                                      phone,
                                      reference_number):
        signup_page = SignUpPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "SignUp3")
        signup_page.create_new_account(email, firstname, lastname, dob, addr, phone)
        signup_page.set_password(password, confirm)
        typeform_page = TypeformPage(self.driver)
        typeform_page.enter_typeform_details(medicare_number, reference_number)
        calendly_page = CalendlyPage(self.driver)
        calendly_page.calendly_book_appointment()
        calendly_page.logout()
        calendly_page.navigate_to_signup_page()

    def nurse_login_update_consults_number(self):
        nurse_login = LoginPage(self.driver, "TestData/smartData1/PatientNurse.xlsx", "Nurse_Login")
        nurse_login.login_into_application()
        nurse_page = NurseDashboardPage(self.driver)
        global before_upcoming_consults_number
        global before_missed_consults_number
        global before_team_consults_number
        before_upcoming_consults_number = nurse_page.get_upcoming_consults_number()
        before_missed_consults_number = nurse_page.get_missed_consults_number()
        before_team_consults_number = nurse_page.get_team_consults_number()
        nurse_page.logout()
        nurse_page.navigate_to_signup_page()
