import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Config, browser, Browser
from utils import allure_attach


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    # Настройка удалённого драйвера для Selene
    browser.config.driver_remote_url = "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    browser.config.driver_options = options
    browser.config.timeout = 10

    yield browser

    browser.quit()












# @pytest.fixture(scope='function')
# def setup_browser(request):
#     # options = Options()
#     # selenoid_capabilities = {
#     #     "browserName": "chrome",
#     #     "browserVersion": "128.0",
#     #     "selenoid:options": {
#     #         "enableVNC": True,
#     #         "enableVideo": True
#     #     }
#     # }
#     # options.capabilities.update(selenoid_capabilities)
#     # driver = webdriver.Remote(
#     #     command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
#     #     options=options
#     # )
#     #
#     #
#     # browser.config._driver = driver
#     yield browser
#     #
#     # allure_attach.add_screenshot(browser)
#     # allure_attach.add_logs(browser)
#     # allure_attach.add_html(browser)
#     # # allure_attach.add_video(browser)
#
#     browser.quit()