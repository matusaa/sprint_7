import allure
import requests
import copy
from constants import Constants
from urls import Urls

@allure.story("Создание заказа")
@allure.title("Проверка создания заказа с разными вариантами цвета")
def test_create_order_with_various_colors(order_color):
    order_data = copy.deepcopy(Constants.order_base_data)
    if order_color is not None:
        order_data["color"] = order_color
    response = requests.post(Urls.ORDER_URL, json=order_data)
    print(response.json())
    assert response.status_code == 201
    assert "track" in response.json(), f"В ответе нет track: {response.json()}"