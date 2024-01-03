

from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_postfach.Lokatoren.lokatoren.BundID_bn_anmelden_postfach_lokatoren import \
    BundID_bn_anmelden_postfach_lokatoren


class BundID_bn_anmelden_postfach:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [11.07.2023]
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_bn_anmelden_postfach_lokatoren = BundID_bn_anmelden_postfach_lokatoren()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def postfach_tab_klick(self):

        locator = self.bundID_bn_anmelden_postfach_lokatoren.POSTFACH_TAB

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def konto_aktivitaeten_tab_klick(self):

        locator = self.bundID_bn_anmelden_postfach_lokatoren.KONTO_AKTIVITAETEN_TAB

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def aktuelle_loging_zeitpunkt_get_text(self):

        locator = self.bundID_bn_anmelden_postfach_lokatoren.AKTUELLER_LOGIN_ZEITPUNKT_TEXT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def auto_abmeldung_popup_anmeldung_klick(self):

        locator = self.bundID_bn_anmelden_postfach_lokatoren.AUTO_LOGOUT_POPUP_ANMELDEN_BUTTON

        # Methode der Klasse wartet auf web element ####################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def abmeldung_button_klick(self):

        locator = self.bundID_bn_anmelden_postfach_lokatoren.xxx

        # Methode der Klasse wartet auf web element ####################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

