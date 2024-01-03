from selenium.webdriver.common.by import By


class BundID_bn_anmelden_postfach_lokatoren:

    ZUGANGE_UND_DATEN_TAB = (By.XPATH, "//button[@id='tab-accessPoints']")
    KONTO_AKTIVITAETEN_TAB = (By.XPATH,"//button[@id='tab-activities']")
    POSTFACH_TAB = (By.XPATH, "//button[@id='tab-postkorb']")

    BUND_ID_PASSWORT_ANGEFORDERT_EINZELNE_NACHRICHT = (By.XPATH ,"//td[normalize-space()='BundID: Benutzername angefordert']")
    BUND_ID_PASSWORT_ANGEFORDERT_OBERSTE_NACHRICHT = (By.XPATH ,"(//span[contains(text(),'BundID: Benutzername angefordert')])[1]")

    BUND_ID_BENUTZERNAME_ANGEFORDERT_EINZELNE_NACHRICHT = (By.XPATH, "(//span[contains(text(),'BundID: Benutzername angefordert')])")
    BUND_ID_BENUTZERNAME_ANGEFORDERT_OBERSTE_NACHRICHT = (By.XPATH, "(//span[contains(text(),'BundID: Benutzername angefordert')])[1]")


    AKTUELLER_LOGIN_ZEITPUNKT_TEXT = (By.XPATH ,"//body/div/div/div/div/div/div/div/div/div[1]")

    AUTO_LOGOUT_POPUP_ANMELDEN_BUTTON = (By.XPATH, "//button[@data-test-id='Rtqbe']//div")

    AUTO_LOGOUT_POPUP_TEXT_P1 = (By.XPATH , "//h3[normalize-space()='Hinweis']")
    AUTO_LOGOUT_POPUP_TEXT_P2 = (By.XPATH , "//p[contains(text(),'Sie waren längere Zeit inaktiv. Zu Ihrer Sicherhei')]")
    AUTO_LOGOUT_POPUP_TEXT_P3 = (By.XPATH , "//b[normalize-space()='Bitte melden Sie sich erneut an.']")

