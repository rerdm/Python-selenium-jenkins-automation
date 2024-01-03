import time

from selenium import webdriver

class InitialisierenDesWebdrivers:

    """
     ###################################################################################################################
     Autor: [Rene Erdmann]
     Erstellt am: [26.06.2023]
     Klasse: [InitialisierenDesWebdrivers]
     Methoden: [get_chrome_driver,get_firefox_driver]
     Funktion:
     Diese Klasse ermöglicht es einen Webdriver zu initialisieren und gibt den initialisierten driver zurück.
     Hier können die unterschiedlichen driver abgelegt werden. Die Driver können über eine getter Methode
     ausgelesen werden.

     Möglichkeit 1 zum Ablegen des drivers (Wenn vorhanden )
        C-Users-rerdmann-AppData-Local-Programs-Python-Python31 ( - mit backslash ersetzen )
     Möglichkeit 2 (Wenn vorhanden)
        Extenal Librarys->PythonXXX --> Scripts

     Chrom = chromedriver.exe
     FireFox = geckodriver.exe
     ###################################################################################################################
    """

    def get_chrome_driver(self):

        driver = webdriver.Chrome()
        time.sleep(6)
        driver.maximize_window()

        return driver

    def get_firefox_driver(self):

        driver = webdriver.Firefox()
        time.sleep(6)
        driver.maximize_window()

        return driver

if __name__ == '__main__':

    # Beispielverwendung
    driver_initialisieren = InitialisierenDesWebdrivers()
    driver = driver_initialisieren.get_firefox_driver()
    driver.get("https://test.id.bund.de/de")
    time.sleep(5)

