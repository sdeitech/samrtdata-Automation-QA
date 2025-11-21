"""
This module contains common reusable functions.
"""

from traceback import print_stack
from configparser import ConfigParser
from SupportLibraries.ui_helper import UIHelpers

ERROR_FILE = {}
class BaseHelpers(UIHelpers):
    """
    This class includes basic reusable base_helpers.
    """



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_properties_file(self):
        """
        This method loads the properties/ini file
        :return: this method returns config reader instance.
        """

        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read('test.ini')

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config

    def get_error_text(self,key):
        error_file_in_dict = {}
        with open("Errors.txt") as err_file:
            for each_line in err_file:
                name, var = each_line.split("=")
                error_file_in_dict[name.strip()] = var.strip()
        return error_file_in_dict[key]














