import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста в инпут')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Ожидание видимости элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ищем заголовок h1 на странице по его тексту')
    def find_h1_on_page(self, find_text):
        element_text = self.driver.find_element(By.XPATH, f".//h1[contains(text(), '{find_text}')]").text
        return element_text