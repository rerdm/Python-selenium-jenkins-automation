from selenium.webdriver.common.by import By


class BundID_bn_anmelden_benutzername_anfordern_lokatoren:

    EMAIL_ADRESSE_EINGABEFELD = (By.XPATH, "//input[@aria-label='E-Mail-Adresse*']")
    GEHEIME_ANTWORT_EINGABEFELD = (By.XPATH, "//input[@aria-label='Geheime Antwort*']")

    BENUTZERNAME_ANFORDERN_BUTTON = (By.XPATH, "//span[normalize-space()='Benutzername anfordern']")
    EMAIL_ADRESSE_INFO_BUTTON = (By.XPATH, "//body//div[@id='app']//div[@role='form']//div//div//div//div//div[1]//button[1]//*[name()='svg']")



    EMAIL_ADRESSE_INFO_POPUP_SCHLIESSEN_BUTTON = (By.XPATH, "(//*[name()='svg'])[8]")

    BENUTZERNAME_ANFORDERN_TEXT_P1 = (By.XPATH, "//div[@id='app']//div//div//div//div//main//section//div//h2")
    BENUTZERNAME_ANFORDERN_TEXT_P2 = (By.XPATH, "//body/div[@id='app']/div/div/div/div/main/section/div[1]/div[1]")



    BENUTZERNAME_ANFORDERN_POP_UP_SCHLIESSEN_BUTTON = (By.XPATH, "//button[@aria-label='close']//*[name()='svg']")
    BENUTZERNAME_ANFORDERN_POP_UP_WEITER_BUTTON = (By.XPATH, "//div[@id='modalContent']//div//button//div")

    WEITER_MIT_BENUTZERNAME_UND_PASSWORT_POP_UP_WEITER_BUTTON = (By.XPATH , "//div[@id='modalContent']//div//button")
    WEITER_MIT_BENUTZERNAME_UND_PASSWORT_POP_UP_SCHLIESSEN_BUTTON = (By.XPATH, "//button[@aria-label='close']")
    EMAIL_ADRESSE_INFO_POPUP_TEXT_P1 = (By.XPATH, "//div[@role='form']//div//div//div//div//div//div//div//h2")
    EMAIL_ADRESSE_INFO_POPUP_TEXT_P2 = (By.XPATH, "//div[@role='form']//div//div//div//div//div//div//div//ul//li")





