import requests
from urls import Urls

class CourierApi:
    @staticmethod
    def create(data):
        return requests.post(Urls.CREATE_COURIER_URL, json=data)

    @staticmethod
    def login(data):
        return requests.post(Urls.LOGIN_COURIER_URL, json=data)

    @staticmethod
    def delete(courier_id):
        return requests.delete(f"{Urls.CREATE_COURIER_URL}/{courier_id}")