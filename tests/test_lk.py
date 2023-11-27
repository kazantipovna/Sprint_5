import data
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_lk_from_main(driver):
    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    assert driver.find_element(By.XPATH, './/a[text()="Профиль"]')


def test_go_to_constructor_from_lk(driver_login):
    helpers.login_fields_set(driver_login, data.email, data.password)
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver_login.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    driver_login.find_element(By.XPATH, './/p[text()="Конструктор"]').click()
    WebDriverWait(driver_login, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[1]/h1[text()="Соберите бургер"]')))
    assert driver_login.find_element(By.XPATH, './/h1[text()="Соберите бургер"]').is_displayed()


def test_logout(driver):
    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    helpers.login_fields_set(driver, data.email, data.password)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, './/button[text()="Выход"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Войти"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Войти"]')
