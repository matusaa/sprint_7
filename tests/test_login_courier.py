import allure
import requests
from urls import Urls
from constants import Constants
from utils import generate_random_string
from api.courier import CourierApi

@allure.story("Логин курьера")
class TestLoginCourier:
    @allure.title("Курьер может авторизоваться, успешный запрос возвращает id")
    def test_courier_can_login_and_returns_id(self, courier):
        courier_data, _ = courier
        login_data = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Для авторизации нужны все обязательные поля (нет логина)")
    def test_login_no_login(self, courier):
        courier_data, _ = courier
        login_data = {
            "password": courier_data["password"]
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 400
        assert response.json()["message"] == Constants.LOGIN_DATA_MISSING

    @allure.title("Для авторизации нужны все обязательные поля (нет пароля)")
    def test_login_no_password(self, courier):
        courier_data, _ = courier
        login_data = {
            "login": courier_data["login"]
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}"
        assert response.json()["message"] == Constants.LOGIN_DATA_MISSING

    @allure.title("Система вернёт ошибку, если логин неверный")
    def test_login_wrong_login(self, courier):
        courier_data, _ = courier
        login_data = {
            "login": "test" + courier_data["login"],
            "password": courier_data["password"]
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 404
        assert response.json()["message"] == Constants.USER_NOT_FOUND

    @allure.title("Система вернёт ошибку, если пароль неверный")
    def test_login_wrong_password(self, courier):
        courier_data, _ = courier
        login_data = {
            "login": courier_data["login"],
            "password": "test" + courier_data["password"]
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 404
        assert response.json()["message"] == Constants.USER_NOT_FOUND

    @allure.title("Ошибка, если авторизоваться под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        login_data = {
            "login": generate_random_string(10),
            "password": generate_random_string(4)
        }
        response = CourierApi.login(login_data)
        assert response.status_code == 404
        assert response.json()["message"] == Constants.USER_NOT_FOUND
