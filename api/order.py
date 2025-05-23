import requests
from urls import Urls

class OrderApi:
    @staticmethod
    def create(data):
        return requests.post(Urls.ORDER_URL, json=data)

    @staticmethod
    def get_orders():
        return requests.get(Urls.ORDER_URL)