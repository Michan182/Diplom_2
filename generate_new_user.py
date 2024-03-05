import requests
from faker import Faker
import string
import random

def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email():
        fake = Faker()
        return fake.email()

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию нового пользователя и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль курьера
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    # возвращаем список
    return login_pass

def generate_new_user_data_and_return():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email():
        fake = Faker()
        return fake.email()

    def generate_random_name():
        fake = Faker()
        return fake.name()

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_email()
    password = generate_random_string(10)
    name = generate_random_name()

    user_data.append(email)
    user_data.append(password)
    user_data.append(name)

    # возвращаем список
    return user_data
