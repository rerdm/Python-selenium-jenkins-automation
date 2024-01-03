

from selenium.webdriver.common.by import By


class BundID_bn_anmelden_konto_aktivitaeten_lokatoren:

    ZUGANGE_UND_DATEN_TAB = (By.XPATH, "//button[@id='tab-accessPoints']")
    KONTO_AKTIVITAETEN_TAB = (By.XPATH,"//button[@id='tab-activities']")
    POSTFACH_TAB = (By.XPATH, "//button[@id='tab-postkorb']")

    NAECHSTE_NACHRICHT_BUTTON = (By.XPATH,"//button[@data-test-id='CTYEWpagination_button_next']//span//div")

    NAECHSTER_SEITE_BUTTON_TEXT = (By.XPATH, "//button[@data-test-id='CTYEWpagination_button_next']//span//div")
    CMS_TEXT_TELEFONNUMMER_GEAENDERT = (By.XPATH, "(//div[@class='h-full flex items-start'] )[1]")
    CMS_TEXT_DE_MAIL_GEAENDERT = (By.XPATH, "(//div[@class='h-full flex items-start'] )[2]")