import data
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_main_page(driver):
    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()


def test_login_from_lk(driver):
    driver.find_element(By.XPATH, './/header/nav/a/p[text()="Личный Кабинет"]').click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()


def test_login_from_login_page(driver_login):
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver_login.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()


def test_login_after_registration(driver_register):
    name = helpers.random_name()
    email = helpers.random_email()
    password = helpers.random_pass()
    helpers.registration_fields_set(driver_register, name, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    helpers.login_fields_set(driver_register, email, password)
    WebDriverWait(driver_register, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver_register.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()


def test_login_from_recovery_pass(driver_login):
    driver_login.find_element(By.XPATH, './/a[text()="Восстановить пароль"]').click()
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Восстановить"]')))
    driver_login.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver_login.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
