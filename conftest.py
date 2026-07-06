import pytest
import requests
from urls import Urls
from helpers import CourierGenerator

@pytest.fixture
def courier_data():
    data = CourierGenerator.get_random_courier_data()
    yield data
    login_payload = {"login": data["login"], "password": data["password"]}
    login_response = requests.post(Urls.LOGIN_COURIER, json=login_payload)
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        requests.delete(f"{Urls.CREATE_COURIER}/{courier_id}")