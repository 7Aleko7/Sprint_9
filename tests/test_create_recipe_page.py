from pages.create_recipe_page import CreateRecipePage
from data import Data
import allure

class TestCreateRecipePage:

    @allure.title('Создание рецепта')
    @allure.description('Заранее созданным и авторизованным пользователем, переходим на страницу создания рецепта, полностью заполнив форму создаем рецепт и проверяем что открылась страница рецепта, в заголовке которой указано корректное название рецепта')
    def test_create_recipe(self,driver, login_user):
        page = CreateRecipePage(driver)
        page.click_on_header_create_recipe_button()
        page.wait_visibility_create_recipe_header()
        page.entering_name(Data.COOKIE_RECIPE['name'])
        page.entering_ingredient(Data.COOKIE_RECIPE['ingredient'])
        page.entering_ingredient_weight(Data.COOKIE_RECIPE['weight'])
        page.click_add_ingredient_button()
        page.entering_cooking_time(Data.COOKIE_RECIPE['time'])
        page.entering_recipe_description(Data.COOKIE_RECIPE['description'])
        page.add_photo(Data.COOKIE_RECIPE['photo'])
        page.click_on_create_recipe_button()
        page.check_create_recipe(Data.COOKIE_RECIPE['name'])