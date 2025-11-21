from PageObjects.smartData2.Support.SupportXpath import SupportXpath
from SupportLibraries.base_helper import BaseHelpers
import allure
from PageObjects.Dispensed.SideNav.SideNavXpath import SideNavXpath

class SupportPage(BaseHelpers):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("View clicked question: {question}")
    def click_question(self, question, qpath):
        try:
            self.mouse_click_action(qpath)
        except Exception as e:
            allure.attach(str(e), name="click_question_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View Most Frequently Asked Questions of title: {cardtitle}")
    def most_asked(self, xnum, cardtitle):
        try:
            most_asked_links = self.get_element_list(SupportXpath.faq_card+"["+str(xnum)+"]"+SupportXpath.most_asked)
            for index, xpath in enumerate(most_asked_links):
                count = index + 1
                sub_link = str(SupportXpath.faq_card+"["+str(xnum)+"]"+SupportXpath.most_asked)
                self.scroll_into_element(sub_link+"["+str(count)+"]")
                self.wait_for_sync(1)
                question = self.get_element_text(sub_link+"["+str(count)+"]")
                qpath = sub_link+"["+str(count)+"]"
                self.click_question(question, qpath)
                # self.mouse_click_action(sub_link+"["+str(count)+"]")
                self.wait_for_sync(1)
                self.mouse_click_action(SideNavXpath.support)
                self.wait_for_sync(1)
            more = SupportXpath.faq_card + "[" + str(xnum) + "]" + SupportXpath.view_more
            self.view_more(more)
        except Exception as e:
            allure.attach(str(e), name="most_asked_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View Frequently Asked Questions om title: {cardtitle}")
    def faq_on(self, xnum, cardtitle):
        try:
            question_links = self.get_element_list(
                SupportXpath.faq_section + "[" + str(xnum) + "]" + SupportXpath.question_items)
            for index, xpath in enumerate(question_links):
                count = index + 1
                sub_link = str(SupportXpath.faq_section + "[" + str(xnum) + "]" + SupportXpath.question_items)
                sub_link_1 = str(SupportXpath.faq_section_1 + "[" + str(xnum) + "]" + SupportXpath.question_items)
                self.scroll_into_element(sub_link + "[" + str(count) + "]")
                question = self.get_element_text(sub_link + SupportXpath.faq_question)
                qpath = sub_link_1 + ")[" + str(count) + "]"
                self.wait_for_sync(3)
                self.click_question(question, qpath)
                # self.mouse_click_action(sub_link+"["+str(count)+"]")
                # self.wait_for_sync(1)
            # self.mouse_click_action(SideNavXpath.support)
            # self.wait_for_sync(1)
        except Exception as e:
            allure.attach(str(e), name="faq_on_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click view more")
    def view_more(self, more):
        try:
            self.mouse_click_action(more)
            faqs_sections = self.get_element_list(SupportXpath.faq_section)
            for index, xpath in enumerate(faqs_sections):
                xnum = index + 1
                cardtitle = self.get_element_text(SupportXpath.faq_section+"["+str(xnum)+"]"+SupportXpath.faq_section_title)
                self.faq_on(xnum, cardtitle)
            self.mouse_click_action(SideNavXpath.support)
        except Exception as e:
            allure.attach(str(e), name="view_more_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View all Frequently Asked Questions")
    def all_faqs(self):
        try:
            faqs_cards = self.get_element_list(SupportXpath.faq_card)
            for index, xpath in enumerate(faqs_cards):
                xnum= index + 1
                # xpaths = str(xpath)
                cardtitle = self.get_element_text(SupportXpath.faq_card+"["+str(xnum)+"]"+SupportXpath.card_title)
                self.most_asked(xnum, cardtitle)
                # more = SupportXpath.faq_card+"["+str(xnum)+"]"+ SupportXpath.view_more
                # self.view_more(more)
        except Exception as e:
            allure.attach(str(e), name="all_faqs_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("View Welcome guide PDF")
    def view_pdf(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(SupportXpath.welcome_guide)
            self.wait_for_sync(2)
            self.mouse_click_action(SupportXpath.welcome_guide)
            self.wait_for_sync(2)
            self.current_window()
        except Exception as e:
            allure.attach(str(e), name="view_pdf_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Switch iframe to Live chat frame")
    def switch_frame(self):
        try:
            self.switch_to_iframe(SupportXpath.live_chat_frame)

        except Exception as e:
            allure.attach(str(e), name="switch_frame_exception", attachment_type=allure.attachment_type.TEXT)
            raise

    @allure.step("Click on LIVE CHAT Button")
    def click_live_chat(self):
        try:
            self.wait_for_sync(2)
            self.scroll_into_element(SupportXpath.live_chat)
            self.wait_for_sync(2)
            self.mouse_click_action(SupportXpath.live_chat)
        except Exception as e:
            allure.attach(str(e), name="click_live_chat_exception", attachment_type=allure.attachment_type.TEXT)
            raise


    @allure.step("View LIVE CHAT")
    def view_live_chat(self):
        self.click_live_chat()
        self.switch_frame()

