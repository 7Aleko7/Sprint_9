from selenium.webdriver.common.by import By

class SignupPageLocators:

    # Кнопка Создать аккаунт в заголовке
    HEADER_SIGNUP_BUTTON = By.XPATH, ".//a[text()='Создать аккаунт']"

    # Заголовок "Регистрация"
    REGISTER_HEADER= By.XPATH, ".//h1[text()='Регистрация']"

    # Инпут "Имя"
    INPUT_NAME= By.XPATH, ".//div[text()='Имя']/parent::label/input"

    # Инпут "Фамилия"
    INPUT_SECOND_NAME = By.XPATH, ".//div[text()='Фамилия']/parent::label/input"

    # Инпут "Имя пользователя"
    INPUT_LOGIN = By.XPATH, ".//div[text()='Имя пользователя']/parent::label/input"

    # Инпут "Адрес электронной почты"
    INPUT_MAIL = By.XPATH, ".//div[text()='Адрес электронной почты']/parent::label/input"

    # Инпут "Пароль"
    INPUT_PASSWORD = By.XPATH, ".//div[text()='Пароль']/parent::label/input"

    # Кнопка Создать аккаунт в форме
    SIGNUP_BUTTON = By.XPATH, ".//button[text()='Создать аккаунт']"