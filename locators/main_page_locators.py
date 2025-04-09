from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка Выход в хэдере
    HEADER_LOGOUT_BUTTON = By.XPATH, ".//a[text()='Выход']"

    # Кнопка Создать рецепт в хэдере
    HEADER_CREATE_RECIPE_BUTTON = By.XPATH, ".//a[text()='Создать рецепт']"