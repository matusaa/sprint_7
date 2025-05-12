import allure
from constants import Constants
from utils import generate_random_string
from api.courier import CourierApi

@allure.story("Создание курьера")
class TestCreateCourier:
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier):
        courier_data, response = courier
        assert response.status_code == 201
        assert response.json().get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier):
        courier_data, response = courier
        duplicate_response = CourierApi.create(courier_data)
        assert duplicate_response.status_code == 409, \
            f"Ожидался статус 409, получен {duplicate_response.status_code}"
        expected_message = Constants.DUPLICATE_LOGIN
        actual_message = duplicate_response.json().get("message", "")
        assert expected_message == actual_message, \
            f"Ожидалось сообщение '{expected_message}', получено '{actual_message}'"

    @allure.title("Ошибка при создании курьера без логина")
    def test_create_courier_no_password(self):
        courier_data = {
            "password": generate_random_string(4),
            "firstName": generate_random_string(10)
        }
        response = CourierApi.create(courier_data)
        assert response.status_code == 400, \
            f"Ожидался статус 400, получен {response.status_code}"
        expected_message = Constants.LOGIN_DATA_MISSING
        actual_message = response.json()["message"]
        assert actual_message == expected_message

    @allure.title("Ошибка при создании курьера без пароля")
    def test_create_courier_no_password(self):
        courier_data = {
            "login": generate_random_string(4),
            "firstName": generate_random_string(10)
        }
        response = CourierApi.create(courier_data)
        assert response.status_code == 400, \
            f"Ожидался статус 400, получен {response.status_code}"
        expected_message = Constants.LOGIN_DATA_MISSING
        actual_message = response.json()["message"]
        assert response.json()["message"] == Constants.LOGIN_DATA_MISSING

    @allure.title("Ошибка при создании курьера с существующим логином")
    def test_create_courier_existing_login(self, courier):
        courier_data, _ = courier
        new_data = {
            "login": courier_data["login"],
            "password": generate_random_string(4),
            "firstName": generate_random_string(10)
        }
        response = CourierApi.create(new_data)
        assert response.status_code == 409
        assert Constants.DUPLICATE_LOGIN in response.json()["message"]