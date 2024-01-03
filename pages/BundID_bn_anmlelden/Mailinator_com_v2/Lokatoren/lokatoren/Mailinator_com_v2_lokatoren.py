from selenium.webdriver.common.by import By


class Mailinator_com_v2_lokatoren:

    PUBLIC_MAILINATOR_INBOX_EINGABEFELD = (By.XPATH, "//input[@id='search']")
    GO_MAILINATOR_INBOX_BUTTON = (By.XPATH, "//button[@value='Search for public inbox for free']")

    IFRAME_MAILINATOR_HTML_MSG_BODY = (By.ID,"html_msg_body")

    # PASSWORT VERGESSEN ###############################################################################################
    # Wenn es nur eine, Passwort vergessen Nachricht gibt
    BUND_ID_PASSWORT_VERGESSEN_LINK_1 = (By.XPATH, "//td[normalize-space()='BundID: Passwort vergessen']")
    # Wenn es mehrere passwort vergessen Nachrichten gibt
    BUND_ID_PASSWORT_VERGESSEN_LINK_2 = (By.XPATH, "(//td[contains(text(),'BundID: Passwort vergessen')])[1]")

    NEUES_PASSWORT_ANLEGEN_LINK = (By.XPATH, "//a[normalize-space()='Neues Passwort anlegen']")

    # BENUTZERNAME VERGESSEN ###########################################################################################
    # Wenn es nur eine benutzername vergessen Nachricht gibt
    BUND_ID_IHR_BENUTZERNAME_LINK_1 = (By.XPATH, "//td[normalize-space()='BundID: Ihr Benutzername']")
    # Wenn es mehrere benutzername vergessen Nachrichten gibt
    BUND_ID_IHR_BENUTZERNAME_LINK_2 = (By.XPATH, "(//td[contains(text(),'BundID: Ihr Benutzername')])[1]")

    # Zeile finden in der, der Benutzername steht [Ihr Benutzername lautet: auto_user_01] ##############################
    IHR_BENUTZERNAME_LAUTET_TEXT = (By.XPATH, "//body/div/p[3]")

    VERIFIZIERUNGSCODE_TEXT = (By.XPATH, "//p[translate(normalize-space(), '0123456789', '0000000000')='000000']")
    IHR_BUND_ID_VERIFIZIERUNGS_CODE_LINK= (By.XPATH, "(//td[contains(text(),'BundID: Ihr Verifizierungscode')])[1]")


