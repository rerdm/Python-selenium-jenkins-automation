
from selenium.webdriver.common.by import By

class BundID_bn_anmelden_zugaenge_daten_lokatoren:

    # Fortschrittsanzeige:
    TAB_ZUGANGE_UND_DATEN = (By.XPATH, "//button[@id='tab-accessPoints']")
    TAB_KONTO_AKTIVITAETEN = (By.XPATH,"//button[@id='tab-activities']")
    TAB_POSTFACH = (By.XPATH, "//button[@id='tab-postkorb']")

    # DATEN Text-BOX ###################################################################################################
    DATEN_TEXT_BOX_P1 = (By.XPATH, "//div[@id='content-accessPoints']//section//div//h2")
    DATEN_TEXT_BOX_P2 = (By.XPATH, "//body/div[@id='app']/div/div/div/div/main/div/div/div[@id='content-accessPoints']/section/div/div/p[1]")
    DATEN_TEXT_BOX_P3 = (By.XPATH, "(//p)[16]")

    # Container Daten: #################################################################################################
    BUTTON_STIFT_PERSOENLICHEDATEN = (By.XPATH, "//button[@data-test-id='3OuwP']")
    BUTTON_ABBRECHEN_PERSOENLICHENDATEN = (By.XPATH, "//button[@data-test-id='iHj7Y']")
    BUTTON_STIFT_ADRESSE = (By.XPATH, "//button[@data-test-id='kqdNh']")
    BUTTON_ABBRECHEN_ADRESSE = (By.XPATH, "//button[@data-test-id='zHHJb']")
    BUTTON_STIFT_KONTODATEN = (By.XPATH, "//button[@data-test-id='cgesE']")
    BUTTON_ABBRECHEN_KONTODATEN = (By.XPATH, "//button[@data-test-id='eqdj5']")

    # Persoenlische Daten: #############################################################################################
    EINGABEFELD_VORNAME_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='bcLcL']")
    EINGABEFELD_NACHNAME_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='C04Cm']")
    EINGABEFELD_GEBURTSNAME_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='0EYQS']")
    EINGABEFELD_GEBURTSDATUM_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='4OgT7']")
    EINGABEFELD_GEBURTSORT_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='VMURo']")

    INPUT_GEBURTSORT_KLICK = (By.XPATH, "//input[@name='Geburtsort']")
    INPUT_VORNAME_KLICK = (By.XPATH, "//input[@name='Vorname(n)']")

    # Adresse: #########################################################################################################
    EINGABEFELD_STRASSE_HAUSNUMMER_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='zBgTZ']")
    EINGABEFELD_PLZ_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='MMnNL']")
    EINGABEFELD_ORT_MEIN_KONTO = (By.XPATH, "//input[@data-test-id='4BLSr']")
    SELECT_LAND_MEIN_KONTO_ = (By.XPATH, "//select[@data-test-id='8m6z14dropdown-select']")

    # Haekchen_Validierung: ############################################################################################
    HAEKCHEN_VORNAME_MEIN_KONTO = (By.XPATH, "//div[@datatestid='bcLcL']//*[contains(@class,'text-success')]")
    HAEKCHEN_NACHNAME_MEIN_KONTO = (By.XPATH, "//div[@datatestid='C04Cm']//*[contains(@class,'text-success')]")
    HAEKCHEN_GEBURTSNAME_MEIN_KONTO = (By.XPATH, "//div[@datatestid='0EYQS']//*[contains(@class,'text-success')]")
    HAEKCHEN_GEBURTSDATUM_MEIN_KONTO = (By.XPATH, "//div[@datatestid='4OgT7']//*[contains(@class,'text-success')]")
    HAEKCHEN_GEBURTSORT_MEIN_KONTO = (By.XPATH, "//div[@datatestid='VMURo']//*[contains(@class,'text-success')]")
    HAEKCHEN_STRASSE_HAUSNUMMER_MEIN_KONTO = (By.XPATH, "//div[@datatestid='zBgTZ']//*[contains(@class,'text-success')]")
    HAEKCHEN_PLZ_MEIN_KONTO = (By.XPATH, "//div[@datatestid='MMnNL']//*[contains(@class,'text-success')]")
    HAEKCHEN_ORT_MEIN_KONTO = (By.XPATH, "//div[@datatestid='4BLSr']//*[contains(@class,'text-success')]")

    # Kontaktdaten: ####################################################################################################
    BUTTON_INFO_TELEFONNUMMER = (By.XPATH, "//button[@class='flex cursor-pointer w-12 select-none justify-center items-center hover:text-primary text-disabled']")
    BUTTON_STIFT_KONTAKTDATEN = (By.XPATH, "//button[@data-test-id='cgesE']")
    DROPDOWN_LAENDERVORWAHL = (By.XPATH, "//select[@name='Ländervorwahl']")
    INPUT_TELEFONNUMMER = (By.XPATH, "//input[@name='Telefonnummer']")
    BUTTON_DE_MAIL_AKKOERDEON = (By.XPATH, "//button[@data-test-id='Q3N0m_disclosure-button']")
    INPUT_DE_MAIL_ADRESSE = (By.XPATH, "//input[@data-test-id='j5BsZ']")
    BUTTON_SPEICHERN_KONTAKTDATEN = (By.XPATH, "//button[@data-test-id='Z2q3K']")
    BUTTON_WEITER_KONTAKTDATEN = (By.XPATH, "//button[@data-test-id='i9lId'] ")
    BUTTON_ABBRECHEN_KONTAKDATEN = (By.XPATH, "//button[@data-test-id='eqdj5']")

    #Haekchen_Validierung_Kontaktdaten: ################################################################################
    # HAEKCHEN_TELEFONNUMMER_MEIN_KONTO = (By.XPATH, "//div[@datatestid='ubTb6']//*[contains(@class,'text-success')]")
    # HAEKCHEN_EMAIL_MEIN_KONTO = (By.XPATH, "//div[@datatestid='ATKpo']//*[contains(@class,'text-success')]")
    # HAEKCHEN_EMAIL_WIEDERHOLEN_MEIN_KONTO = (By.XPATH, "//div[@datatestid='aE6yo']//*[contains(@class,'text-success')]")
    # HAEKCHEN_DE_EMAIL_MEIN_KONTO = (By.XPATH, "//div[@datatestid='j5BsZ']//*[contains(@class,'text-success')]")

    # Zugänge ##########################################################################################################

    ZUGANG_ONLINE_AUSWEIS_BUTTON_KLICK = (By.XPATH, "//h3[normalize-space()='Online-Ausweis']")
    ZUGANG_ONLINE_ELSTER_ZERTIFIKAT_BUTTON_KLICK = (By.XPATH, "//h3[normalize-space()='ELSTER-Zertifikat']")
    ZUGANG_ONLINE_BENUTZERNAME_PASSWORT_BUTTON_KLICK = (By.XPATH, "//h3[normalize-space()='Benutzername & Passwort']")