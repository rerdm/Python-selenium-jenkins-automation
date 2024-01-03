import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class AllgemeineSeleniumHilfsKlassen:

    def __init__(self, driver):

        self.driver_path_version_14 = None
        self.driver_path_version_13 = None
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def find_element(self, locator):

        return self.driver.find_element(*locator)

    def scroll_to_element(self, element):

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_element_plus_50_pixel(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_down(50)

    def scroll_to_element_plus_100_pixel(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.scroll_down(100)

    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")


