

class BundID_bn_passwort_neu_setzen:

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

        # TODO
        # self.bundID_bn_passwort_neu_setzen_lokatoren = BundID_bn_passwort_neu_setzen_lokatoren()

    def neues_passwort_send_keys(self, keys):

        locator = self.bundID_bn_passwort_neu_setzen_lokatoren.NEUES_PASSWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def neues_passwort_wiederholen_send_keys(self, keys):

        locator = self.bundID_bn_passwort_neu_setzen_lokatoren.NEUERS_PASSWORT_WIEDERHOLEN_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def geheime_antwort_send_keys(self, keys):

        locator = self.bundID_bn_passwort_neu_setzen_lokatoren.GEHEIME_ANTWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def passwort_aendern_button_klick(self):

        locator = self.bundID_bn_passwort_neu_setzen_lokatoren.PASSWORT_AENDERN_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()

    def passwort_erfolgreich_geaendert_weiter_pop_up_button_klick(self):

        locator = self.bundID_bn_passwort_neu_setzen_lokatoren.PASSWORT_WURDE_ERFOLGREICH_GEAENDERT_WEITER_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()
