import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language of the page')
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Choose browser: Chrome or Firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name == 'chrome':
        print("\nstart chrome browser for test...")
        options = COptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test...")
        options = FOptions()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox, default browser is chrome")

    yield driver

    print("\nclose browser...")
    driver.quit()
