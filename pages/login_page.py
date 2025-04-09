from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('После ввода почты и пароля нажимаем Войти')
    def login(self, mail, password):
        self.send_keys_to_input(LoginPageLocators.INPUT_MAIL, mail)
        self.send_keys_to_input(LoginPageLocators.INPUT_PASSWORD, password)
        self.click_on_element(LoginPageLocators.SIGNIN_BUTTON)

    @allure.step('Проверяем наличие кнопки Выход')
    def check_logout_button(self):
        assert self.wait_visibility_of_element(MainPageLocators.HEADER_LOGOUT_BUTTON)