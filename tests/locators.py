from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BNT1 = By.XPATH, './/button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" с главной
    LOGIN_BNT2 = By.XPATH, './/button[text()="Войти"]'  # кнопка "Войти" со странички входа
    LOGIN_H2 = By.XPATH, './/h2[text()="Вход"]'  # заголовок "Вход"
    LOGIN_A = By.XPATH, './/a[text()="Войти"]'  # ссылка "Войти" из восстановления пароля
    LOGOUT_BNT = By.XPATH, './/button[text()="Выход"]'  # кнопка "Выход"
    LK_BNT = By.XPATH, './/p[text()="Личный Кабинет"]'  # меню "Личный кабинет"
    REGISTER_BNT = By.XPATH, './/button[text()="Зарегистрироваться"]'  # кнопка "Зарегистрироваться"
    RECOVER_PASS = By.XPATH, './/a[text()="Восстановить пароль"]'  # пункт "Восстановить пароль"
    RECOVER_PASS_BNT = By.XPATH, './/button[text()="Восстановить"]'  # кнопка "Восстановить пароль"
    LK_PROFILE = By.XPATH, './/a[text()="Профиль"]'  # меню "Профиль" в ЛК
    INCORRECT_PASS = By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]'  # сообщение "Некорректный пароль"
    INCORRECT_PASS_CHECK = By.XPATH, './/fieldset[3]/div/p'  # для проверки сообщения "Некорректный пароль"
    USER_EXISTS = By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]'  # сообщение "Такой пользователь уже существует"
    USER_EXISTS_CHECK = By.XPATH, './/div/main/div/p'  # для проверки сообщения "Такой пользователь уже существует"
    FIELDSET1 = By.XPATH, './/fieldset[1]//input'  # поле для ввода данных
    FIELDSET2 = By.XPATH, './/fieldset[2]//input'  # поле для ввода данных
    FIELDSET3 = By.XPATH, './/fieldset[3]//input'  # поле для ввода данных
    HEADER_H2 = By.XPATH, './/h2'  # любой заголовок h2
    MAKE_BURGER = By.XPATH, './/section[1]/h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер" в конструкторе
    CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]'  # меню "Конструктор"
    ORDER_BNT = By.XPATH, './/button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    SOUSES = By.XPATH, './/span[text()="Соусы"]'  # меню "Соусы"
    NACHINKI = By.XPATH, './/span[text()="Начинки"]'  # список "Соусы"
    BULKI = By.XPATH, './/span[text()="Булки"]'  # меню "Булки"
    SOUSES_CHECK = By.XPATH, './/h2[text()="Соусы"]'  # список "Булки"
    NACHINKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'  # меню "Начинки"
    BULKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'  # список "Начинки"
