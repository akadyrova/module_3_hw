import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser=webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    yield browser
    print("\nquit browser..")
    browser.quit()