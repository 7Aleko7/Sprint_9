from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators
from locators.login_page_locators import LoginPageLocators
import allure

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку Создать аккаунт в заголовке страницы')
    def click_on_header_signup_button(self):
        self.click_on_element(SignupPageLocators.HEADER_SIGNUP_BUTTON)

    @allure.step('После ввода всех данных в форму регистрации нажимаем Создать аккаунт')
    def signup(self, name, second_name, login, mail, password):
        self.send_keys_to_input(SignupPageLocators.INPUT_NAME, name)
        self.send_keys_to_input(SignupPageLocators.INPUT_SECOND_NAME, second_name)
        self.send_keys_to_input(SignupPageLocators.INPUT_LOGIN, login)
        self.send_keys_to_input(SignupPageLocators.INPUT_MAIL, mail)
        self.send_keys_to_input(SignupPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(SignupPageLocators.SIGNUP_BUTTON)

    @allure.step('Проверяем наличие заголовка Войти на сайт')
    def check_signin_header(self):
        assert self.wait_visibility_of_element(LoginPageLocators.SIGNIN_HEADER)