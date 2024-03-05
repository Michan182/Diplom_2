import urls
import allure
import requests
import handlers


class TestCreateOrder:
    @allure.title('Check get list of order when user authorized')
    def test_get_list_orders_user_authorized(self, register_new_user_and_return_access_token, generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        ingredients_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d"]
        }

        request_order = requests.get(f"{urls.HOME_URL}{handlers.GET_ORDERS}",
                                 data=ingredients_data, headers=headers)

        assert request_order.status_code == 200
        assert 'orders' in request_order.json()

    @allure.title('Check get list of order when user is not authorized')
    def test_get_list_orders_user_is_not_authorized(self):

        request_order = requests.get(f"{urls.HOME_URL}{handlers.GET_ORDERS}")

        expected_message = "You should be authorised"
        assert request_order.json()["message"] == expected_message
        assert request_order.status_code == 401