import random
import string
import data
import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def random_name():
    """Метод генерирует рандомное имя из букв латинского алфавита."""
    name = (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")
    return name


def random_email():
    """Метод генерирует рандомный имейл из букв латинского алфавита и цифр"""
    email = (f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}_"
             f"{''.join(random.choice(string.ascii_lowercase) for i in range(6))}_"
             f"{random.randint(1111, 9999)}@gmail.com")
    return email


def random_pass():
    """Метод генерирует рандомный пароль из букв латинского алфавита и цифр"""
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return password


def login_fields_set(driver, email, password):
    """Метод заполняет поля для логина и жмет кнопку."""
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locators.Locators.LOGIN_BNT2))
    driver.find_element(*locators.Locators.FIELDSET1).send_keys(email)
    driver.find_element(*locators.Locators.FIELDSET2).send_keys(password)
    driver.find_element(*locators.Locators.LOGIN_BNT2).click()


def registration_fields_set(driver, name, email, password):
    """Метод заполняет поля для регистрации и жмет кнопку."""
    driver.find_element(*locators.Locators.FIELDSET1).send_keys(name)
    driver.find_element(*locators.Locators.FIELDSET2).send_keys(email)
    driver.find_element(*locators.Locators.FIELDSET3).send_keys(password)
    driver.find_element(*locators.Locators.REGISTER_BNT).click()
