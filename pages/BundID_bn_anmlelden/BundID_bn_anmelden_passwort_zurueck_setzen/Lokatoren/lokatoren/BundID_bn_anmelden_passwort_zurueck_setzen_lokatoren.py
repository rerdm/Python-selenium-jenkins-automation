from selenium.webdriver.common.by import By


class BundID_bn_anmelden_passwort_zurueck_setzen_lokatoren:

    BENUTZERNAME_ODER_EMAIL_EINGABEFELD = (By.XPATH, "//input[@aria-label='Benutzername oder E-Mail-Adresse*']")
    GEHEIME_ANTWORT_EINGABEFELD = (By.XPATH, "//input[@aria-label='Geheime Antwort*']")

    BENUTZERNAME_ODER_EMAIL_INFO_BUTTON = (By.XPATH, "//body/div[@id='app']/div/div/div/div/main/section/div[@role='form']/div/div/div/div/div[1]/button[1]//*[name()='svg']")
    BENUTZERNAME_ODER_EMAIL_INFO_POPUP_SCHLIESSEN_BUTTON = (By.XPATH, "//div[@role='form']//div//div//div//div//div//div//div//button//*[name()='svg']")

    PASSWORT_ZUREUCKSETZEN_BUTTON = (By.XPATH, "//span[normalize-space()='Passwort zurücksetzen']")
    PASSWORT_ZURUECKSETZEN_POP_UP_WEITER_BUTTON = (By.XPATH, "//div[@id='modalContent']//div//button//div")

