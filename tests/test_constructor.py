from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_souses():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Соусы"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Соусы"]').is_displayed()
    driver.quit()


def test_go_to_nachinki():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Начинки"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Начинки"]').is_displayed()
    driver.quit()


def test_go_to_bulki():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Соусы"]')))
    driver.find_element(By.XPATH, './/span[text()="Булки"]').click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Булки"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Булки"]').is_displayed()
    driver.quit()
