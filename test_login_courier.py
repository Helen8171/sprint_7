import allure
import requests
from urls import Urls
from helpers import CourierGenerator

class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        requests.post(Urls.CREATE_COURIER, json=courier_data)
        payload = {"login": courier_data["login"], "password": courier_data["password"]}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка авторизации без обязательного поля")
    def test_login_courier_missing_field_fails(self, courier_data):
        payload = {"login": courier_data["login"]}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.title("Ошибка авторизации с неправильным паролем")
    def test_login_courier_wrong_password_fails(self, courier_data):
        requests.post(Urls.CREATE_COURIER, json=courier_data)
        payload = {"login": courier_data["login"], "password": "wrong_password123"}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.title("Ошибка авторизации под несуществующим пользователем")
    def test_login_non_existent_courier_fails(self):
        payload = {
            "login": CourierGenerator.generate_random_string(),
            "password": CourierGenerator.generate_random_string()
        }
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")