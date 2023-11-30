import data
import helpers
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_lk_from_main(driver):
    """Переход в ЛК с главной страницы."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    driver.find_element(*locators.Locators.LK_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LK_PROFILE))
    assert driver.find_element(*locators.Locators.LK_PROFILE)


def test_go_to_constructor_from_lk(driver):
    """Переход в конструктор из ЛК."""
    driver.get('https://stellarburgers.nomoreparties.site/login')
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    driver.find_element(*locators.Locators.LK_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LK_PROFILE))
    driver.find_element(*locators.Locators.CONSTRUCTOR).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.MAKE_BURGER))
    assert driver.find_element(*locators.Locators.MAKE_BURGER).is_displayed()


def test_logout(driver):
    """Выход из ЛК."""
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*locators.Locators.LOGIN_BNT1).click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.ORDER_BNT))
    driver.find_element(*locators.Locators.LK_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LK_PROFILE))
    driver.find_element(*locators.Locators.LOGOUT_BNT).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LOGIN_BNT2))
    assert driver.find_element(*locators.Locators.LOGIN_BNT2)
