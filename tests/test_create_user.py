import urls
import pytest
import allure
import handlers
import requests
from generate_new_user import generate_new_user_data_and_return as gen_data
from generate_new_user import register_new_user_and_return_login_password as registered_data


class TestCreateUser:

    @allure.title('Check user created')
    def test_create_new_user(self):
        user_data = {
            "email": gen_data()[0],
            "password": gen_data()[1],
            "name": gen_data()[2]
        }
        response = requests.post(
            f'{urls.HOME_URL}{handlers.CREATE_USER}',
            data=user_data)
        expected_message = True
        assert response.json()["success"] == expected_message
        assert response.status_code == 200

    @allure.title('Check create user already exist')
    def test_create_user_already_exist(self):
        user_data = {
            "email": registered_data()[0],
            "password": registered_data()[1],
            "name": registered_data()[2]
        }
        response = requests.post(
            f'{urls.HOME_URL}{handlers.CREATE_USER}',
            data=user_data)

        expected_message = "User already exists"
        assert response.json()["message"] == expected_message
        assert response.status_code == 403

    @pytest.mark.parametrize('email, password, name',
                             [
                                 ("", gen_data()[1], gen_data()[2]),
                                 (gen_data()[0], "", gen_data()[2]),
                                 (gen_data()[0], gen_data()[1], ""),
                                 ("", "", "")
                             ]
                             )
    @allure.title('Check create user with missed data')
    def test_try_create_user_with_missed_data(self, email, password, name):
        negative_auth_data = {
            'email': email,
            'password': password,
            'name': name}
        response = requests.post(
            f'{urls.HOME_URL}{handlers.CREATE_USER}',
            data=negative_auth_data)

        expected_message = "Email, password and name are required fields"
        assert response.json()["message"] == expected_message
        assert response.status_code == 403
