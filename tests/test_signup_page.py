from pages.signup_page import SignupPage
from data import Data
import allure

class TestSignupPage:

    @allure.title('Регистрация пользователя')
    @allure.description('С главной страницы переходим на страницу регистрации, по кнопке Создать аккаунт, и заполнив всю форму создаем аккаунт')
    def test_signup(self, driver, open_login_page):
        name = Data.generate_random_string(5)
        second_name = Data.generate_random_string(5)
        login = Data.generate_random_string(5)
        mail = Data.generate_random_string(7) + '@yandex.ru'
        password = Data.generate_random_string(10)

        page = SignupPage(driver)
        page.click_on_header_signup_button()
        page.signup(name, second_name, login, mail, password)
        page.check_signin_header()