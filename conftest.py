import pytest

from helpers.helpers import *
from helpers.registration import register_new_courier_and_return_login_password

@allure.step("Создаём курьера")
@pytest.fixture(scope="function")
def create_and_delete_courier():
    courier = register_new_courier_and_return_login_password()
    with allure.step('Получаем id для последующего удаления'):
        courier_id = courier_login(courier["login"], courier["password"]).json()["id"]
    yield courier
    delete_courier(courier_id)
