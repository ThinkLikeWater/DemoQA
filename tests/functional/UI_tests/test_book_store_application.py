import unittest
from tests.tools.UI_tools.books_store_application_tools import BookStoreApplicationTools


class BookStoreApplication(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = BookStoreApplicationTools()
        cls.driver.login()

    def test_01_verify_book_store_application_page(self):
        self.driver.find_web_element(self.driver.login_page_button)
        self.driver.find_web_element(self.driver.book_store_page_button)
        self.driver.find_web_element(self.driver.profile_page_button)
        self.driver.find_web_element(self.driver.book_store_api_page_button)

    def test_02_verify_profile_page(self):
        self.driver.verify_books_in_collection(books=False)

    def test_03_add_few_books_to_your_collection(self):
        self.driver.add_book_to_your_collection(["Git Pocket Guide", "Learning JavaScript Design Patterns"])

    def test_04_delete_all_books_from_your_collection(self):
        self.driver.delete_all_books()

    def test_05_logout(self):
        self.driver.logout()
