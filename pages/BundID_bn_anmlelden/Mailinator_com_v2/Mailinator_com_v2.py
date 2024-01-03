import inspect
import logging
import re

from helper.Selenium_hilfs_klassen.ErstelleUndSpeicherScreenshot import ErstelleUndSpeicherScreenshot
from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.Mailinator_com_v2.Lokatoren.lokatoren.Mailinator_com_v2_lokatoren import \
    Mailinator_com_v2_lokatoren


class Mailinator_com_v2:
    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [07.06.2023]
    Klasse: [Mailinator_com]
    Page-Webseite: https://www.mailinator.com/
    Diese Page besitzt Methoden, die auf die elemente der Webseite zugreifen können.
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.erstelle_und_speichere_screen_shot = ErstelleUndSpeicherScreenshot(driver=self.driver)
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.mailinator_de_lokatoren = Mailinator_com_v2_lokatoren()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def enter_public_mailinator_inbox_send_keys(self,keys):

        locator = self.mailinator_de_lokatoren.PUBLIC_MAILINATOR_INBOX_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def go_enter_public_mailinator_button_klick(self):

        locator = self.mailinator_de_lokatoren.GO_MAILINATOR_INBOX_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def ihr_benutzername_nachricht_link_klick(self):

        try:
            locator = self.mailinator_de_lokatoren.BUND_ID_IHR_BENUTZERNAME_LINK_1
        except:
            locator = self.mailinator_de_lokatoren.BUND_ID_IHR_BENUTZERNAME_LINK_2

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def passwort_vergessen_nachricht_link_klick(self):
        try:
            locator = self.mailinator_de_lokatoren.BUND_ID_PASSWORT_VERGESSEN_LINK_1
        except:
            locator = self.mailinator_de_lokatoren.BUND_ID_PASSWORT_VERGESSEN_LINK_2

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def benutzername_nachricht_ihr_benutzername_lautet_get_text(self):

        # INDIVIDUELL für diese Methode - Zum iFrame wechseln ##########################################################
        iframe = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.mailinator_de_lokatoren.IFRAME_MAILINATOR_HTML_MSG_BODY)

        # Zu Iframe wechseln ###########################################################################################
        self.driver.switch_to.frame(iframe)

        locator = self.mailinator_de_lokatoren.IHR_BENUTZERNAME_LAUTET_TEXT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        text = element_text

        regex = r'Ihr Benutzername lautet: (\w+)'
        match = re.search(regex, text)

        if match:
            username = match.group(1)
            print("Benutzername:", username)
        else:
            username = False

        return username

    def neuens_passwort_anlegen_link_klick(self):

        # INDIVIDUELL für diese Methode - Zum iFrame wechseln ##########################################################
        iframe = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.mailinator_de_lokatoren.IFRAME_MAILINATOR_HTML_MSG_BODY)

        # Zu Iframe wechseln ###########################################################################################
        self.driver.switch_to.frame(iframe)

        locator = self.mailinator_de_lokatoren.NEUES_PASSWORT_ANLEGEN_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

        # Zurück zum ursprünglichen Frame wechseln
        self.driver.switch_to().defaultContent()

    def ihr_bund_id_verifizierungs_code_link_klick(self):

        locator = self.mailinator_de_lokatoren.IHR_BUND_ID_VERIFIZIERUNGS_CODE_LINK

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def verifizierungs_code_get_text(self):

        # INDIVIDUELL für diese Methode - Zum iFrame wechseln ##########################################################
        iframe = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.mailinator_de_lokatoren.xxxx)

        # Zu Iframe wechseln ###########################################################################################
        self.driver.switch_to.frame(iframe)

        locator = self.mailinator_de_lokatoren.VERIFIZIERUNGSCODE_TEXT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        # Zurück zum ursprünglichen Frame wechseln
        self.driver.switchTo().defaultContent()

        return element_text
