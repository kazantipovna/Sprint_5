import random
import string
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# короткие пароли
short_pass = [''.join(random.sample(string.ascii_letters + string.digits, 1)),
              ''.join(random.sample(string.ascii_letters + string.digits, 2)),
              ''.join(random.sample(string.ascii_letters + string.digits, 3)),
              ''.join(random.sample(string.ascii_letters + string.digits, 4)),
              ''.join(random.sample(string.ascii_letters + string.digits, 5))]


# имейлы не по формату
unform_email = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail."]


def random_name():
    name = (f"{''.join(random.choice(string.ascii_uppercase) for i in range(1))}"
            f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}")
    return name


def random_email():
    email = (f"{''.join(random.choice(string.ascii_lowercase) for i in range(4))}_"
             f"{''.join(random.choice(string.ascii_lowercase) for i in range(6))}_"
             f"{random.randint(1111, 9999)}@gmail.com")
    return email


def random_pass():
    password = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return password


def login_fields_set(driver, email, password):
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'Auth_login__3hAey')))
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(email)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(password)
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()


def registration_fields_set(driver, name, email, password):
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(email)
    driver.find_element(By.XPATH, './/fieldset[3]//input').send_keys(password)
    driver.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]').click()
