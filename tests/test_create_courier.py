import requests
import allure

from helpers.generators import generate_random_string
from constants.constants import Url
from helpers.helpers import delete_courier, courier_login


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Проверка создания курьера без логина")
    def test_create_courier_without_login(self):
        payload = {
            "login": "",
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
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
        payload = {
            "login": generate_random_string(10),
            "password": "",
            "firstName": generate_random_string(10),
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
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": "",
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
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
        }
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
        login = generate_random_string(10)
        payload_1 = {
            "login": login,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
        }
        payload_2 = {
            "login": login,
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
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
