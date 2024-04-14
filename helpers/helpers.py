import json
import allure
import requests
from constants.constants import Url
from test_data.test_data_create_order import Order


@allure.step("Логинимся курьером")
def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{Url.service_url}{Url.login_url}", data=payload)
    return response


@allure.step("Удаляем курьера")
def delete_courier(id):
    requests.delete(f"{Url.service_url}{Url.delete_courier_url}{id}")


@allure.step("Отменяем заказ")
def cancel_order(id):
    payload = {"track": id}
    requests.put(f"{Url.service_url}{Url.cancel_order_url}", data=payload)


@allure.step("Создаем заказ")
def order_create(color):
    Order.order_body["color"] = color
    payload = Order.order_body
    response = requests.post(
        f"{Url.service_url}{Url.create_order_url}", data=json.dumps(payload)
    )
    return response
