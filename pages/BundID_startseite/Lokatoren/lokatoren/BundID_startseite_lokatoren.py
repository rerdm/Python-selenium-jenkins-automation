from selenium.webdriver.common.by import By


class BundID_startseite_lokatoren:

    """
    BUTTON_ elemente werden benötigt, um das Webelement zu drücken.
    TEXT_ elemente werden genutzt, um den SMC zuzugreifen, der sich in dem Webelement befindet
    VIEW_ element sind hilfselement sie werden können CreateScreenShotFromWebelement übergeben werden, um genau dieses
    element zu fotografieren
    """

    # Header
    BUTTON_LUPE = (By.XPATH, "//button[@data-test-id='e2kgi']")
    BUTTON_LUPE_CLOSE = (By.XPATH, "//div[@role='search']//div//button//*[name()='svg']")
    BUTTON_HILFE = (By.XPATH, "//a[@data-test-id='xz6zp']")
    BUTTON_SPRACHAUSWAHL = (By.XPATH, "//button[@data-test-id='tn6PN']")
    BUTTON_SPRACHAUSWAHL_DEUTSCH = (By.XPATH, "//label[@for='de']")
    LUPE_EINGABEFELD = (By.XPATH, "//input[@placeholder='Suchbegriff eingeben']")

    # MainContainer Bund ID - Ihr zugang zur digitalen Verwaltung
    VIEW_BUNDID_MAIN_CONTANINER = (By.XPATH, "//h2[@class='text-h1 content-a mb-10']")
    BUTTON_ANMELDEN = (By.XPATH, "//button[@data-test-id='8dJvk']")
    BUTTON_KONTO_ERSTELLEN = (By.XPATH, "//button[@data-test-id='T21lr']")
    BUTTON_MEHR_INFORMATIONEN = (By.XPATH, "//a[@data-test-id='cFvZN']")
    BUTTON_VIDEO = (By.ID, "JI2jH")
    BUTTON_VIDEO_COOKIES_YOUTUBE = (By.XPATH,"//button[@aria-label='Accept the use of cookies and other data for the "
                                             "purposes described']//div[2]")

    # Hilfreiche Informationen Container
    BUTTON_ERSTE_FRAGE_WAS_IST_BUND_ID = (By.XPATH, "//button[@data-test-id='5kZ4i_0_disclosure-button']")
    TEXT_ERSTE_FRAGE_P1 = (By.XPATH, "//p[contains(text(),'Die BundID bietet Ihnen ein zentrales Konto zur Id')]")
    TEXT_ERSTE_FRAGE_P2 = (By.XPATH, "//p[contains(text(),'Sie erhalten alle Bescheide und Nachrichten in Bez')]")
    TEXT_ERSTE_FRAGE_P3 = (By.XPATH, "//p[contains(text(),'Alle Online-Anträge finden Sie schnell und übersic')]")
    TEXT_ERSTE_FRAGE_P4 = (By.XPATH, "//p[contains(text(),'Weitere Informationen finden Sie im Abschnitt')]")

    BUTTON_ZWEITE_FRAGE_WIE_ERSTELLE_ICH_EIN_BUNDID_KONTO = (By.XPATH, "//button[@data-test-id='5kZ4i_1_disclosure"
                                                                       "-button']")
    TEXT_ZWEITE_FRAGE_P1 = (By.XPATH, "//p[contains(text(),'Um ein BundID-Konto zu erstellen, müssen Sie zunäc')]")
    TEXT_ZWEITE_FRAGE_P2 = (By.XPATH, "//p[normalize-space()='Es gibt vier Möglichkeiten zur Konto-Erstellung:']")
    TEXT_ZWEITE_FRAGE_P3 = (By.XPATH, "//li[normalize-space()='Benutzername & Passwort']")
    TEXT_ZWEITE_FRAGE_P4 = (By.XPATH, "//li[normalize-space()='Online-Ausweis']")
    TEXT_ZWEITE_FRAGE_P5 = (By.XPATH, "//li[normalize-space()='ELSTER-Zertifikat']")
    TEXT_ZWEITE_FRAGE_P6 = (By.XPATH, "//li[normalize-space()='Europäische ID']")
    TEXT_ZWEITE_FRAGE_P7 = (By.XPATH, "//p[contains(text(),'Wählen Sie eine Option aus und folgen Sie den Schr')]")
    TEXT_ZWEITE_FRAGE_P8 = (By.XPATH, "//p[contains(text(),'Jede dieser Optionen stellt eine Zugangsart dar.')]")

    BUTTON_DRITTE_FRAGE_WIE_STELLE_ICH_EIN_ONLINE_ANTRAG = (By.XPATH, "//button[@data-test-id='5kZ4i_2_disclosure"
                                                                      "-button']")
    TEXT_DRITTE_FRAGE_WIE_STELLE_ICH_EIN_ONLINE_ANTRAG = (By.XPATH, "//p[contains(text(),'Bisher mussten Sie für das "
                                                                    "Stellen eines Antrags d')]")

    LINK_ALLE_HILFREICHE_INFORMATIONEN = (By.XPATH, "//a[@data-test-id='JFxjf']")

    # Links: Die Bund-ID können sie beispielweise hier schon nutzen
    LINK_BUND_DE_VERWALTUNG = (By.XPATH, "//a[@data-test-id='MleXd']")
    LINK_BAFOG = (By.XPATH, "//a[@data-test-id='1VBHO']")

    # Footer: Impressum - Datenschutz - Erklärung zur Barrierefreiheit - Kontakt
    BUTTON_IMPRESSUM = (By.XPATH, "//a[@data-test-id='QqJeL']")
    BUTTON_DATENSCHUTZ = (By.XPATH, "//a[@data-test-id='UCwTy']")
    BUTTON_BARRIEREFREIHEIT = (By.XPATH, "//a[@data-test-id='ugwq5']")
    BUTTON_KONTAKT_BUTTON = (By.XPATH, "//a[@data-test-id='Uwndb']")

