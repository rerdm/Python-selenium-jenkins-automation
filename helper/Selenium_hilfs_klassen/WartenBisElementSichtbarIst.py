import sys
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BundID_startseite.Lokatoren.lokatoren.BundID_startseite_lokatoren import BundID_startseite_lokatoren

class WartenBisElementSichtbarIst:

    def __init__(self, driver, waiting_time):

        self.driver = driver
        self.waiting_time = waiting_time

    def sichtbares_element_gefunden(self, locator):

        try:
            element = WebDriverWait(self.driver, self.waiting_time).until(EC.visibility_of_element_located(locator))
            return element

        except:
            return False


