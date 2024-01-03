import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class InitialisierenWebdriversSetzeZoomLevel:

    """
     ###################################################################################################################
     Autor: [Rene Erdmann]
     Erstellt am: [26.06.2023]

     Bitte prüft, ob ihr die neueste Selenium Version installiert habt
     Im Terminal --> # pip list
     ... selenium 4.11.2
     Wenn ihr eine ältere version habt dan updated die Version
     Im Terminal -->  # pip install --upgrade selenium

     Danach sollte # pip list die neuste version anzeigen.

     ###################################################################################################################
    """

    def get_chrome_driver_ohne_zoom(self):

        driver = webdriver.Chrome()

        time.sleep(6)
        driver.maximize_window()

        return driver

    def get_chrome_driver_zoom(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--force-device-scale-factor=0.80")

        driver = webdriver.Chrome(options=chrome_options)

        driver.maximize_window()

        return driver

    def get_firefox_driver_ohne_zoom(self):

        # TODO
        driver = webdriver.Firefox()
        time.sleep(6)
        driver.maximize_window()

        return driver

    def get_firefox_driver_zoom(self):

        # TODO
        # Erstelle eine Instanz der Firefox-Options
        firefox_options = Options()

        # Setze das Zoom-Level auf 80%
        firefox_options.add_argument("--zoom 0.30")

        # Initialisiere den Firefox-Driver mit den festgelegten Optionen
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()

        return driver


if __name__ == '__main__':

    # Driver Test Chrom ohne Zoom

    driver_initialisieren = InitialisierenWebdriversSetzeZoomLevel()
    driver = driver_initialisieren.get_chrome_driver_ohne_zoom()
    driver.get("https://test.id.bund.de/de")
    time.sleep(4)
    driver.quit()

    # # Driver Test Chrom mit Zoom

    driver_initialisieren = InitialisierenWebdriversSetzeZoomLevel()
    driver = driver_initialisieren.get_chrome_driver_zoom()
    driver.get("https://test.id.bund.de/de")
    time.sleep(4)
    driver.quit()



