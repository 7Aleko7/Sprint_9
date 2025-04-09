from pages.login_page import LoginPage
import allure

class TestLoginPage:

    @allure.title('Авторизация пользователя')
    @allure.description('Предварительно создав пользователя, заполняем форму на главной странице и авторизуемся')
    def test_login(self, driver, create_user, open_login_page):
        mail = create_user['mail']
        password = create_user['password']

        page = LoginPage(driver)
        page.login(mail, password)
        page.check_logout_button()