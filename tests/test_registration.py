import data
import helpers
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_without_pass(driver_register):
    helpers.registration_fields_set(driver_register, helpers.random_name(), helpers.random_email(), '')
    assert driver_register.current_url == 'https://stellarburgers.nomoreparties.site/register'


def test_registration_without_email(driver_register):
    helpers.registration_fields_set(driver_register, helpers.random_name(), '', helpers.random_pass())
    assert driver_register.current_url == 'https://stellarburgers.nomoreparties.site/register'


def test_registration_without_name(driver_register):
    helpers.registration_fields_set(driver_register, '', helpers.random_email(), helpers.random_pass())
    assert driver_register.current_url == 'https://stellarburgers.nomoreparties.site/register'


@pytest.mark.parametrize('password', [helpers.short_pass[0], helpers.short_pass[1], helpers.short_pass[2],
                                      helpers.short_pass[3], helpers.short_pass[4]])
def test_registration_password_less_6_synbols(driver_register, password):
    helpers.registration_fields_set(driver_register, helpers.random_name(), helpers.random_email(), password)
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]')))
    assert driver_register.find_element(By.XPATH, './/fieldset[3]/div/p').text == 'Некорректный пароль'


@pytest.mark.parametrize('email', [helpers.unform_email[0], helpers.unform_email[1], helpers.unform_email[2], helpers.unform_email[3]])
def test_registration_with_incorrect_email(driver_register, email):
    helpers.registration_fields_set(driver_register, helpers.random_name(), email, helpers.random_pass())
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/p[text()="Такой пользователь уже существует"]')))
    assert driver_register.find_element(By.XPATH, '//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'


def test_registration_correct(driver_register):
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    helpers.registration_fields_set(driver_register, name, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    assert driver_register.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_registration_with_exist_user(driver_register):
    helpers.registration_fields_set(driver_register, data.name, data.email, data.password)
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/div/p[text()="Такой пользователь уже существует"]')))
    assert driver_register.find_element(By.XPATH, '//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'
