from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.create_recipe_page_locators import CreateRecipePageLocators
from selenium.webdriver.common.by import By
import allure

class CreateRecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем Создать рецепт в заголовке страницы')
    def click_on_header_create_recipe_button(self):
        self.click_on_element(MainPageLocators.HEADER_CREATE_RECIPE_BUTTON)

    @allure.step('Ожидаем появления заголовка Создание рецепта')
    def wait_visibility_create_recipe_header(self):
        self.wait_visibility_of_element(CreateRecipePageLocators.CREATE_RECIPE_HEADER)

    @allure.step('Вводим название рецепта')
    def entering_name(self, name):
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_RECIPE_NAME, name)

    @allure.step('Вводим ингредиент в инпут и кликаем на ингредиент в выпадающем списке')
    def entering_ingredient(self, ingredient_name):
        ingredient_button = By.XPATH, f".//div[contains(text(), '{ingredient_name}')]"
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_INGREDIENTS, ingredient_name)
        self.click_on_element(ingredient_button)

    @allure.step('Вводим вес ингредиента')
    def entering_ingredient_weight(self, ingredient_weight):
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_WEIGHT_INGREDIENTS, ingredient_weight)

    @allure.step('Нажимаем добавить ингредиент')
    def click_add_ingredient_button(self):
        self.click_on_element(CreateRecipePageLocators.ADD_INGREDIENTS_BUTTON)

    @allure.step('Вводим время приготовления')
    def entering_cooking_time(self, time):
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_COOKING_TIME, time)

    @allure.step('Вводим описание рецепта')
    def entering_recipe_description(self, description):
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_RECIPE_DESCRIPTION, description)

    @allure.step('Загружаем фото')
    def add_photo(self, photo):
        self.send_keys_to_input(CreateRecipePageLocators.INPUT_ADD_PHOTO, photo)

    @allure.step('Нажимаем Создать рецепт')
    def click_on_create_recipe_button(self):
        self.click_on_element(CreateRecipePageLocators.CREATE_RECIPE_BUTTON)

    @allure.step('Ожидаем открытия страницы рецепта(появление кнопки Редактировать рецепт) и проверяем название рецепта в заголовке')
    def check_create_recipe(self, recipe_name):
        self.wait_visibility_of_element(CreateRecipePageLocators.EDIT_RECIPE_BUTTON)
        assert self.find_h1_on_page(recipe_name)