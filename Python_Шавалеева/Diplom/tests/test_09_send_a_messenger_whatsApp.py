import re

import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from components.window_messenger import WindowMessenger


@allure.title("Отправка сообщений WhatsApp")
@allure.description("Тестирование Мессенджера WhatsApp, отправка сообщения")
def test_send_a_messanger(page: Page):
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

    with allure.step("Проверка отображения текстового сообщения, приветствия"):
        expect(window_messenger.get_text_in_window()).to_have_text("Мы здесь, чтобы помочь. Пишите нам WhatsApp по любым вопросам")

    with allure.step("Проверка отображения поля ввода с плейсхолдером"):
        input_field = window_messenger.get_input()
        expect(input_field).to_have_value("Здравствуйте!")

    with allure.step("Проверка отображения кнопок: закрытие и отправка"):
        expect(window_messenger.get_send_button()).to_be_visible()
        expect(window_messenger.get_button_close()).to_be_visible()

    with allure.step("Ввести новый текст"):
        new_text = "Нужна консультация по услуге"
        window_messenger.clear_message(new_text)
        expect(window_messenger.get_input()).to_have_value(new_text)

    with allure.step("Кликнуть на иконку самолетик, для отправки сообщения"):
        with page.context.expect_page() as new_page_info:
            window_messenger.click_button_send()
        new_page = new_page_info.value
        new_page.close()
        # expect(new_page).to_have_url(re.compile(r"^https://api\.whatsapp\.com/"))