import requests
import allure
from urls import API_BASE_URL

class StellarBurgersAPI:
    def __init__(self):
        self.base_url = API_BASE_URL

    @allure.step("API: создание пользователя")
    def create_user(self, data):
        response = requests.post(f"{self.base_url}/auth/register", json=data)
        response.raise_for_status()
        return response

    @allure.step("API: авторизация пользователя")
    def login_user(self, email, password):
        response = requests.post(f"{self.base_url}/auth/login",
                               json={"email": email, "password": password})
        response.raise_for_status()
        return response

    @allure.step("API: удаление пользователя")
    def delete_user(self, token):
        headers = {"Authorization": token}
        response = requests.delete(f"{self.base_url}/auth/user", headers=headers)
        response.raise_for_status()
        return response

    @allure.step("API: получение ингредиентов")
    def get_ingredients(self):
        response = requests.get(f"{self.base_url}/ingredients")
        response.raise_for_status()
        return response