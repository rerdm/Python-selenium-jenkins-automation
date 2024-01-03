import inspect
import logging

from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst

from pages.BundID_bn_anmlelden.BundID_bn_anmelden_konto_aktivitaeten.Lokatoren.lokatoren.BundID_bn_anmelden_konto_aktivitaeten_lokatoren import \
    BundID_bn_anmelden_konto_aktivitaeten_lokatoren
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_konto_aktivitaeten.Lokatoren.lokatoren.BundID_bn_anmelden_konto_aktivitaeten_lokatoren_js import \
    BundID_bn_anmelden_konto_aktivitaeten_lokatoren_js


class BundID_bn_anmelden_konto_aktivitaeten:
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

        self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren = BundID_bn_anmelden_konto_aktivitaeten_lokatoren()
        self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren_js = BundID_bn_anmelden_konto_aktivitaeten_lokatoren_js()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)


    def naechste_nachricht_button_klick(self):

        locator = self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.NAECHSTER_SEITE_BUTTON_TEXT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        if element.text == "Nächste Seite":

            locator = self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.NAECHSTE_NACHRICHT_BUTTON

            element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
                locator=locator)

            element.click()
    def weiter_bis_zur_letzten_nachricht_button_klick(self, step_number=None,
                                                      abs_pfad_zum_test_ausfuerhungs_ordner=None,
                                                      screen_shot=False,
                                                      einzelner_schritt=False,
                                                      screenshot_vor_der_aktion=None,
                                                      screenshot_nach_der_aktion=None,
                                                      scroll=False):

        # Iterieren auf die Nächsten seite #############################################################################

        for i in range(1, 70):

            # Wartet auf das Webelement ################################################################################

            naechstest_seite_verfuegbar = WartenBisElementSichtbarIst(
                driver=self.driver,
                waiting_time=self.webdriver_wait

            ).sichtbares_element_gefunden(locator=self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.NAECHSTER_SEITE_BUTTON_TEXT)

            try:
                naechstest_seite_verfuegbar.text

                if naechstest_seite_verfuegbar.text == "Nächste Seite":

                    locator = self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.NAECHSTE_NACHRICHT_BUTTON

                    methoden_name = inspect.currentframe().f_code.co_name
                    logging.info("Method executed : " + str(methoden_name))

                    # Diese Methode kann screenshots machen und auf ein element klicken.
                    # Je nach einstellung kann das Screenshot setting konfiguriert werden
                    #webelement_element_klick_plus_screenshots = WebelementElementKlickPlusScreenShots()
                    #webelement_element_klick_plus_screenshots.element_klick(
                     #   driver=self.driver,
                      #  methoden_name=methoden_name,
                       # locator=locator,
                     #   #webdriver_wait=self.webdriver_wait,
                     #   waiting_time=self.waiting_time,
                     #   step_number=step_number,
                     #   abs_pfad_zum_test_ausfuerhungs_ordner=abs_pfad_zum_test_ausfuerhungs_ordner,
                     #   screen_shot=screen_shot,
                     #   einzelner_schritt=einzelner_schritt,
                     #   screenshot_vor_der_aktion=screenshot_vor_der_aktion,
                     #   screenshot_nach_der_aktion=screenshot_nach_der_aktion,
                     #   scroll=scroll
                    #)

                else:
                    break
            except:
                break

    def anmeldung_mit_benutzername_und_passwort_kontoaktivitaet_get_text(self):

        element_text_via_js = self.driver.execute_script(self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren_js.
                                                         ANMELDUNG_MIT_BENUTZERNAME_UND_PASSWORT_NACHRICHT)

        return element_text_via_js

    def konto_wurde_erfolgreich_erstellt_get_text(self):

        element_text_via_js = self.driver.execute_script(
            self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren_js.
            KONTO_WURDE_ERSTELLT_NACHRICHT
        )

        return element_text_via_js

    def passwort_wurde_erfolgreich_zurueck_gesetzt_get_text(self):

        element_text_via_js = self.driver.execute_script(
            self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren_js.
            PASSWORT_WURDE_ERFOLGREICH_ZURUECK_GESETZT_LETZTER_EINTRAG
        )

        return element_text_via_js

    def sitzung_ist_abgelaufen_abmeldung_ist_erfolgt_nachricht_get_text(self):

        element_text_via_js = self.driver.execute_script(
            self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren_js.
            SITZUNG_IST_ABGELAUFEN_AUTOMATISCHE_ABMELDUNG_ERFOLGT_NACHRICHT
        )

        return element_text_via_js

    def telefon_nummer_geaendert_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.CMS_TEXT_TELEFONNUMMER_GEAENDERT)
        element = element
        return element

    def de_mail_geaendert_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_konto_aktivitaeten_lokatoren.CMS_TEXT_DE_MAIL_GEAENDERT)
        element = element
        return element