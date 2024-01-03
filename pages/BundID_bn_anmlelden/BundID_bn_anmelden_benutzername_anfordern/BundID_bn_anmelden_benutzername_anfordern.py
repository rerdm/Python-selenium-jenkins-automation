

from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_benutzername_anfordern.Lokatoren.lokatoren.BundID_bn_anmelden_benutzername_anfordern_lokatoren import \
    BundID_bn_anmelden_benutzername_anfordern_lokatoren


class BundID_bn_anmelden_benutzername_anfordern:

    """
  ####################################################################################################################
  Autor: [Rene Erdmann]
  Erstellt am: [18.07.2023]
  ####################################################################################################################
  """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_bn_anmelden_benutzername_anfordern_lokatoren = BundID_bn_anmelden_benutzername_anfordern_lokatoren()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def email_adresse_send_keys(self,keys):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.EMAIL_ADRESSE_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def geheime_antwort_send_keys(self,keys):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.GEHEIME_ANTWORT_EINGABEFELD

        # Methode der Klasse wartet auf web element ####################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def email_adresse_info_button_klick(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.EMAIL_ADRESSE_INFO_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def email_adresse_pop_get_text_p1(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.EMAIL_ADRESSE_INFO_POPUP_TEXT_P1  # Beispiel

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def email_adresse_pop_get_text_p2(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.EMAIL_ADRESSE_INFO_POPUP_TEXT_P2  # Beispiel

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


    def email_adresse_info_popup_schliessen_klick(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.EMAIL_ADRESSE_INFO_POPUP_SCHLIESSEN_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def email_adresse_info_popup_get_text(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.POP

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


    def benutzername_anfordern_button_klick(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.BENUTZERNAME_ANFORDERN_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def benutzername_anfordern_get_text(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.BENUTZERNAME_ANFORDERN_TEXT_P1

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def benutzername_anfordern_p2_text_p1(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.BENUTZERNAME_ANFORDERN_TEXT_P1

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def weiter_mit_benutzername_und_passwort_pop_up_button_klick(self):

        locator = self.bundID_bn_anmelden_benutzername_anfordern_lokatoren.\
            WEITER_MIT_BENUTZERNAME_UND_PASSWORT_POP_UP_WEITER_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()