import data
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_main_page(driver):
    """Логин с главной страницы."""
    driver.find_element(*helpers.Locators.LOCATOR_LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    assert driver.find_element(*helpers.Locators.LOCATOR_ORDER_BNT).is_displayed()


def test_login_from_lk(driver):
    """Логин со страницы ЛК."""
    driver.find_element(*helpers.Locators.LOCATOR_LK_BNT).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.
                                    visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    assert driver.find_element(*helpers.Locators.LOCATOR_ORDER_BNT).is_displayed()


def test_login_from_login_page(driver_login):
    """Логин со страницы логина."""
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    assert driver_login.find_element(*helpers.Locators.LOCATOR_ORDER_BNT).is_displayed()


def test_login_after_registration(driver_register):
    """Логин сразу после регистрации."""
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    helpers.registration_fields_set(driver_register, name, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_LOGIN_BNT2))
    helpers.login_fields_set(driver_register, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_ORDER_BNT).is_displayed()


def test_login_from_recovery_pass(driver_login):
    """Логин со страницы восстановления пароля."""
    driver_login.find_element(*helpers.Locators.LOCATOR_RECOVER_PASS).click()
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_RECOVER_PASS_BNT))
    driver_login.find_element(*helpers.Locators.LOCATOR_LOGIN_A).click()
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_LOGIN_BNT2))
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.
                                          visibility_of_element_located(helpers.Locators.LOCATOR_ORDER_BNT))
    assert driver_login.find_element(*helpers.Locators.LOCATOR_ORDER_BNT).is_displayed()
