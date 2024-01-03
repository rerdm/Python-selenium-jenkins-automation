
from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_anmeldeseite.Lokatoren.lokatoren.BundID_bn_anmelden_anmeldeseite_lokatoren import \
    BundID_bn_anmelden_anmeldeseite_lokatoren


class BundID_bn_anmelden_anmeldeseite:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [05.07.2023]
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_bn_anmelden_anmeldeseite_lokatoren = BundID_bn_anmelden_anmeldeseite_lokatoren()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def passwort_vergessen_link_klick(self):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.PASSWORT_VERGESSEN_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def passwort_vergessen_link_klick_get_text(self):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.PASSWORT_VERGESSEN_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def benutzername_vergessen_link_klick(self):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.BENUTZERNAME_VERGESSEN_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def benutzername_vergessen_link_link_get_text(self):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.BENUTZERNAME_VERGESSEN_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


    def benutzername_oder_email_adresse_send_keys(self, keys):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.BENUTZERNAME_ODER_PASSWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def passwort_send_keys(self, keys):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.PASSWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def anmelde_button_klick(self):

        locator = self.bundID_bn_anmelden_anmeldeseite_lokatoren.ANMELDE_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

