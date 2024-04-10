import requests

from helpers.generators import generate_random_string


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():

    # создаём список, чтобы метод мог его вернуть
    login_pass = {}

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {"login": login, "password": password, "firstName": first_name}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(
        "https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload
    )

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        # login_pass.append(login)
        # login_pass.append(password)
        # login_pass.append(first_name)

        login_pass["login"] = login
        login_pass["password"] = password
        login_pass["first_name"] = first_name

    # возвращаем список
    return login_pass
