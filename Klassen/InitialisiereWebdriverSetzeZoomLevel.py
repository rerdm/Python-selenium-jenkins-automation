import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class InitialisiereWebdriverSetzeZoomLevel:

    def __init__(self):
        self.driver = None

    def get_chrome_webdriver_ohne_zoom(self):

        """
        Diese Methode liefert einen Chrome-Webdriver instanz zurück.
        Das Zoomlevel ist auf 100 % gestellt
        """

        if not self.driver:
            chrome_options = Options()

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

            # Webdriver Window auf Maximum setzen
            self.driver.maximize_window()

        return self.driver

    def get_chrome_webdriver_mit_zoom(self):
        """
        Diese Methode liefert einen Chrome-Webdriver instanz zurück.
        Das Zoomlevel ist hard codiert auf 90 % gestellt
        """
        if not self.driver:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

        return self.driver

    def get_firefox_webdriver_ohne_zoom(self):

        """
        Diese Methode liefert einen FireFox-Webdriver instanz zurück.
        Das Zoomlevel ist auf 100 % gestellt
        """
        if not self.driver:
            firefox_options = FirefoxOptions()

            firefox_service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

            self.driver.maximize_window()

        return self.driver

    def get_firefox_webdriver_mit_zoom(self):
        """
        Diese Methode liefert einen FireFox-Webdriver instanz zurück.
        Das Zoomlevel ist hard codiert auf 90 % gestellt
        """
        if not self.driver:

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.90")

            chrome_service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            self.driver.maximize_window()

        return self.driver

    def close_webdriver(self):

        if self.driver:
            self.driver.quit()
            self.driver = None


if __name__ == "__main__":

    webdriver_initialisieren = InitialisiereWebdriverSetzeZoomLevel()

    try:
        driver = webdriver_initialisieren.get_firefox_webdriver_mit_zoom()
        driver.get("https://test.id.bund.de/de")
        time.sleep(5)

        # Dein Selenium-Code hier...

    finally:
        webdriver_initialisieren.close_webdriver()
