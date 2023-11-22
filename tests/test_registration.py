import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_without_pass():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.random_name())
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.random_email())
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
    driver.quit()


def test_registration_without_email():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.random_name())
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(conftest.random_pass())
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
    driver.quit()


def test_registration_without_name():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.random_email())
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(conftest.random_pass())
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
    driver.quit()


def test_registration_password_less_6_synbols():
    driver = webdriver.Chrome()
    for password in conftest.random_short_pass():
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.random_name())
        driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.random_email())
        driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(password)
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
        assert driver.find_element(By.XPATH, './/fieldset[3]/div/p').text == 'Некорректный пароль'
    driver.quit()


def test_registration_with_incorrect_email():
    driver = webdriver.Chrome()
    for email in conftest.unformatted_emails():
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.random_name())
        driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(email)
        driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(conftest.random_pass())
        driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/div/p[text()="Такой пользователь уже существует"]')))
        assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'
    driver.quit()


def test_registration_correct():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.random_name())
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.random_email())
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(conftest.random_pass())
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


def test_registration_with_exist_user():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/register')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.name)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/div/p[text()="Такой пользователь уже существует"]')))
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/p').text == 'Такой пользователь уже существует'
    driver.quit()
