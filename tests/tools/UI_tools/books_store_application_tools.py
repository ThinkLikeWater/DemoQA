from tests.tools.UI_tools.core import WebDriver
import time

default_username = "ConstantineTheGreat"
default_password = "ConstantineTheGreat123!"


class BookStoreApplicationTools(WebDriver):
    def __init__(self):
        super().__init__()
        self.book_store_application_button_on_mane_page = (
            "//h5[text()='Book Store Application']", "Main page Book Store Application button")
        self.book_store_application = (
            "// *[contains(text(), 'Book Store Application')]", "Book Store Application button")
        self.login_page_button = ("// *[contains(text(), 'Login')]", "Login Page button")
        self.book_store_page_button = ("//span[text()='Book Store']", "Book Store button")
        self.profile_page_button = ("//span[text()='Profile']", "Profile button")
        self.book_store_api_page_button = ("//span[text()='Book Store API']", "Book Store API button")
        self.new_user_button = ("//button[@id='newUser']", "New User button")
        self.first_name_input = ("//input[@id='firstname']", "First Name input")
        self.last_name_input = ("//input[@id='lastname']", "Last Name input")
        self.user_name_input = ("//input[@id='userName']", "User Name input")
        self.password_input = ("//input[@id='password']", "Password input")
        self.register_button = ("//button[@id='register']", "Register button")
        self.login_button = ("//button[@id='login']", "Login button")
        self.logout_button = ("//button[text()='Log out']", "Logout button")
        self.no_books_message = ("//div[text()='No rows found']", "No books in collection")
        self.im_not_a_robot_checkbox = ("//span[@id='recaptcha-anchor']", "I'm not a robot checkbox")
        self.book = ("//a[text()='{}']", "A book")
        self.delete_all_books_button = ("//button[text()='Delete All Books']", "No books in collection")
        self.confirm_to_delete_all_books = ("//button[@id='closeSmallModal-ok']", "Confirm to delete all books")
        self.add_new_book_button = ("//button[text()='Add To Your Collection']", "Add new book button")
        self.back_to_book_store_button = ("//button[text()='Back To Book Store']", "Back to book store button")
        self.book_store_api_swagger = ("//h2[text()='Book Store API']", "Book Store API Swagger")

    def navigate(self, page):
        self.scroll_down()
        if page == "Profile":
            self.click_web_element(self.profile_page_button)
        if page == "Login":
            self.click_web_element(self.login_page_button)
        if page == "Book Store":
            self.click_web_element(self.book_store_page_button)
        if page == "Book Store API":
            self.click_web_element(self.book_store_api_page_button)

    def logout(self):
        self.navigate("Login")
        self.click_web_element(self.logout_button)

    def login(self, username=default_username, password=default_password):
        self.send_text(self.user_name_input, username)
        self.send_text(self.password_input, password)
        self.click_web_element(self.login_button)
        time.sleep(5)
        self.find_web_element(self.logout_button)

    def verify_books_in_collection(self, books):
        self.navigate("Profile")
        if not books:
            self.find_web_element(self.no_books_message)

    def add_book_to_your_collection(self, books):
        self.navigate("Book Store")
        for book in books:
            element = (self.book[0].format(book), self.book[1])
            self.click_web_element(element=element)
            self.scroll_down()
            self.click_web_element(self.add_new_book_button)
            self.press_enter_on_keyboard()
            self.click_web_element(self.back_to_book_store_button)

    def delete_all_books(self):
        self.navigate("Profile")
        self.click_web_element(self.delete_all_books_button)
        self.click_web_element(self.confirm_to_delete_all_books)
        self.press_enter_on_keyboard()

    def verify_book_store_api_page(self):
        self.chrome_driver.get("https://demoqa.com/swagger/")
        self.find_web_element(self.book_store_api_swagger)
