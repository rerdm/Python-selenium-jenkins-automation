import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_zugaenge_daten.Lokatoren.lokatoren.BundID_bn_anmelden_zugaenge_daten_lokatoren import \
    BundID_bn_anmelden_zugaenge_daten_lokatoren
from selenium.webdriver.common.keys import Keys
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_zugaenge_daten.Lokatoren.lokatoren_cms_texte.BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen import \
    BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_zugaenge_daten.Lokatoren.lokatoren_cms_texte.BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte import \
    BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte


class BundID_bn_anmelden_zugaenge_daten:

    """
    ####################################################################################################################
    Autor: [Anna]
    Erstellt am: [02.08.2023]
    Klasse: [BundID_bn_anmelden_zugaenge_daten]
    Methoden: [...]
    Staus [TODO]
    Page-Webseite:
    Diese Page besitzt Methoden die auf die elemente der Webseite zugreifen können.
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte = BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte()

        self.bundID_bn_anmelden_zugaenge_daten_lokatoren = BundID_bn_anmelden_zugaenge_daten_lokatoren()
        self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen = BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen()



        self.wartezeit_fuer_screen_shots = waiting_time

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=webdriver_wait)

# Container_Zugänge:####################################################################################################

    def zugaenge_und_daten_tab_klick(self):

        # Warten auf das Webelement: ###################################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.TAB_ZUGANGE_UND_DATEN)

        # Aktion: ######################################################################################################
        element.click()

    def stift_persoenlichedaten_klick(self):

        # Warten auf das Webelement: ###################################################################################
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_STIFT_PERSOENLICHEDATEN)

        # Aktion: ######################################################################################################
        element.click()

# DATEN Text-Box #######################################################################################################

    def daten_text_box_get_text_p1(self):

        # Hier muss der Locator für das Webelement angegeben werden ####################################################

        locator = self.bundID_bn_anmelden_zugaenge_daten_lokatoren.DATEN_TEXT_BOX_P1  # Beispiel

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def daten_text_box_get_text_p2(self):

        # Hier muss der Locator für das Webelement angegeben werden ####################################################

        locator = self.bundID_bn_anmelden_zugaenge_daten_lokatoren.DATEN_TEXT_BOX_P2  # Beispiel

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def daten_text_box_get_text_p3(self):

        # Hier muss der Locator für das Webelement angegeben werden ####################################################

        locator = self.bundID_bn_anmelden_zugaenge_daten_lokatoren.DATEN_TEXT_BOX_P3  # Beispiel

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        # Entfernt die Zeilenumbrüche\Tabulatoren und die Leerstellen vor und nach dem String,
        # so das wirklich nur der String verglichen wird
        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


# Vorname ##############################################################################################################

    def InputTextInFeldUndGetErrorMessage(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_VORNAME_MEIN_KONTO)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)
        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_VORNAME_FEHLER)

        return error_message

    def TextLoeschenVonFeld(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_VORNAME_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_VORNAME_FEHLER)

        return error_message

    def vorname_send_keys(self, vorname):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_VORNAME_MEIN_KONTO)

        # Aktion
        element.send_keys(vorname)

    def vorname_fehler_get_text(self):

        # Warten auf das Webelement
        vorname_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_VORNAME_FEHLER)

        return vorname_fehler_get_text.text

# Nachname #############################################################################################################

    def InputTextInFeldUndGetErrorMessage_Nachname(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_NACHNAME_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_NACHNAME_FEHLER)

        return error_message

    def TextLoeschenVonFeld_Nachname(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_NACHNAME_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_NACHNAME_FEHLER)

        return error_message

    def nachname_send_keys(self, nachname):

        # warten auf Webelement
        nachname_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_NACHNAME_MEIN_KONTO)

        # Aktion
        nachname_feld.send_keys(nachname)

    def nachname_fehler_get_text(self):

        # Warten auf das Webelement
        nachname_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_NACHNAME_FEHLER)

        return nachname_fehler_get_text

#Geburtsname:

    def InputTextInFeldUndGetErrorMessage_Geburtsname(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSNAME_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSNAME_FEHLER)

        return error_message

    def TextLoeschenVonFeld_Geburtsname(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSNAME_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSNAME_FEHLER)

        return error_message

    def geburtsname_send_keys(self, geburtsname):

        geburtsname_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSNAME_MEIN_KONTO)

        geburtsname_feld.send_keys(geburtsname)

    def geburtsname_fehler_get_text(self):

        geburtsname_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSNAME_FEHLER)

        return geburtsname_fehler_get_text

# Geburtsdatum #########################################################################################################

    def InputTextInFeldUndGetErrorMessage_Geburtsdatum(self, keys):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSDATUM_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSDATUM_FEHLER)

        return error_message

    def TextLoeschenVonFeld_Geburtsdatum(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSDATUM_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSDATUM_FEHLER)

        return error_message

    def geburtsdatum_send_keys(self, geburtsdatum):

        geburtsdatum_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSDATUM_MEIN_KONTO)

        geburtsdatum_feld.send_keys(geburtsdatum)

    def geburtsdatum_fehler_get_text(self):

        # Warten auf das Webelement
        geburtsdatum_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSDATUM_FEHLER)

        return geburtsdatum_fehler_get_text

# Geburtsort ###########################################################################################################

    def InputTextInFeldUndGetErrorMessage_Geburtsort(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSORT_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSORT_FEHLER)

        return error_message

    def TextLoeschenVonFeld_Geburtsort(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSORT_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSORT_FEHLER)
        return error_message

    def geburtsort_send_keys(self, geburtsort):

        geburtsort_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_GEBURTSORT_MEIN_KONTO)

        geburtsort_feld.send_keys(geburtsort)

    def geburtsort_fehler_get_text(self):

        geburtsort_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_GEBURTSORT_FEHLER)

        return geburtsort_fehler_get_text

    def stift_adresse_klick(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_STIFT_ADRESSE)

        element.click()


# Straße, Hausnummer ###################################################################################################

    def InputTextInFeldUndGetErrorMessage_Strasse_Hausnummer(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_STRASSE_HAUSNUMMER_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_STRASSE_HAUSNUMMER_FEHLER)

        return error_message

    def TextLoeschenVonFeld_Strasse_Hausnummer(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_STRASSE_HAUSNUMMER_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_STRASSE_HAUSNUMMER_FEHLER)

        return error_message

    def strasse_und_hausnummer_send_keys(self, strasse_und_hausnummer):

        strasse_und_hausnummer_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_STRASSE_HAUSNUMMER_MEIN_KONTO)

        strasse_und_hausnummer_feld.send_keys(strasse_und_hausnummer)

    def strasse_hausnummer_fehler_get_text(self):

        strasse_hausnummer_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_STRASSE_HAUSNUMMER_FEHLER)

        return strasse_hausnummer_fehler_get_text

# PLZ ##################################################################################################################

    def TextLoeschenVonFeld_plz(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_PLZ_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_PLZFEHLER)

        return error_message

    def InputTextInFeldUndGetErrorMessage_plz(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_PLZ_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_PLZFEHLER)

        return error_message

    def postleitzahl_send_keys(self, postleitzahl):

        postleitzahl_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_PLZ_MEIN_KONTO)

        postleitzahl_feld.send_keys(postleitzahl)

    def postleitzahl_fehler_get_text(self):

        postleitzahl_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_PLZFEHLER)

        return postleitzahl_fehler_get_text

# Ort ##################################################################################################################

    def InputTextInFeldUndGetErrorMessage_Ort(self, keys):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_ORT_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_ORTFEHLER)
        return error_message

    def TextLoeschenVonFeld_Ort(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_ORT_MEIN_KONTO)

        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(Keys.TAB)

        error_message = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_ORTFEHLER)

        return error_message

    def ort_send_keys(self, ort):

        ort_feld = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.EINGABEFELD_ORT_MEIN_KONTO)

        ort_feld.send_keys(ort)

    def ort_fehler_get_text(self):

        ort_fehler_get_text = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_ORTFEHLER)

        return ort_fehler_get_text

    def button_abbrechen_klick(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_ABBRECHEN_ADRESSE)

        element.click()

    def geburtsort_input_klick(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.INPUT_GEBURTSORT_KLICK)

        element.click()

    def vorname_input_klick(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.INPUT_VORNAME_KLICK)

        element.click()



    def info_button_telefonnummer_klick(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_INFO_TELEFONNUMMER)
        time.sleep(1)

        element.click()

    def info_ihre_telefonnummer_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_IHRE_TELEFONNUMMER)

        return element

    def info_darf_folgende_zeichen_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_DARF_FOLGENDE_ZEICHEN)

        return element

    def info_darf_keine_klammern_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_DARF_KEINE_KLAMMERN)

        return element


    def info_darf_nicht_mit_einer_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_DARF_NICHT_MIT_EINER_O)

        return element

    def info_nicht_mit_einem_leerzeichen_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_DARF_NICHT_MIT_EINEM_LEERZEICHEN)

        return element

    def stift_kontakt_daten_button_klick(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_STIFT_KONTAKTDATEN)

        element.click()

    def laendervorwahl_dropdown_element_auswaehlen(self, laendervorwahl):
        # warten auf Webelement
        laendervorwahl_dropdown = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.DROPDOWN_LAENDERVORWAHL)

        # Aktion
        time.sleep(2)
        laendervorwahl_dropdown.click()

        # DropDown auswaehlen
        select_object = Select(laendervorwahl_dropdown)
        select_object.select_by_visible_text(laendervorwahl)

        laendervorwahl_dropdown.click()
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.send_keys(laendervorwahl)
        actions.perform()
        time.sleep(5)

    def telefonnummer_send_keys(self, telefonnummer):

        # warten auf Webelement
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.INPUT_TELEFONNUMMER)

        # Aktion
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(telefonnummer)


    def de_mail_akkordeon_button_klick(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_DE_MAIL_AKKOERDEON)

        element.click()


    def de_mail_adresse_send_keys(self, de_mail_adresse):

        # warten auf Webelement
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.INPUT_DE_MAIL_ADRESSE)

        # Aktion
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(de_mail_adresse)

    def speichern_button_von_kontaktdaten_klick(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_SPEICHERN_KONTAKTDATEN)

        element.click()

    def ihre_daten_erfolgreich_get_text(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte.CMS_TEXT_IHRE_DATEN_WURDEN_ERFOLGREICH)

        return element

    def weiter_button_von_kontaktdaten_klick(self):
        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_WEITER_KONTAKTDATEN)

        element.click()

    def laendervorwahl_dropdown_element_mit_Buchstabe_auswaehlen(self, laendervorwahl):
        # warten auf Webelement
        laendervorwahl_dropdown = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.DROPDOWN_LAENDERVORWAHL)

        # Aktion
        time.sleep(2)
        laendervorwahl_dropdown.send_keys(Keys.ENTER)
        laendervorwahl_dropdown.send_keys(laendervorwahl)

    def konto_aktivitaeten_tab_klick(self):


        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.TAB_KONTO_AKTIVITAETEN)

        element.click()

    def telefonnummer_fehler_get_text(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_TELEFONNUMMER_FEHLER)

        return element

    def de_mail_fehler_get_text(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren_cms_fehlermeldungen.TEXT_DE_MAIL_FEHLER)

        return element

    def button_abbrechen__kontakdaten_klick(self):

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=self.bundID_bn_anmelden_zugaenge_daten_lokatoren.BUTTON_ABBRECHEN_KONTAKDATEN)

        element.click()

