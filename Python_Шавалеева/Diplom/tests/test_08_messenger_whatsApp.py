import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from components.window_messenger import WindowMessenger


@allure.title("Открытие чата WhatsApp")
@allure.description("Тестирование Мессенджера WhatsApp, открытие окна чата, наличие атрибутов")
def test_open_messenger_whatsApp(page: Page):
    main_page = MainPage(page)
    window_messenger = WindowMessenger(page)
    main_page.open_main_page()

    with allure.step("Кликнуть на иконку Мессендера WhatsApp"):
        main_page.messenger_link.get_link_messenger()
        main_page.click_link_messenger()

    with allure.step("Проверка заголовка"):
        expect(window_messenger.get_title()).to_have_text("Алимма")

    with allure.step("Проверка статуса"):
        expect(window_messenger.get_status()).to_contain_text("Online")

    with allure.step("Проверка отображения текстового сообщения приветствия "):
        expect(window_messenger.get_text_in_window()).to_have_text("Мы здесь, чтобы помочь. Пишите нам WhatsApp по любым вопросам")

    with allure.step("Проверка отображения поля ввода с плейсхолдером"):
        input_field = window_messenger.get_input()
        expect(input_field).to_have_value("Здравствуйте!")

    with allure.step("Проверка отображения кнопок: закрытие и отправка"):
        expect(window_messenger.get_send_button()).to_be_visible()
        expect(window_messenger.get_button_close()).to_be_visible()
