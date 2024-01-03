from selenium.webdriver.common.by import By


class BundID_bn_anmelden_zugaenge_daten_lokatoren_cms_texte:

    CMS_TEXT_IHRE_TELEFONNUMMER = (By.XPATH, "//h2[@class='font-semibold mb-4']")
    CMS_TEXT_DARF_FOLGENDE_ZEICHEN = (By.XPATH, "//li[contains(text(),'... darf folgende Zeichen enthalten: Ziffern, Bind')]")
    CMS_TEXT_DARF_KEINE_KLAMMERN = (By.XPATH, "//li[contains(text(),'... darf keine Klammern oder Schrägstriche enthalt')]")
    CMS_TEXT_DARF_NICHT_MIT_EINER_O = (By.XPATH, "//li[normalize-space()='... darf nicht mit einer 0 beginnen']")
    CMS_TEXT_DARF_NICHT_MIT_EINEM_LEERZEICHEN = (By.XPATH, "//li[contains(text(),'... darf nicht mit einem Leerzeichen oder Bindestr')]")
    CMS_TEXT_IHRE_DATEN_WURDEN_ERFOLGREICH = (By.XPATH, "//h3[normalize-space()='Ihre Daten wurden erfolgreich geändert.']")
