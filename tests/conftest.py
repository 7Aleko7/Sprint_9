import pytest
from pages.login_page import LoginPage
from urls import Urls
import random
import string
from pages.signup_page import SignupPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Важно для Docker!
    chrome_options.add_argument("--disable-dev-shm-usage")  # Важно для Docker!
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture
def open_login_page(driver):
    driver.get(Urls.LOGIN_URL)

@pytest.fixture
def create_user(driver):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = generate_random_string(5)
    second_name = generate_random_string(5)
    login = generate_random_string(5)
    mail = generate_random_string(7) + '@yandex.ru'
    password = generate_random_string(10)
    creds = {
        "mail": mail,
        "password": password }

    page = SignupPage(driver)
    driver.get(Urls.SIGNUP_URL)
    page.signup(name, second_name, login, mail, password)

    yield creds

@pytest.fixture
def login_user(driver, create_user, open_login_page):
    mail = create_user['mail']
    password = create_user['password']
    page = LoginPage(driver)
    page.login(mail, password)