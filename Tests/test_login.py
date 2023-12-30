import pytest

from Klassen.InitialisiereWebdriverSetzeZoomLevel import InitialisiereWebdriverSetzeZoomLevel

@pytest.fixture

def driver():

    webdriver_initialisieren = InitialisiereWebdriverSetzeZoomLevel()
    driver_instance = webdriver_initialisieren.get_firefox_webdriver_mit_zoom()

    yield driver_instance
    driver_instance.quit()

@pytest.mark.login
def test_open_and_check_url(driver):

    expected_url = "https://test.id.bund.de/de"
    driver.get(expected_url)
    actual_url = driver.current_url
    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"


