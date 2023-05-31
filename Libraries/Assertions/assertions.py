from robot.api import logger
from assertpy import soft_assertions
from assertpy import assert_that


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
            logger.info("*****Actual******")
            logger.info(actual_result)
            assert_that(actual_result).is_empty()
