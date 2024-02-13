import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Проверяем кликабельность кнопки заказа из header')
    def check_button_order_in_header_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Проверяем кликабельность кнопки заказа внизу страницы')
    def check_button_order_is_clickable(self):
        self.check_element_is_clickable(MainPageLocators.BUTTON_ORDER_CENTER_DIV)

    @allure.step('Проверяем кликабельность логотипа "Yandex"')
    def check_logo_yandex_is_clickable(self):
        self.check_element_is_clickable(BasePageLocators.LOGO_YANDEX)

    @allure.step('Кликаем по лого яндекса')
    def click_logo_yandex(self):
        self.click_on_element(BasePageLocators.LOGO_YANDEX)

    @allure.step('Кликаем по кнопке "Заказать" в header')
    def click_button_order_header(self):
        self.click_on_element(BasePageLocators.BUTTON_ORDER_HEADER)

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_button_order_div(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDER_CENTER_DIV)

    @allure.step('Кликаем по лого самоката')
    def click_logo_scooter(self):
        self.click_on_element(BasePageLocators.LOGO_SCOOTER)
