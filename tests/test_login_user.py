import urls
import allure
import requests
import handlers


class TestLoginUser:
    @allure.title('Check user authorisation')
    def test_user_authorisation(self, register_new_user_and_return_login_password):
        reg_data = {
            "email": register_new_user_and_return_login_password[0],
            "password": register_new_user_and_return_login_password[1]
        }
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_USER}",
                                 data=reg_data)
        expected_message = True
        assert response.json()["success"] == expected_message
        assert response.status_code == 200

    @allure.title('Check user authorisation with wrong password and login')
    def test_user_authorisation_with_wrong_data(self, generate_new_user_data_and_return):
        reg_data = {
            "email": generate_new_user_data_and_return[0],
            "password": generate_new_user_data_and_return[1]
        }
        response = requests.post(f"{urls.HOME_URL}{handlers.LOGIN_USER}",
                                 data=reg_data)
        expected_message = "email or password are incorrect"
        assert response.json()["message"] == expected_message
        assert response.status_code == 401
