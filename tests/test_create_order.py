import pytest
import allure

from helpers.helpers import order_create, cancel_order
from test_data.test_data_create_order import Order


@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", Order.scooter_colors)
    @allure.title("Заказ самоката")
    def test_create_order(self, color):
        response = order_create(color)
        order_id = response.json()["track"]
        cancel_order(order_id)
        assert "track" in response.text and response.status_code == 201
