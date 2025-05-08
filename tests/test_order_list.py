import requests
import allure
from urls import Urls
from api.order import OrderApi

@allure.story("Список заказов")
class TestOrderList:
    @allure.title("В теле ответа возвращается список заказов")
    def test_get_orders_returns_list(self):
        response = OrderApi.get_orders()
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)