import pytest
import requests
import urls
from helpers import Helpers
import handlers

@pytest.fixture()
def register_new_user_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    helpers = Helpers()
    # генерируем логин, пароль и имя курьера
    email = helpers.generate_random_email()
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию нового пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{urls.HOME_URL}{handlers.CREATE_USER}', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список логин и пароль курьера
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    # возвращаем список
    yield login_pass

@pytest.fixture()
def generate_new_user_data_and_return():
    helpers = Helpers()

    # создаём список, чтобы метод мог его вернуть
    user_data = []

    # генерируем логин, пароль и имя курьера
    email = helpers.generate_random_email()
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_name()

    user_data.append(email)
    user_data.append(password)
    user_data.append(name)

    # возвращаем список
    return user_data


@pytest.fixture
def register_new_user_and_return_access_token():
    helpers = Helpers()

    # генерируем логин, пароль и имя курьера
    email = helpers.generate_random_email()
    password = helpers.generate_random_string(10)
    name = helpers.generate_random_name()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию нового пользователя
    response = requests.post(f'{urls.HOME_URL}{handlers.CREATE_USER}', data=payload)

    # если регистрация прошла успешно (код ответа 200), входим пользователя и возвращаем токен
    if response.status_code == 200:
        login_data = {
            "email": email,
            "password": password
        }
        login_response = requests.post(f'{urls.HOME_URL}{handlers.LOGIN_USER}', data=login_data)

        # извлекаем токен из ответа на вход
        token = login_response.json().get("accessToken")
        return token
