import urls
import allure
import requests
import handlers


class TestChangeUserData:
    @allure.title('Check change user data when authorized')
    def test_change_user_data_authorized(self, register_new_user_and_return_access_token, generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        new_name_and_email = {
                        "email": generate_new_user_data_and_return[0],
                        "name": generate_new_user_data_and_return[1]
                             }
        response = requests.patch(f"{urls.HOME_URL}{handlers.CHANGE_USER_DATA}",
                                 data=new_name_and_email, headers=headers)

        expected_message = True
        assert response.json()["success"] == expected_message
        assert response.status_code == 200

    @allure.title('Check change user data when not authorized')
    def test_change_user_data_not_authorized(self, register_new_user_and_return_access_token,
                                         generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        new_name_and_email = {
            "email": generate_new_user_data_and_return[0],
            "name": generate_new_user_data_and_return[1]
        }
        response = requests.patch(f"{urls.HOME_URL}{handlers.CHANGE_USER_DATA}",
                                  data=new_name_and_email, headers=headers)

        expected_message = True
        assert response.json()["success"] == expected_message
        assert response.status_code == 200
