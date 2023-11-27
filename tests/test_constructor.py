from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import helpers


def test_go_to_souses(driver):
    """Переход в менюшку "Соусы"."""
    driver.find_element(*helpers.Locators.LOCATOR_SOUSES).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_SOUSES_CHECK))
    assert driver.find_element(*helpers.Locators.LOCATOR_SOUSES_CHECK).is_displayed()


def test_go_to_nachinki(driver):
    """Переход в менюшку "Начинки"."""
    driver.find_element(*helpers.Locators.LOCATOR_NACHINKI).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_NACHINKI_CHECK))
    assert driver.find_element(*helpers.Locators.LOCATOR_NACHINKI_CHECK).is_displayed()


def test_go_to_bulki(driver):
    """Переход в менюшку "Булки" через "Соусы"."""
    driver.find_element(*helpers.Locators.LOCATOR_SOUSES).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_SOUSES_CHECK))
    driver.find_element(*helpers.Locators.LOCATOR_BULKI).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_BULKI_CHECK))
    assert driver.find_element(*helpers.Locators.LOCATOR_BULKI_CHECK).is_displayed()
