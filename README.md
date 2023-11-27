# Sprint_5
---
#### Тесты на проверку https://stellarburgers.nomoreparties.site/register по заданиям спринта 5

##### Тесты в каталоге tests, файлы:

* __conftest.py__ - фикстуры;
* __data.py__ - общие переменные;
* __helpers.py__ - вспомогательные функции;
* __test_registration.py__ - проверки регистрации пользователя:
    * test_registration_without_pass - без пароля
    * test_registration_without_email - без имейла
    * test_registration_without_name - без имени
    * test_registration_password_less_6_synbols - с паролями <6 символов
    * test_registration_with_incorrect_email - с имейлами не по формату
    * test_registration_correct - корректная регистрация
    * test_registration_with_exist_user - уже существующего пользователя
* __test_login.py__ - проверки логина пользователя:
    * test_login_from_main_page - с главной страницы
    * test_login_from_lk - из ЛК
    * test_login_from_login_page - со страницы логина
    * test_login_after_registration - сразу после регистрации
    * test_login_from_recovery_pass - со страницы восстановления пароля
* __test_lk.py__ - проверки перехода в личный кабинет и выход:
    * test_go_to_lk_from_main - в ЛК с главной
    * test_go_to_constructor_from_lk - из ЛК в конструктор
    * test_logout - выход
* __test_constructor.py__ - проверки перехода к разделам конструктора:
    * test_go_to_souses - переход в соусы
    * test_go_to_nachinki - переход в начинки
    * test_go_to_bulki - переход в будки
