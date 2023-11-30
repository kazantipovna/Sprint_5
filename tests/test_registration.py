import data
import helpers
import pytest
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_without_pass(driver):
    """Попытка регистрации без пароля."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, helpers.random_name(), helpers.random_email(), '')
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.REGISTER_BNT))
    assert driver.find_element(*locators.Locators.HEADER_H2).text == 'Регистрация'


def test_registration_without_email(driver):
    """Попытка регистрации без имейла."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, helpers.random_name(), '', helpers.random_pass())
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.REGISTER_BNT))
    assert driver.find_element(*locators.Locators.HEADER_H2).text == 'Регистрация'


def test_registration_without_name(driver):
    """Попытка регистрации без имени."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, '', helpers.random_email(), helpers.random_pass())
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.REGISTER_BNT))
    assert driver.find_element(*locators.Locators.HEADER_H2).text == 'Регистрация'


@pytest.mark.parametrize('password', ['q', '1qa2w'])
def test_registration_password_less_6_synbols(driver, password):
    """Попытка регистрации с паролем <6 символов. Проверяем граничные значения 1 и 5."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, helpers.random_name(), helpers.random_email(), password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.INCORRECT_PASS))
    assert driver.find_element(*locators.Locators.INCORRECT_PASS_CHECK).text == 'Некорректный пароль'


@pytest.mark.parametrize('email', [data.unform_email[0], data.unform_email[1]])
def test_registration_with_incorrect_email(driver, email):
    """Попытка регистрации с имейлом не по формату."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, helpers.random_name(), email, helpers.random_pass())
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.USER_EXISTS))
    assert driver.find_element(*locators.Locators.USER_EXISTS_CHECK).text == 'Такой пользователь уже существует'


def test_registration_correct(driver):
    """Успешная регистрация."""
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, name, email, password)
    WebDriverWait(driver, 10).until(expected_conditions. visibility_of_element_located(locators.Locators.LOGIN_H2))
    assert driver.find_element(*locators.Locators.HEADER_H2).text == 'Вход'


def test_registration_with_exist_user(driver):
    """Попытка регистрации существующего пользователя."""
    driver.get('https://stellarburgers.nomoreparties.site/register')
    helpers.registration_fields_set(driver, data.name, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions. visibility_of_element_located(locators.Locators.USER_EXISTS))
    assert driver.find_element(*locators.Locators.USER_EXISTS_CHECK).text == 'Такой пользователь уже существует'
