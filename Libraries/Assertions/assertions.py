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

    def verify_is_not_equal(self, actual_result, expected_result):
        """Asserts the actual is not equal to expected ignoring params"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(actual_result).is_not_equal_to(expected_result)

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

    def verify_a_list_does_not_contain(self, result_list, not_contain_element):
        """Asserts the expected does not contain the list of actual"""
        with soft_assertions():
            logger.info("*****Element not included******")
            logger.info(not_contain_element)
            logger.info("*****Actual******")
            logger.info(result_list)
            assert_that(result_list).does_not_contain(not_contain_element)

    def verify_a_list_is_empty(self, actual_result):
        """Asserts the expected does not contain of actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info("[]")
            logger.info('*****Actual******')
            logger.info(actual_result)
            assert_that(actual_result).is_empty()

    def verify_element_is_displayed(self, element: WebElement):
        """Verifies the element is displayed"""
        is_displayed = element.is_displayed()
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(f"Element {element} displayed: ", True)
            logger.info("*****Actual******")
            logger.info(f"Element {element} displayed: ", is_displayed)
            assert_that(is_displayed).is_true()

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

    def verify_element_is_not_displayed(self, element: WebElement):
        """Verifies the element is not displayed"""
        is_displayed = element.is_displayed()
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(f"Element {element} displayed: ", False)
            logger.info("*****Actual******")
            logger.info(f"Element {element} displayed: ", is_displayed)
            assert_that(is_displayed).is_false()

    def verify_a_dictionary_contains_key(self, expected_result, actual_result):
        """Asserts the expected contains the dictionary of the actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_result)
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(expected_result).contains_key(actual_result)

    def verify_the_element_exist(self,expected_instance, actual_instance):
        """Asserts the object is instance of a class"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info(expected_instance)
            logger.info("*****Actual******")
            logger.info(actual_instance)
            assert_that(actual_instance).is_instance_of(expected_instance)

    def verify_a_list_is_not_empty(self, actual_result):
        """Asserts the expected does not contain of actual"""
        with soft_assertions():
            logger.info("*****Expected******")
            logger.info("[]")
            logger.info('*****Actual******')
            logger.info(actual_result)
            assert_that(actual_result).is_not_empty()
