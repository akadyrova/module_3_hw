import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser=webdriver.Chrome()
    browser.implicitly_wait(10)
    link="http://selenium1py.pythonanywhere.com/"+language+"/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    yield browser
    print("\nquit browser..")
    browser.quit()