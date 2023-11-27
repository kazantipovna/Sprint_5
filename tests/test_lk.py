import data
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_lk_from_main(driver):
    """Переход в ЛК с главной страницы."""
    driver.find_element(*helpers.Locators.LOCATOR_LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    driver.find_element(*helpers.Locators.LOCATOR_LK_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_LK_PROFILE))
    assert driver.find_element(*helpers.Locators.LOCATOR_LK_PROFILE)


def test_go_to_constructor_from_lk(driver_login):
    """Переход в конструктор из ЛК."""
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    driver_login.find_element(*helpers.Locators.LOCATOR_LK_BNT).click()
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_LK_PROFILE))
    driver_login.find_element(*helpers.Locators.LOCATOR_CONSTRUCTOR).click()
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_MAKE_BURGER))
    assert driver_login.find_element(*helpers.Locators.LOCATOR_MAKE_BURGER).is_displayed()


def test_logout(driver):
    """Выход из ЛК."""
    driver.find_element(*helpers.Locators.LOCATOR_LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    driver.find_element(*helpers.Locators.LOCATOR_LK_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_LK_PROFILE))
    driver.find_element(*helpers.Locators.LOCATOR_LOGOUT_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_LOGIN_BNT2))
    assert driver.find_element(*helpers.Locators.LOCATOR_LOGIN_BNT2)
