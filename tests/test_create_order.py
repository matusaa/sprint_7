import pytest
import allure
import requests
import copy
from constants import Constants
from urls import Urls
from data import order_colors
from api.order import OrderApi

@allure.story("Создание заказа")
class TestCreateOrder:
    @allure.title("Проверка создания заказа с разными вариантами цвета")
    @pytest.mark.parametrize("order_color", order_colors)
    def test_create_order_with_various_colors(self, order_color):
        order_data = copy.deepcopy(Constants.order_base_data)
        order_data["color"] = order_color
        response = OrderApi.create(order_data)
        assert response.status_code == 201
        assert "track" in response.json(), f"В ответе нет track: {response.json()}"

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        order_data = copy.deepcopy(Constants.order_base_data)
        response = OrderApi.create(order_data)
        assert response.status_code == 201
        assert "track" in response.json(), f"В ответе нет track: {response.json()}"