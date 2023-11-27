import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_souses(driver):
    """Переход в менюшку "Соусы"."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.SOUSES).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.SOUSES_CHECK))
    assert driver.find_element(*locators.Locators.SOUSES_CHECK).is_displayed()


def test_go_to_nachinki(driver):
    """Переход в менюшку "Начинки"."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.NACHINKI).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.NACHINKI_CHECK))
    assert driver.find_element(*locators.Locators.NACHINKI_CHECK).is_displayed()


def test_go_to_bulki(driver):
    """Переход в менюшку "Булки" через "Соусы"."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.SOUSES).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.SOUSES_CHECK))
    driver.find_element(*locators.Locators.BULKI).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.BULKI_CHECK))
    assert driver.find_element(*locators.Locators.BULKI_CHECK).is_displayed()
