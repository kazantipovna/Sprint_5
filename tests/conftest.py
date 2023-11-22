import random
import string

# данные пользователя для корректных логинов
name = 'Julia'
email = 'Julia_Zvereva_3666@gmail.com'
password = '1qa2ws'


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


def random_short_pass():
    passwords = [''.join(random.sample(string.ascii_letters + string.digits, 1)),
                 ''.join(random.sample(string.ascii_letters + string.digits, 2)),
                 ''.join(random.sample(string.ascii_letters + string.digits, 3)),
                 ''.join(random.sample(string.ascii_letters + string.digits, 4)),
                 ''.join(random.sample(string.ascii_letters + string.digits, 5))]
    return passwords


def unformatted_emails():
    emails = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}",
              f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@",
              f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail",
              f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail."]
    return emails
