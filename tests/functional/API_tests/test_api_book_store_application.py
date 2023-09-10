import pytest
from tests.tools.API_tools.api_books_store_application_tools import APIBookStoreApplicationTools


class TestBookStoreApplicationAPI:
    api = None

    @classmethod
    def setup_class(cls):
        cls.api = APIBookStoreApplicationTools()
        cls.api.get_token()

    def test_01_login(self):
        self.api.login()

    def test_02_create_get_and_delete_user(self):
        credentials = self.api.create_random_string_with_special_symbols()
        self.api.create_user(
            user_name=credentials,
            password=credentials)
        self.api.get_user(credentials, credentials)
        self.api.delete_user(credentials, credentials)

    def test_03_get_books(self):
        self.api.get_all_books()
