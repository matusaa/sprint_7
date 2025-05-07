import requests
import allure
from urls import Urls

@allure.story("Список заказов")
@allure.title("В теле ответа возвращается список заказов")
def test_get_orders_returns_list():
    response = requests.get(Urls.ORDER_URL)
    assert response.status_code == 200
    response_json = response.json()
    assert "orders" in response_json
    assert isinstance(response_json["orders"], list)