
from helper.Selenium_hilfs_klassen.ErstelleUndSpeicherScreenshot import ErstelleUndSpeicherScreenshot
from helper.Selenium_hilfs_klassen.WartenBisElementSichtbarIst import WartenBisElementSichtbarIst

from pages.BundID_bn_anmlelden.BundID_bn_anmleden_basis_page.Lokatoren.lokatoren_cms_texte.BundID_bn_anmleden_basis_page_lokatoren_cms_texte import \
    BundID_bn_anmleden_basis_page_cms_texte_lokatoren

from pages.BundID_bn_anmlelden.BundID_bn_anmleden_basis_page.Lokatoren.lokatoren.BundID_bn_anmleden_basis_page_lokatoren import \
    BundID_bn_anmleden_basis_page_lokatoren


class BundID_bn_anmleden_basis_page:

    """
    ####################################################################################################################
    Autor: [Rene Erdmann]
    Erstellt am: [28.06.2023]
    ####################################################################################################################
    """

    def __init__(self, driver, webdriver_wait=20, waiting_time=1):

        self.driver = driver
        self.waiting_time = waiting_time
        self.webdriver_wait = webdriver_wait

        self.bundID_bn_anmleden_basis_page_lokatoren = BundID_bn_anmleden_basis_page_lokatoren()
        self.bundID_bn_anmleden_basis_page_cms_texte_lokatoren = BundID_bn_anmleden_basis_page_cms_texte_lokatoren()

        self.warte_auf_sichtbares_element = WartenBisElementSichtbarIst(
            driver=self.driver,
            waiting_time=self.webdriver_wait)


    def benutzername_und_passwort_button_klick(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BUTTON_BENUTZERNAME_UND_PASSWORT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()


    def hinweis_weiter_mit_benutzername_u_passwort_popup_button_klick(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BUTTON_WEITER_MIT_BENUTZERNAME_UND_PASSWORT

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()


    def hinweis_weiter_mit_benutzername_u_passwort_popup_get_text_p1(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P1

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


    def hinweis_weiter_mit_benutzername_u_passwort_popup_get_text_p2(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P2

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text

    def hinweis_weiter_mit_benutzername_u_passwort_popup_get_text_p3(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P3

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element_text = element.text

        element_text = element_text.replace('\n', ' ').replace('\t', ' ').strip()

        return element_text


    # def hinweis_weiter_mit_benutzername_u_passwort_popup_get_text_p2_js(self):
    #
    #     element_text_via_js = self.driver.execute_script(self.bundID_bn_anmleden_basis_page_lokatoren.
    #                                                      BENUTZERNAME_ANFORDERN_POP_UP_TEXT_P2_JS)
    #
    #     return element_text_via_js


    def benutzername_oder_email_send_keys(self, keys):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.BENUTZERNAME_ODER_EMAIL_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def password_send_keys(self, keys):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.PASSWORT_EINGABEFELD

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.send_keys(keys)

    def anmelde_button_klick(self):

        locator = self.bundID_bn_anmleden_basis_page_lokatoren.ANMELDE_BUTTON

        element = self.warte_auf_sichtbares_element.sichtbares_element_gefunden(
            locator=locator)

        element.click()




