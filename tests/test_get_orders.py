import allure
import requests
from urls import Urls

class TestGetOrders:
    @allure.title("Получение списка заказов")
    def test_get_orders_list_success(self):
        response = requests.get(Urls.ORDERS)
        assert response.status_code == 200
        assert type(response.json().get("orders")) == list