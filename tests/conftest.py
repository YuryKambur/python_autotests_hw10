import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import allure_attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    # Отключаем автоматическое пересоздание драйвера
    browser.config.rebuild_not_alive_driver = False
    browser.config.driver = driver

    yield browser

    allure_attach.add_screenshot(browser)
    allure_attach.add_logs(browser)
    allure_attach.add_html(browser)
    allure_attach.add_video(browser)

    browser.quit()