import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_from_main_page():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
    driver.quit()


def test_login_from_lk():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/header/nav/a/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
    driver.quit()


def test_login_from_login_page():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
    driver.quit()


def test_login_after_registration():
    name = conftest.random_name()
    email = conftest.random_email()
    password = conftest.random_pass()
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(email)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(password)
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
    driver.quit()


def test_login_from_recovery_pass():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, './/a[text()="Восстановить пароль"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Восстановить"]')))
    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    assert driver.find_element(By.XPATH, './/button[text()="Оформить заказ"]').is_displayed()
    driver.quit()
