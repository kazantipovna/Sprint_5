import random
import string

# данные пользователя для корректных логинов
name = 'Julia'
email = 'Julia_Zvereva_3666@gmail.com'
password = '1qa2ws'

# список имейлов не по формату для проверки регистрации с корректным имейлом
unform_email = [f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}",
                f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}_{random.randint(1111, 9999)}@gmail."]
