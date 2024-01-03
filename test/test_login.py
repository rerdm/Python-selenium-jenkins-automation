import sys
import pytest
import allure

sys.path.append("C:/Users/renee/Desktop/PublicDocuments/7. Programming/Python-selenium-jenkins-automation")

from classes.InitialisiereWebdriverSetzeZoomLevel import InitialisiereWebdriverSetzeZoomLevel
from pages.BundID_bn_anmlelden.BundID_bn_anmleden_basis_page.Lokatoren.lokatoren import BundID_bn_anmleden_basis_page_lokatoren


@pytest.fixture
def driver():

    webdriver_initialisieren = InitialisiereWebdriverSetzeZoomLevel()
    driver_instance = webdriver_initialisieren.get_firefox_webdriver_mit_zoom()

    yield driver_instance
    driver_instance.quit()

def test_open_website_and_login_postive_test(driver):

    expected_url = "https://test.id.bund.de/de"
    driver.get(expected_url)
    actual_url = driver.current_url



    assert actual_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"




