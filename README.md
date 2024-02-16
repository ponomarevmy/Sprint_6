# Яндекс практикум Sprint_6

<h2> Привет! Это авто-тесты для сайта qa-scooter.praktikum-services.ru </h2>

Проверка перехода на страницы при клике на логотопы в header - `test_click_on_logo.py`
<table>
	<tbody>
		<tr>
			<td>test_logo_redirect_dzen_true</td>
			<td>Проверка переход на "https://dzen.ru/" при клике на логотип Yandex.</td>
		</tr>
		<tr>
			<td>test_logo_go_to_start_page_true</td>
			<td>Проверка перехода на "https://qa-scooter.praktikum-services.ru/" при клике на логотип Самокат.</td>
		</tr>
	</tbody>
</table>

Аккордион на главной странице -  `test_main_page.py`
<table>
	<tbody>
		<tr>
			<td>test_accordion</td>
			<td>Проверка соответствия вопроса и ответа в разделе вопросы о важном.</td>
		</tr>
    </tbody>
</table>

Оформление заказ - `test_order_page.py`
<table>
	<tbody>
		<tr>
			<td>test_order_true</td>
			<td>Проверка создания заказа через header.</td>
		</tr>
        <tr>
			<td>test_button_order_center_div</td>
			<td>Проверка открытия формы заказа по кнопки заказа внизу страницы</td>
		</tr>
	</tbody>
</table>


<h3>Для работы нужны библиотеки:</h3>
<h4>1 - Selenium</h4>
<h4>2 - Pytest</h4>
<h4>3 - Allure</h4>

Запуск тестов `pytest -v`
<br>
Запуск тестов c формированием отчетов `pytest -v  --alluredir=allure_results`
<br>
Посмотреть вэб версию отчета `allure serve allure_results `