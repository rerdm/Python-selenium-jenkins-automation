
from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_startseite.Lokatoren.lokatoren.BundID_startseite_lokatoren import BundID_startseite_lokatoren
from pages.BundID_startseite.Lokatoren.lokatoren.BundID_startseite_lokatoren_js import BundID_startseite_lokatoren_js


class BundID_startseite:
    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [20.06.2023]
    Klasse: [BundID_startseite]
    Page-Webseite: https://test.id.bund.de/de
    Diese Page besitzt Methoden, die auf die elemente der Webseite zugreifen können.
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.warte_auf_sichtbares_element = None
        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_startseite_lokatoren = BundID_startseite_lokatoren()
        self.bundID_startseite_lokatoren_js = BundID_startseite_lokatoren_js()

        # NOTWENDIGE: Hilfsklassen Instanz #############################################################################
        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

    def sprachauswahl_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_SPRACHAUSWAHL

        # Methode der Klasse wartet auf web element ####################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()
    def sprachauswahl_deutsch_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_SPRACHAUSWAHL_DEUTSCH

        # Methode der Klasse wartet auf web element ####################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()


    def hilfe_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_HILFE

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def lupe_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_LUPE

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def lupe_button_schliessen_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_LUPE_CLOSE

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def lupe_send_keys(self, keys):

        locator = self.bundID_startseite_lokatoren.LUPE_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def bundID_main_container_get_text(self):

        element_text_via_js = self.driver.execute_script(self.bundID_startseite_lokatoren_js.
                                                         LOKATOR_JS_MAIN_CONTAINER_TEXT)

        return element_text_via_js

    def anmelde_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_ANMELDEN

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def konto_erstellen_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_KONTO_ERSTELLEN

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def mehr_informationen_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_MEHR_INFORMATIONEN

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def video_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_VIDEO

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def erste_frage_was_ist_bund_id_button_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_ERSTE_FRAGE_WAS_IST_BUND_ID

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def erste_frage_was_ist_bund_id_p1_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ERSTE_FRAGE_P1

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def erste_frage_was_ist_bund_id_p2_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ERSTE_FRAGE_P2

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def erste_frage_was_ist_bund_id_p3_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ERSTE_FRAGE_P3

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def erste_frage_was_ist_bund_id_p4_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ERSTE_FRAGE_P4

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def zweite_frage_wie_erstelle_ich_ein_bundid_konto_klick(self):

        locator = self.bundID_startseite_lokatoren.BUTTON_ZWEITE_FRAGE_WIE_ERSTELLE_ICH_EIN_BUNDID_KONTO

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def zweite_frage_wie_erstelle_ich_ein_bundid_konto_p1_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ZWEITE_FRAGE_P1

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def zweite_frage_wie_erstelle_ich_ein_bundid_konto_p2_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_ZWEITE_FRAGE_P2

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def dritte_frage_wie_stelle_ich_einen_online_antrag_klick(self):

        locator = self.bundID_startseite_lokatoren.TEXT_DRITTE_FRAGE_WIE_STELLE_ICH_EIN_ONLINE_ANTRAG

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def dritte_frage_wie_stelle_ich_einen_online_antrag_get_text(self):

        locator = self.bundID_startseite_lokatoren.TEXT_DRITTE_FRAGE_WIE_STELLE_ICH_EIN_ONLINE_ANTRAG

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        return element_text

    def alle_hilfreichen_informationen_link_klick(self):

        locator = self.bundID_startseite_lokatoren.LINK_ALLE_HILFREICHE_INFORMATIONEN

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()


