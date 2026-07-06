import allure
import requests
from urls import Urls
from data import ErrorMessages

class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, courier_data):
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, courier_data):
        requests.post(Urls.CREATE_COURIER, json=courier_data)
        response = requests.post(Urls.CREATE_COURIER, json=courier_data)
        assert response.status_code == 409
        assert ErrorMessages.DUPLICATE_COURIER in response.json().get("message", "")

    @allure.title("Ошибка при создании курьера без обязательного поля")
    def test_create_courier_missing_login_fails(self, courier_data):
        payload = courier_data.copy()
        payload.pop("login")
        response = requests.post(Urls.CREATE_COURIER, json=payload)
        assert response.status_code == 400
        assert ErrorMessages.MISSING_FIELDS_COURIER in response.json().get("message", "")