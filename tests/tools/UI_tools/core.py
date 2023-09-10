from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class WebDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--kiosk")
        self.chrome_driver = webdriver.Chrome(options=self.options)
        self.actions = ActionChains(self.chrome_driver)
        self.keys = Keys()
        self.chrome_driver.get('https://demoqa.com/login')
        self.im_not_a_robot_checkbox = ("//span[@id='recaptcha-anchor']", "I'm not a robot checkbox")

    def find_web_element(self, element, method=By.XPATH, time=20):
        try:
            WebDriverWait(self.chrome_driver, time).until(EC.element_to_be_clickable((method, element[0])))
            web_element = self.chrome_driver.find_element(method, element[0])
            print(f"The element {element[1]} exists.")
            return web_element
        except NoSuchElementException:
            print(f"The element {element[1]} does not exist.")

    def click_web_element(self, element, method=By.XPATH):
        self.find_web_element(element, method).click()

    def send_text(self, element, text):
        element = self.find_web_element(element)
        element.send_keys(text)

    def refresh_page(self):
        self.chrome_driver.refresh()

    def click_on_recaptcha_checkbox(self):
        WebDriverWait(self.chrome_driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[@title='reCAPTCHA']")))
        WebDriverWait(self.chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

    def press_enter_on_keyboard(self):
        time.sleep(3)
        try:
            self.actions.send_keys(self.keys.ENTER)
            self.actions.perform()
        except:
            pass

    def scroll_down(self):
        self.chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
