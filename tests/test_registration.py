import data
import helpers
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_without_pass(driver_register):
    """Попытка регистрации без пароля."""
    helpers.registration_fields_set(driver_register, helpers.random_name(), helpers.random_email(), '')
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_REGISTER_BNT))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_HEADER_H2).text == 'Регистрация'


def test_registration_without_email(driver_register):
    """Попытка регистрации без имейла."""
    helpers.registration_fields_set(driver_register, helpers.random_name(), '', helpers.random_pass())
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_REGISTER_BNT))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_HEADER_H2).text == 'Регистрация'


def test_registration_without_name(driver_register):
    """Попытка регистрации без имени."""
    helpers.registration_fields_set(driver_register, '', helpers.random_email(), helpers.random_pass())
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_REGISTER_BNT))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_HEADER_H2).text == 'Регистрация'


@pytest.mark.parametrize('password', [helpers.short_pass[0], helpers.short_pass[1], helpers.short_pass[2],
                                      helpers.short_pass[3], helpers.short_pass[4]])
def test_registration_password_less_6_synbols(driver_register, password):
    """Попытка регистрации с паролем <6 символов."""
    helpers.registration_fields_set(driver_register, helpers.random_name(), helpers.random_email(), password)
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_INCORRECT_PASS))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_INCORRECT_PASS_CHECK).text == 'Некорректный пароль'


@pytest.mark.parametrize('email', [helpers.unform_email[0], helpers.unform_email[1],
                                   helpers.unform_email[2], helpers.unform_email[3]])
def test_registration_with_incorrect_email(driver_register, email):
    """Попытка регистрации с имейлом не по формату."""
    helpers.registration_fields_set(driver_register, helpers.random_name(), email, helpers.random_pass())
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_USER_EXISTS))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_USER_EXISTS_CHECK).text == 'Такой пользователь уже существует'


def test_registration_correct(driver_register):
    """Успешная регистрация."""
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    helpers.registration_fields_set(driver_register, name, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_LOGIN_H2))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_HEADER_H2).text == 'Вход'


def test_registration_with_exist_user(driver_register):
    """Попытка регистрации существующего пользователя."""
    helpers.registration_fields_set(driver_register, data.name, data.email, data.password)
    WebDriverWait(driver_register, 10).until(expected_conditions.
                                             visibility_of_element_located(helpers.Locators.LOCATOR_USER_EXISTS))
    assert driver_register.find_element(*helpers.Locators.LOCATOR_USER_EXISTS_CHECK).text == 'Такой пользователь уже существует'
