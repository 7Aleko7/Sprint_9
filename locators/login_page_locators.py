from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Кнопка Войти, на форме авторизации
    SIGNIN_BUTTON = By.XPATH, ".//button[text()='Войти']"

    # Инпут "Электронная почта"
    INPUT_MAIL= By.XPATH, ".//div[text()='Электронная почта']/parent::label/input"

    # Инпут "Пароль"
    INPUT_PASSWORD = By.XPATH, ".//div[text()='Пароль']/parent::label/input"

    # Кнопка Создать аккаунт в заголовке
    HEADER_SIGNUP_BUTTON = By.XPATH, ".//a[text()='Создать аккаунт']"

    # Заголовок "Войти на сайт"
    SIGNIN_HEADER = By.XPATH, ".//h1[text()='Войти на сайт']"


