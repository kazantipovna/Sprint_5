from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Locators:
    LOCATOR_SOUSES = By.XPATH, './/span[text()="Соусы"]'
    LOCATOR_NACHINKI = By.XPATH, './/span[text()="Начинки"]'
    LOCATOR_BULKI = By.XPATH, './/span[text()="Булки"]'
    LOCATOR_SOUSES_CHECK = By.XPATH, './/h2[text()="Соусы"]'
    LOCATOR_NACHINKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'
    LOCATOR_BULKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'


def test_go_to_to(driver):
    driver.find_element(Locators.LOCATOR_SOUSES).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Locators.LOCATOR_SOUSES_CHECK))
    driver.find_element(Locators.LOCATOR_BULKI).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Locators.LOCATOR_BULKI_CHECK))
    assert driver.find_element(Locators.LOCATOR_BULKI_CHECK).is_displayed()


def test_go_to_souses(driver):
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Соусы"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Соусы"]').is_displayed()


def test_go_to_nachinki(driver):
    driver.find_element(By.XPATH, './/span[text()="Начинки"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Начинки"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Начинки"]').is_displayed()


def test_go_to_bulki(driver):
    driver.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Соусы"]')))
    driver.find_element(By.XPATH, './/span[text()="Булки"]').click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Булки"]')))
    assert driver.find_element(By.XPATH, './/h2[text()="Булки"]').is_displayed()
