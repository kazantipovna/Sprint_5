import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_lk_from_main():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver.find_element(By.XPATH, './/header/nav/a/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/ul/li[1]/a[text()="Профиль"]')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
    driver.quit()


def test_go_to_constructor_from_lk():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver.find_element(By.XPATH, './/header/nav/a/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/ul/li[1]/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, './/nav/ul/li[1]/a/p[text()="Конструктор"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/section[1]/h1[text()="Соберите бургер"]')))
    assert driver.find_element(By.XPATH, './/section[1]/h1[text()="Соберите бургер"]').is_displayed()
    driver.quit()


def test_logout():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(conftest.email)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(conftest.password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
    driver.find_element(By.XPATH, './/header/nav/a/p[text()="Личный Кабинет"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/ul/li[1]/a[text()="Профиль"]')))
    driver.find_element(By.XPATH, './/nav/ul/li[3]/button[text()="Выход"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Войти"]')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()
