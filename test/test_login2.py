import pytest
from selenium import webdriver
import time

@pytest.fixture
def chrome_driver():
    # Setup: Erstelle eine Instanz des ChromeDrivers und gib sie zurück
    chromedriver_path = "C:\\Users\\renee\\Desktop\\PublicDocuments\\7. Programming\\Python-selenium-jenkins-automation\\driver\\ChromeDriver120\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    yield driver  # Hier wird die Instanz an den Test übergeben
    # Teardown: Schließe den ChromeDriver nach dem Test
    driver.quit()

def test_open_and_close_webpage(chrome_driver):
    # Test: Öffne die Webseite, warte 2 Minuten und schließe dann den Browser
    chrome_driver.get("https://www.google.com")
    time.sleep(10)
    # Hier können zusätzliche Assertions hinzugefügt werden, um den Test zu überprüfen
