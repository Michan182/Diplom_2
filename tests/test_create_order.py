import urls
import allure
import requests
import handlers
import ingredients

class TestCreateOrder:
    @allure.title('Check create order when user authorized')
    def test_create_order_when_user_authorized(self, register_new_user_and_return_access_token, generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        ingredients_data = {
            "ingredients": [ingredients.meat_Protostomia]
        }

        request_order = requests.post(f"{urls.HOME_URL}{handlers.CREATE_ORDER}",
                                 data=ingredients_data, headers=headers)

        assert request_order.status_code == 200
        assert 'order' in request_order.json()

    @allure.title('Check create order when user is not authorized')
    def test_create_order_when_user_is_not_authorized(self):
        ingredients_data = {
            "ingredients": [ingredients.meat_Protostomia, ingredients.sauce_SpicyX]
        }

        request_order = requests.post(f"{urls.HOME_URL}{handlers.CREATE_ORDER}",
                                 data=ingredients_data)

        assert request_order.status_code == 200
        assert 'order' in request_order.json()

    @allure.title('Check create order with ingredients')
    def test_create_order_with_ingredients(self, register_new_user_and_return_access_token, generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        ingredients_data = {
            "ingredients": [ingredients.bun_R2_D3, ingredients.meat_Protostomia, ingredients.sauce_SpicyX]
        }

        request_order = requests.post(f"{urls.HOME_URL}{handlers.CREATE_ORDER}",
                                 data=ingredients_data, headers=headers)

        assert request_order.status_code == 200
        assert 'order' in request_order.json()

    @allure.title('Check create order without ingredients')
    def test_create_order_without_ingredients(self, register_new_user_and_return_access_token,
                                           generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        ingredients_data = {
            "ingredients": []
        }

        request_order = requests.post(f"{urls.HOME_URL}{handlers.CREATE_ORDER}",
                                      data=ingredients_data, headers=headers)

        expected_message = "Ingredient ids must be provided"
        assert request_order.json()["message"] == expected_message
        assert request_order.status_code == 400

    @allure.title('Check create order with wrong ingredients hash')
    def test_create_order_with_wrong_ingredients_hash(self, register_new_user_and_return_access_token,
                                              generate_new_user_data_and_return):
        access_token = register_new_user_and_return_access_token
        headers = {"Authorization": access_token}
        ingredients_data = {
            "ingredients": ["61c0c5a71d1f82001bdaaa43", "61c0c5a71d1f82001bdaaadere", "61c0c5a71d1f82001bdaaa31"]
        }

        request_order = requests.post(f"{urls.HOME_URL}{handlers.CREATE_ORDER}",
                                      data=ingredients_data, headers=headers)

        assert request_order.status_code == 500
        assert 'Error' in request_order.text
