import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = './chromedriver'


@pytest.fixture
def driver_register():
    service = Service(executable_path=DRIVER_PATH)
    options = Options()
    options.add_argument("--window-size=1920, 1080")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://stellarburgers.nomoreparties.site/register')
    yield driver
    driver.quit()


# @pytest.fixture
# def driver_register():
#     driver = webdriver.Chrome()
#     driver.get('https://stellarburgers.nomoreparties.site/register')
#     yield driver
#     driver.quit()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    yield driver
    driver.quit()
