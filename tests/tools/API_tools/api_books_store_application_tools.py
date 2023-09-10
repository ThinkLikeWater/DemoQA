import requests
import random
import string
import json


class APIBookStoreApplicationTools:
    def __init__(self):
        self.requests = requests.Session()
        self.user_id = None
        self.token = None
        self.login_url = "https://demoqa.com/Account/v1/Authorized"
        self.generate_token_url = "https://demoqa.com/Account/v1/GenerateToken"
        self.create_user_url = "https://demoqa.com/Account/v1/User"
        self.user_url = "https://demoqa.com/Account/v1/User/"
        self.all_books_url = "https://demoqa.com/BookStore/v1/Books"
        self.default_username = "ConstantineTheGreat"
        self.default_password = "ConstantineTheGreat123!"

    def login(self, user_name=None, password=None, status_code=200, *args, **kwargs):
        if not user_name:
            user_name = self.default_username
        if not password:
            password = self.default_password
        data = {
            "userName": user_name,
            "password": password}
        r = self.requests.post(url=self.login_url, data=data)
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"

    def get_token(self, user_name=None, password=None, status_code=200):
        if not user_name:
            user_name = self.default_username
        if not password:
            password = self.default_password
        data = {
            "userName": user_name,
            "password": password}
        r = self.requests.post(url=self.generate_token_url, data=data)
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"
        self.token = json.loads(r.content)['token']

    def create_user(self, user_name, password, status_code=201):
        data = {
            "userName": user_name,
            "password": password
        }
        r = self.requests.post(url=self.create_user_url, data=data)
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"
        self.user_id = json.loads(r.content)['userID']

    def get_user(self, user_name, password, user_id=None, status_code=200):
        user_id = user_id if user_id else self.user_id
        self.get_token(user_name=user_name, password=password)
        r = self.requests.get(self.user_url + user_id, headers={'Authorization': f"Bearer {self.token}"})
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"

    def delete_user(self, user_name, password, user_id=None, status_code=204):
        user_id = user_id if user_id else self.user_id
        self.get_token(user_name=user_name, password=password)
        r = self.requests.delete(self.user_url + user_id, headers={'Authorization': f"Bearer {self.token}"})
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"

    def get_all_books(self, user_name=None, password=None, status_code=200):
        if not user_name:
            user_name = self.default_username
        if not password:
            password = self.default_password
        self.get_token(user_name=user_name, password=password)
        r = self.requests.get(self.all_books_url, headers={'Authorization': f"Bearer {self.token}"})
        assert r.status_code == status_code, f"Actual status code {r.status_code} is not equal to expected {status_code}." \
                                             f"Text error message - {r.text}"

    @staticmethod
    def create_random_string_with_special_symbols():
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = "!@#$%^&*()"

        # Ensure at least one character from each category
        password = random.choice(lowercase_letters)
        password += random.choice(uppercase_letters)
        password += random.choice(digits)
        password += random.choice(special_characters)

        # Choose the remaining characters randomly from all categories
        remaining_length = random.randint(4, 12)  # Ensure the password is at least 8 characters long
        all_characters = lowercase_letters + uppercase_letters + digits + special_characters
        password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

        # Shuffle the password to make it more random
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password
