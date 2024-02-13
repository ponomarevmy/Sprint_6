from selenium.webdriver.common.by import By
import data


class BasePageLocators:

    # Логотип scooter
    LOGO_SCOOTER = [By.XPATH, '//img[@alt="Scooter"]']

    # Логотип яндекс
    LOGO_YANDEX = [By.XPATH, '//img[@alt="Yandex"]']

    # Заказать из хэдера
    BUTTON_ORDER_HEADER = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()= "Заказать"]']