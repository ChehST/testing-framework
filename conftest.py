import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from _pytest.config.argparsing import Parser


# Create fixture for registration command line options
def pytest_addoption(parser: Parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose browser: english or spanish :)",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest):

    browser_name = request.config.getoption("browser")
    browser = None

    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # Тест должен запускаться с параметром language следующей командой:
        # pytest --language=es test_items.py
        # и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
