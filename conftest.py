import pytest

from helpers.generators import generate_courier_data
from helpers.helpers import *
from helpers.registration import register_new_courier_and_return_data



@allure.step("Создаём курьера")
@pytest.fixture(scope="function")
def create_and_delete_courier():
    courier_data = generate_courier_data()
    courier = register_new_courier_and_return_data(
        courier_data["login"], courier_data["password"], courier_data["first_name"]
    )
    with allure.step("Получаем id для последующего удаления"):
        courier_id = courier_login(courier["login"], courier["password"]).json()["id"]
    yield courier
    delete_courier(courier_id)
