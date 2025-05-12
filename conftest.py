import pytest
import requests
from urls import Urls
from utils import generate_random_string
from api.courier import CourierApi

@pytest.fixture
def courier():
    courier_data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    response =CourierApi.create(courier_data)
    yield courier_data, response

    # Удаление курьера после прохождения теста
    login_response = CourierApi.login({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if login_response.status_code == 200 and "id" in login_response.json():
        courier_id = login_response.json()["id"]
        CourierApi.delete(courier_id)

