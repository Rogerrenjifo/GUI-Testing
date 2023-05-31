from robot.api import logger
from assertpy import soft_assertions
from assertpy import assert_that
from selenium.webdriver.remote.webelement import WebElement


class Verification(object):
    """A Verification class"""

    def verify_equal_ignore(self, actual_result, expected_result, list_ignore=[]):
        """Asserts the actual is equal to expected ignoring params"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            logger.info(f"Are ignored: {list_ignore}")
            assert_that(actual_result).is_equal_to(expected_result, ignore=list_ignore)

    def verify_is_not_equal_ignore(self, actual_result, expected_result, list_ignore=[]):
        """Asserts the actual is not equal to expected ignoring params"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            logger.info(f"Are ignored: {list_ignore}")
            assert_that(actual_result).is_not_equal_to(expected_result, ignore=list_ignore)

    def verify_subset(self, expected_result, actual_result):
        """Asserts the expected is subset of actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(expected_result).is_subset_of(actual_result)

    def verify_a_dictionary_does_not_contain(self, expected_result, actual_result):
        """Asserts the expected does not contain the dictionary of the actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(expected_result).does_not_contain_key(actual_result)

    def verify_a_list_does_not_contain(self, expected_result, actual_result):
        """Asserts the expected does not contain the list of actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(expected_result).does_not_contain(actual_result)

    def verify_a_list_contains(self, elements_list, item):
        """Asserts the expected does not contain of actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(elements_list)
            logger.info("*****Actual******")
            logger.info(item)
            assert_that(elements_list).contains(item)

    def verify_all_elements_are_different(self, element_list):
        """Verifies all the elements in a list are different"""
        element_set = list(set(element_list))
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(element_set.sort())
            logger.info("*****Actual******")
            logger.info(element_list.sort())
            assert_that(element_list.sort()).is_equal_to(element_set.sort())

    def element_should_be_displayed(self, element: WebElement):
        """Verifies the element is displayed"""
        with soft_assertions():
            is_displayed = element.is_displayed()
            logger.info("*****Expected******")
            logger.info(f"Element {element} displayed: ", True)
            logger.info("*****Actual******")
            logger.info(f"Element {element} displayed: ", is_displayed)
            assert_that(is_displayed).is_true()
