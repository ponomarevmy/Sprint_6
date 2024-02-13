import pytest
import allure
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка создания заказа через header')
    @allure.description('При успешном закаже появляется окно с кнопкой "Проверить статус"')
    @pytest.mark.parametrize('name, surname, address, phone', [*data.RegistrationDetails.reg_data_order])
    def test_order_true(self, driver, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.check_button_order_in_header_is_clickable()
        main_page.click_button_order_header()
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.click_metro_station()
        order_page.check_button_komsomol()
        order_page.click_metro_komsomol_st()
        order_page.set_phone(phone)
        order_page.check_button_next()
        order_page.click_next()
        order_page.check_button_order()
        order_page.click_date()
        order_page.click_today()
        order_page.click_rental_period()
        order_page.click_rental_period_choose()
        order_page.click_black_color()
        order_page.check_button_order()
        order_page.click_button_order()
        order_page.check_button_yes_is_clickable()
        order_page.click_button_yes()
        order_page.check_visibility_of_button_status()
        text_in_button = order_page.text_in_button_status()
        assert text_in_button == 'Посмотреть статус'

    @allure.title('Проверка открытия формы заказа по кнопки заказа внизу страницы')
    def test_button_order_center_div(self, driver):
        main_page = MainPage(driver)
        main_page.check_button_order_is_clickable()
        main_page.click_button_order_div()
        current_url = main_page.get_current_url()
        assert "https://qa-scooter.praktikum-services.ru/order" in current_url
