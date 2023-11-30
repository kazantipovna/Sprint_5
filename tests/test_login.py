import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_main_page(driver):
    """Логин с главной страницы."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    assert driver.find_element(*locators.Locators.ORDER_BNT).is_displayed()


def test_login_from_lk(driver):
    """Логин со страницы ЛК."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.LK_BNT).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    assert driver.find_element(*locators.Locators.ORDER_BNT).is_displayed()


def test_login_from_login_page(driver):
    """Логин со страницы логина."""
    driver.get('https://stellarburgers.nomoreparties.site/login')
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    assert driver.find_element(*locators.Locators.ORDER_BNT).is_displayed()


def test_login_after_registration(driver):
    """Логин сразу после регистрации."""
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, name, email, password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LOGIN_BNT2))
    helpers.login_fields_set(driver, email, password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    assert driver.find_element(*locators.Locators.ORDER_BNT).is_displayed()


def test_login_from_recovery_pass(driver):
    """Логин со страницы восстановления пароля."""
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(*locators.Locators.RECOVER_PASS).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.RECOVER_PASS_BNT))
    driver.find_element(*locators.Locators.LOGIN_A).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LOGIN_BNT2))
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    assert driver.find_element(*locators.Locators.ORDER_BNT).is_displayed()
