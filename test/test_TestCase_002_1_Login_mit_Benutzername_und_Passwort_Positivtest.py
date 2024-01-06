import os
import sys
import time
import pytest

########################################################################################################################
# Konfig -  Notwendig damit für den import der python module

aktuelles_verzeichnis = os.getcwd()
sys.path.append(aktuelles_verzeichnis)

########################################################################################################################


from classes.InitialisiereWebdriverSetzeZoomLevel import InitialisiereWebdriverSetzeZoomLevel

from pages.BundID_bn_anmlelden.BundID_bn_anmelden_anmeldeseite.BundID_bn_anmelden_anmeldeseite import \
    BundID_bn_anmelden_anmeldeseite
from pages.BundID_bn_anmlelden.BundID_bn_anmelden_zugaenge_daten.BundID_bn_anmelden_zugaenge_daten import \
    BundID_bn_anmelden_zugaenge_daten
from pages.BundID_bn_anmlelden.BundID_bn_anmleden_basis_page.BundID_bn_anmleden_basis_page import \
    BundID_bn_anmleden_basis_page
from pages.BundID_startseite.BundID_startseite import BundID_startseite


@pytest.fixture()
def driver():

    webdriver_initialisieren = InitialisiereWebdriverSetzeZoomLevel()
    driver = webdriver_initialisieren.get_firefox_webdriver_mit_zoom()

    yield driver
    driver.quit()

def test_TestCase_002_1_Login_mit_Benutzername_und_Passwort_Positivtest(driver):

# Globale Variablen für die Waiting times

    waiting_time = 1

# TEST-DATEN INITIALISIEREN ############################################################################################

    benutzername = "test07"
    passwort = "passwort123!"
    bundid_test_startseite_url ="https://test.id.bund.de/de"
    bundid_test_postfachseite = "https://test.id.bund.de/de/account/mailbox"

# PAGES INITIALISIEREN  ################################################################################################

    bundID_startseite = BundID_startseite(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmleden_basis_page = BundID_bn_anmleden_basis_page(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmelden_anmeldeseite = BundID_bn_anmelden_anmeldeseite(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmelden_zugaenge_daten = BundID_bn_anmelden_zugaenge_daten(
        driver=driver,
        webdriver_wait=3
    )

# VORBEDINGUNGEN #######################################################################################################

    driver.get(bundid_test_startseite_url)
    aktuelles_ergebnis = driver.current_url

    assert aktuelles_ergebnis == bundid_test_startseite_url, f"erwartetes_ergebnis: {aktuelles_ergebnis}, aktuelles_ergebnis: {bundid_test_startseite_url}"
    print("Vorbedingung erfolgreich")

# SCHRITT 2 ###########################################################################################################

    bundID_startseite.anmelde_button_klick()
    time.sleep(waiting_time)

    bundID_bn_anmleden_basis_page.benutzername_und_passwort_button_klick()
    time.sleep(waiting_time)

    bundID_bn_anmleden_basis_page.hinweis_weiter_mit_benutzername_u_passwort_popup_button_klick()
    time.sleep(waiting_time)

    # Hier wird das Erwartete mit dem aktuellen Ergebnis verglichen und reported Passed oder Failed

    erwartetes_ergebnis = "https://test.id.bund.de/de/web/login/1/Benutzername"
    aktuelles_ergebnis = driver.current_url

    assert aktuelles_ergebnis == erwartetes_ergebnis, f"erwartetes_ergebnis: {aktuelles_ergebnis}, aktuelles_ergebnis: {erwartetes_ergebnis}"

    bundID_bn_anmelden_anmeldeseite.benutzername_oder_email_adresse_send_keys(keys=benutzername)
    time.sleep(waiting_time)

    bundID_bn_anmelden_anmeldeseite.passwort_send_keys(keys=passwort)
    time.sleep(waiting_time)

    bundID_bn_anmelden_anmeldeseite.anmelde_button_klick()
    time.sleep(waiting_time)

    time.sleep(10)

    #bundID_bn_anmelden_zugaenge_daten.zugaenge_und_daten_tab_klick()
    #time.sleep(waiting_time)

    aktuelles_ergebnis = driver.current_url
    assert aktuelles_ergebnis == bundid_test_postfachseite, f"erwartetes_ergebnis: {aktuelles_ergebnis}, aktuelles_ergebnis: {bundid_test_postfachseite}"


    print("Schritt 2 erfolgreich")



def test_TestCase_002_1_Login_mit_Benutzername_und_Passwort_Negativtest(driver):

    # Globale Variablen für die Waiting times

    waiting_time = 1

# TEST-DATEN INITIALISIEREN ############################################################################################

    benutzername = "test07"
    passwort = "passwort123X!"
    bundid_test_startseite_url ="https://test.id.bund.de/de"
    bundid_test_postfachseite = "https://test.id.bund.de/de/account/mailbox"

# PAGES INITIALISIEREN  ################################################################################################

    bundID_startseite = BundID_startseite(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmleden_basis_page = BundID_bn_anmleden_basis_page(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmelden_anmeldeseite = BundID_bn_anmelden_anmeldeseite(
        driver=driver,
        webdriver_wait=3
    )

    bundID_bn_anmelden_zugaenge_daten = BundID_bn_anmelden_zugaenge_daten(
        driver=driver,
        webdriver_wait=3
    )

# VORBEDINGUNGEN #######################################################################################################

    driver.get(bundid_test_startseite_url)
    aktuelles_ergebnis = driver.current_url

    assert aktuelles_ergebnis == bundid_test_startseite_url, f"erwartetes_ergebnis: {aktuelles_ergebnis}, aktuelles_ergebnis: {bundid_test_startseite_url}"


# SCHRITT 2 ############################################################################################################

    bundID_startseite.anmelde_button_klick()
    time.sleep(waiting_time)

    bundID_bn_anmleden_basis_page.benutzername_und_passwort_button_klick()
    time.sleep(waiting_time)

    bundID_bn_anmleden_basis_page.hinweis_weiter_mit_benutzername_u_passwort_popup_button_klick()
    time.sleep(waiting_time)

    # Hier wird das Erwartete mit dem aktuellen Ergebnis verglichen und reported Passed oder Failed

    erwartetes_ergebnis = "https://test.id.bund.de/de/web/login/1/Benutzername"
    aktuelles_ergebnis = driver.current_url

    assert aktuelles_ergebnis == erwartetes_ergebnis, f"erwartetes_ergebnis: {aktuelles_ergebnis}," \
                                                      f" aktuelles_ergebnis: {erwartetes_ergebnis}"

    bundID_bn_anmelden_anmeldeseite.benutzername_oder_email_adresse_send_keys(keys=benutzername)
    time.sleep(waiting_time)

    bundID_bn_anmelden_anmeldeseite.passwort_send_keys(keys=passwort)
    time.sleep(waiting_time)

    bundID_bn_anmelden_anmeldeseite.anmelde_button_klick()
    time.sleep(waiting_time)

    time.sleep(10)

    #bundID_bn_anmelden_zugaenge_daten.zugaenge_und_daten_tab_klick()
    #time.sleep(waiting_time)

    aktuelles_ergebnis = driver.current_url

    assert aktuelles_ergebnis == bundid_test_postfachseite, f"erwartetes_ergebnis: {aktuelles_ergebnis}," \
                                                            f" aktuelles_ergebnis: {bundid_test_postfachseite}"





