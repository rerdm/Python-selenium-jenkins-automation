from selenium.webdriver.common.by import By

class BundID_bn_anmelden_anmeldeseite_lokatoren:

    PASSWORT_VERGESSEN_LINK = (By.XPATH, "//a[@data-test-id='VLWYO']")
    BENUTZERNAME_VERGESSEN_LINK = (By.XPATH, "//a[@data-test-id='ZjjNR']")

    BENUTZERNAME_ODER_PASSWORT_EINGABEFELD = (By.XPATH, "//input[@aria-label='Benutzername oder E-Mail-Adresse*']")
    PASSWORT_EINGABEFELD = (By.XPATH, "//input[@aria-label='Passwort*']")

    ANMELDE_BUTTON = (By.XPATH, "//button[@data-test-id='xxTqJ']//div")