import requests

from constants.constants import Url
from helpers.generators import generate_random_string


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_data(login, password, first_name):

    # создаём словарь, чтобы метод мог его вернуть
    courier_data = {}

    # собираем тело запроса
    payload = {"login": login, "password": password, "firstName": first_name}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{Url.service_url}{Url.create_courier_url}", data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        courier_data["login"] = login
        courier_data["password"] = password
        courier_data["first_name"] = first_name

    # возвращаем словарь
    return courier_data
