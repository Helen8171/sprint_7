import allure
import pytest
import requests
from urls import Urls

class TestCreateOrder:
    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_create_order_colors(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(Urls.ORDERS, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()