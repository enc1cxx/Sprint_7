import random
import string


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_data():

    # создаём словарь, чтобы метод мог его вернуть
    courier_data = {}
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data["login"] = login
    courier_data["password"] = password
    courier_data["first_name"] = first_name

    return courier_data