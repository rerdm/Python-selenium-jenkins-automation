from selenium.webdriver.common.by import By


class BundID_bn_anmleden_basis_page_lokatoren:


    BUTTON_BENUTZERNAME_UND_PASSWORT = (By.XPATH, "//div[contains(text(),'Benutzername & Passwort')]")

    BUTTON_WEITER_MIT_BENUTZERNAME_UND_PASSWORT = (By.XPATH, "//span[normalize-space()='WEITER MIT BENUTZERNAME UND PASSWORT']")

    BENUTZERNAME_ODER_EMAIL_EINGABEFELD = (By.XPATH, "//input[@aria-label='Benutzername oder E-Mail-Adresse*']")
    PASSWORT_EINGABEFELD = (By.XPATH, "//input[@aria-label='Passwort*']")

    ANMELDE_BUTTON = (By.XPATH, "//button[@data-test-id='xxTqJ']")

    BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P1 = (By.XPATH, "//div[@id='modalContent']//div//h3")
    BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P2 = (By.XPATH,  "//div[@id='modal-container']//p[1]")
    BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P3 = (By.XPATH,  "//div[@id='modal-container']//p[2]")


    BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P2_JS = """ 
                                var xpathExpression = "//body/div[@id='modal-container']/div[@data-test-id='dGBOUmodal-overlay']/div/div[@aria-label='modal']/div/div[@id='modalContent']/div/div[1]";
                                var result = document.evaluate(xpathExpression, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
                                var textContent = result.singleNodeValue.textContent;
                                return textContent; 
                                """