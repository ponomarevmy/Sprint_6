from selenium.webdriver.common.by import By
import data


class MainPageLocators:
    # Блок с кнопкой зказа в нижней части главной страцины
    BUTTON_ORDER_CENTER_DIV = [By.CLASS_NAME, "Home_FinishButton__1_cWm"]

    # Нижняя кнопка заказа
    BUTTON_ORDER_CENTER = [By.CLASS_NAME, "Button_Button__ra12g Button_UltraBig__UU3Lp"]

    # Блок "Самокат на пару дней"
    MAIN_TITLE = [By.CLASS_NAME, 'Home_Header__iJKdX']

    # Кнопка "Да все привыкли" куки.
    COOKIE_LOCATOR = [By.ID, "rcc-confirm-button"]

    # Аккордион: 1-8 вопросы и 1-8 ответы
    LIST_0 = [By.ID, 'accordion__heading-0']
    ACCORDION_0 = [By.XPATH, "//div[@id='accordion__panel-0']//p"]
    LIST_1 = [By.ID, 'accordion__heading-1']
    ACCORDION_1 = [By.XPATH, "//div[@id='accordion__panel-1']//p"]
    LIST_2 = [By.ID, 'accordion__heading-2']
    ACCORDION_2 = [By.XPATH, "//div[@id='accordion__panel-2']//p"]
    LIST_3 = [By.ID, 'accordion__heading-3']
    ACCORDION_3 = [By.XPATH, "//div[@id='accordion__panel-3']//p"]
    LIST_4 = [By.ID, 'accordion__heading-4']
    ACCORDION_4 = [By.XPATH, "//div[@id='accordion__panel-4']//p"]
    LIST_5 = [By.ID, 'accordion__heading-5']
    ACCORDION_5 = [By.XPATH, "//div[@id='accordion__panel-5']//p"]
    LIST_6 = [By.ID, 'accordion__heading-6']
    ACCORDION_6 = [By.XPATH, "//div[@id='accordion__panel-6']//p"]
    LIST_7 = [By.ID, 'accordion__heading-7']
    ACCORDION_7 = [By.XPATH, "//div[@id='accordion__panel-7']//p"]
