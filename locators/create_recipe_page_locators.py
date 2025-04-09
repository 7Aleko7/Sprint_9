from selenium.webdriver.common.by import By


class CreateRecipePageLocators:

    # Заголовок "Создание рецепта"
    CREATE_RECIPE_HEADER = By.XPATH, ".//h1[text()='Создание рецепта']"

    # Инпут "Название рецепта"
    INPUT_RECIPE_NAME = By.XPATH, ".//div[text()='Название рецепта']/parent::label/input"

    # Инпут "Ингредиенты"
    INPUT_INGREDIENTS = By.XPATH, ".//div[text()='Ингредиенты']/parent::label/input"

    # Инпут вес ингредиента
    INPUT_WEIGHT_INGREDIENTS = By.XPATH, ".//div[2]/div/label/input"

    # Кнопка "Добавить ингредиент"
    ADD_INGREDIENTS_BUTTON = By.XPATH, ".//div[text()='Добавить ингредиент']"

    # Инпут "Время приготовления"
    INPUT_COOKING_TIME = By.XPATH, ".//div[text()='Время приготовления']/parent::label/input"

    # Инпут "Описание рецепта"
    INPUT_RECIPE_DESCRIPTION = By.XPATH, ".//div[text()='Описание рецепта']/parent::label/textarea"

    # Инпут добавления фотографии
    INPUT_ADD_PHOTO = By.XPATH, "//input[@type='file']"

    # Кнопка Создать рецепт в форме
    CREATE_RECIPE_BUTTON = By.XPATH, ".//button[text()='Создать рецепт']"

    # Заголовок "Редактировать рецепт"
    EDIT_RECIPE_BUTTON = By.XPATH, ".//a[text()='Редактировать рецепт']"





