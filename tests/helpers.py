import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Locators:
    LOCATOR_LOGIN_BNT1 = By.XPATH, './/button[text()="Войти в аккаунт"]' # кнопка "Войти в аккаунт" с главной
    LOCATOR_LOGIN_BNT2 = By.XPATH, './/button[text()="Войти"]' # кнопка "Войти" со странички входа
    LOCATOR_LOGIN_H2 = By.XPATH, './/h2[text()="Вход"]' # заголовок "Вход"
    LOCATOR_LOGIN_A = By.XPATH, './/a[text()="Войти"]' # ссылка "Войти" из восстановления пароля
    LOCATOR_LOGOUT_BNT = By.XPATH, './/button[text()="Выход"]' # кнопка "Выход"
    LOCATOR_LK_BNT = By.XPATH, './/p[text()="Личный Кабинет"]' # меню "Личный кабинет"
    LOCATOR_REGISTER_BNT = By.XPATH, './/button[text()="Зарегистрироваться"]' # кнопка "Зарегистрироваться"
    LOCATOR_RECOVER_PASS = By.XPATH, './/a[text()="Восстановить пароль"]' # пункт "Восстановить пароль"
    LOCATOR_RECOVER_PASS_BNT = By.XPATH, './/button[text()="Восстановить"]' # кнопка "Восстановить пароль"
    LOCATOR_LK_PROFILE = By.XPATH, './/a[text()="Профиль"]' # меню "Профиль" в ЛК
    LOCATOR_INCORRECT_PASS = By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]' # сообщение "Некорректный пароль"
    LOCATOR_INCORRECT_PASS_CHECK = By.XPATH, './/fieldset[3]/div/p' # для проверки сообщения "Некорректный пароль"
    LOCATOR_USER_EXISTS = By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]' # сообщение "Такой пользователь уже существует"
    LOCATOR_USER_EXISTS_CHECK = By.XPATH, './/div/main/div/p' # для проверки сообщения "Такой пользователь уже существует"
    LOCATOR_FIELDSET1 = By.XPATH, './/fieldset[1]//input' # поле для ввода данных
    LOCATOR_FIELDSET2 = By.XPATH, './/fieldset[2]//input' # поле для ввода данных
    LOCATOR_FIELDSET3 = By.XPATH, './/fieldset[3]//input' # поле для ввода данных
    LOCATOR_HEADER_H2 = By.XPATH, './/h2' # любой заголовок h2
    LOCATOR_MAKE_BURGER = By.XPATH, './/section[1]/h1[text()="Соберите бургер"]' # заголовок "Соберите бургер" в конструкторе
    LOCATOR_CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]' # меню "Конструктор"
    LOCATOR_ORDER_BNT = By.XPATH, './/button[text()="Оформить заказ"]' # кнопка "Оформить заказ"
    LOCATOR_SOUSES = By.XPATH, './/span[text()="Соусы"]' # меню "Соусы"
    LOCATOR_NACHINKI = By.XPATH, './/span[text()="Начинки"]' # список "Соусы"
    LOCATOR_BULKI = By.XPATH, './/span[text()="Булки"]' # меню "Булки"
    LOCATOR_SOUSES_CHECK = By.XPATH, './/h2[text()="Соусы"]' # список "Булки"
    LOCATOR_NACHINKI_CHECK = By.XPATH, './/h2[text()="Начинки"]' # меню "Начинки"
    LOCATOR_BULKI_CHECK = By.XPATH, './/h2[text()="Начинки"]' # список "Начинки"


# список коротких паролей для провкрки регистрации с паролем <6 символов
short_pass = [''.join(random.sample(string.ascii_letters + string.digits, 1)),
              ''.join(random.sample(string.ascii_letters + string.digits, 2)),
              ''.join(random.sample(string.ascii_letters + string.digits, 3)),
              ''.join(random.sample(string.ascii_letters + string.digits, 4)),
              ''.join(random.sample(string.ascii_letters + string.digits, 5))]


# список имейлов не по формату для проверки регистрации с корректным имейлом
unform_email = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail."]


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
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOCATOR_LOGIN_BNT2))
    driver.find_element(*Locators.LOCATOR_FIELDSET1).send_keys(email)
    driver.find_element(*Locators.LOCATOR_FIELDSET2).send_keys(password)
    driver.find_element(*Locators.LOCATOR_LOGIN_BNT2).click()


def registration_fields_set(driver, name, email, password):
    """Метод заполняет поля для регистрации и жмет кнопку."""
    driver.find_element(*Locators.LOCATOR_FIELDSET1).send_keys(name)
    driver.find_element(*Locators.LOCATOR_FIELDSET2).send_keys(email)
    driver.find_element(*Locators.LOCATOR_FIELDSET3).send_keys(password)
    driver.find_element(*Locators.LOCATOR_REGISTER_BNT).click()
