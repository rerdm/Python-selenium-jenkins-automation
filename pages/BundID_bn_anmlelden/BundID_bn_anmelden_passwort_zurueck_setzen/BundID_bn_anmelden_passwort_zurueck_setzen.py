
from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_passwort_zurueck_setzen.Lokatoren.lokatoren.BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren import \
    BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_passwort_zurueck_setzen.Lokatoren.lokatoren_cms_texte.BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren_cms_texte import \
    BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren_cms_texte


class BundID_bn_anmelden_passwort_zurueck_setzen:

    """
  ####################################################################################################################
  Autor: [Rene Erdmann]
  Erstellt am: [28.06.2023]
  ####################################################################################################################
  """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren = BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren()
        self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren_cms_texte =\
            BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren_cms_texte()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def benutzername_oder_email_adresse_send_keys(self, keys):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.BENUTZERNAME_ODER_EMAIL_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def geheime_antwort_send_keys(self, keys):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.GEHEIME_ANTWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def benutzername_oder_email_adresse_info_button_klick(self):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.BENUTZERNAME_ODER_EMAIL_INFO_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def benutzername_oder_email_adresse_info_popup_schliessen_klick(self):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.\
            BENUTZERNAME_ODER_EMAIL_INFO_POPUP_SCHLIESSEN_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def passwort_zuruecksetzen_button_klick(self):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.PASSWORT_ZUREUCKSETZEN_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def passwort_zurueck_setzen_bestaetigen_weiter_button_klick(self):

        locator = self.bundID_bn_anmelden_passwort_zurueck_setzen_lokatoren.PASSWORT_ZURUECKSETZEN_POP_UP_WEITER_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()