import requests
import allure

from helpers.generators import generate_courier_data
from constants.constants import Url
from helpers.helpers import delete_courier, courier_login


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Проверка создания курьера без логина")
    def test_create_courier_without_login(self):
        courier_data = generate_courier_data()
        payload = {
            "login": "",
            "password": courier_data["password"],
            "first_name": courier_data["first_name"],
        }
        with allure.step("Пробуем создать курьера с пустым логином"):
            response = requests.post(
                f"{Url.service_url}{Url.create_courier_url}", data=payload
            )
        response_json = response.json()
        assert response.status_code == 400 and (
            response_json["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Проверка создания курьера без пароля")
    def test_create_courier_without_password(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": "",
            "first_name": courier_data["first_name"],
        }
        with allure.step("Пробуем создать курьера с пустым паролем"):
            response = requests.post(
                f"{Url.service_url}{Url.create_courier_url}", data=payload
            )
        response_json = response.json()

        assert (
            response.status_code == 400
            and response_json["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Проверка создания курьера без имени")
    def test_create_courier_without_first_name(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "first_name": "",
        }
        with allure.step("Пробуем создать курьера с пустым именем"):
            response = requests.post(
                f"{Url.service_url}{Url.create_courier_url}", data=payload
            )
        response_json = response.json()

        courier_id = courier_login(payload["login"], payload["password"]).json()["id"]
        delete_courier(courier_id)

        assert response.status_code == 201 and response_json["ok"] == True

    @allure.title("Проверка создания курьера c корректными данными")
    def test_create_courier(self):
        payload = generate_courier_data()
        with allure.step("Пробуем создать курьера с полным набором корректных данных"):
            response = requests.post(
                f"{Url.service_url}{Url.create_courier_url}", data=payload
            )
        response_json = response.json()
        courier_id = courier_login(payload["login"], payload["password"]).json()["id"]
        delete_courier(courier_id)

        assert response.status_code == 201 and response_json["ok"] == True

    @allure.title("Проверка создания курьера c существующим логином")
    def test_create_courier_duplicate_login(self):

        payload_1 = generate_courier_data()

        courier2_data = generate_courier_data()

        payload_2 = {
            "login": payload_1["login"],
            "password": courier2_data["password"],
            "first_name": courier2_data["first_name"],
        }
        with allure.step(
            "Пробуем создать первого курьера с полным набором корректных данных"
        ):
            requests.post(f"{Url.service_url}{Url.create_courier_url}", data=payload_1)
        with allure.step(
            "Пробуем создать второго курьера с логином, равным логину первого курьера"
        ):
            response = requests.post(
                f"{Url.service_url}{Url.create_courier_url}", data=payload_2
            )
        response_json = response.json()
        courier_id = courier_login(payload_1["login"], payload_1["password"]).json()[
            "id"
        ]
        delete_courier(courier_id)
        assert (
            response.status_code == 409
            and response_json["message"] == "Этот логин уже используется"
        )
