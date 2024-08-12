from selenium.common import NoSuchElementException

from Utilities.GenericMethod import genericmethod
from Utilities.customLogger import LogGen

myLogger = LogGen.loggeen()


class assertion:

    def __init__(self, driver):
        self.driver = driver
        self.genericMethod = genericmethod(driver)

    # * Verify Value Equals
    # * @param expectedValue
    # * @param actualValue
    def verifyEquals(expectedValue, actualValue):
        myLogger.info("************** Verifying Expexted Equals to Actual ***************")
        if actualValue == expectedValue:
            assert True
            myLogger.info(actualValue)
            myLogger.info("****** Value matched ******")
        else:
            myLogger.info("****** Value not matched--> Action failed ******")

    # * Verify Value not Equals
    # * @param expectedValue
    # * @param actualValue
    def verifyNotEquals(expectedValue, actualValue):
        myLogger.info("************** Verifying Expexted Not Equals to Actual***************")
        if actualValue != expectedValue:
            assert True
            myLogger.info(actualValue)
            myLogger.info("****** Value not matched ******")
        else:
            assert False
            myLogger.info("****** Value matched--> Action failed ******")

    # * Waiting for element to be displayed
    # * @param element
    # * @param elementname
    def verifyElementDisplayed(element, elementname):
        myLogger.info("************** Verifying Elementname is displayed in page ***************")
        if (element.is_displayed()):
            assert True
            myLogger.info("Elementname is displayed in page")
        else:
            assert False
            myLogger.info("Elementname is not displayed in page")

    # * Waiting for element to be present
    # * @param element
    # * @param elementname
    def verifyElementPresent(element, elementname):
        myLogger.info("************** Verifying Elementname is present in webpage ***************")
        if (element.isPresent()):
            assert True
        else:
            assert False
            myLogger.info("Elementname is not present in webpage")

    def is_element_present(self, element, value):
        myLogger.info("************** Verifying Elementname is present in webpage ***************")
        try:
            self.driver.find_element(element)
            return True
        except NoSuchElementException:
            return False

    def check_element_present(context, selector):
        # context.web_drivers = {}
        # driver = context.web_drivers['main']
        element_present = context.is_element_present(context.driver, selector)
        assert element_present, f"Element with '{selector}' should be present, but it's not"
