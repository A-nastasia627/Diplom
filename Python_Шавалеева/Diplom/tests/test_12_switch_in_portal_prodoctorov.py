import allure
from playwright.sync_api import Page, expect
from components.cart_profile_doctor import CardProfileDoctor
from controls.link_prodoctorov import LinkProdoctorov
from pages.page_nevrolog import PageNevrolog
from pages.page_prodoctorov import PageProdoctorov


@allure.title("Переход на портал Prodoctorov, со страницы Неврология")
@allure.description("Переход на портал Prodoctorov по ссылке под карточкой врача")
def test_switch_in_portal_prodoctorov(page: Page):
    nevrolog_page = PageNevrolog(page, "Врач-невролог клиники Alimma")
    doctor_name = "Тихонова Ольга Ивановна"
    doctor_card = CardProfileDoctor(page, doctor_name)
    nevrolog_page.open()

    with allure.step("Пролистать статью до заголовка - Врач-невролог клиники Alimma"):
        nevrolog_page.scroll_to_section()

    with allure.step("Проверка отображения заголовка и карточки врача "):
        expect(nevrolog_page.section).to_have_text("Врач-невролог клиники Alimma")
        expect(doctor_card.wrapper).to_be_visible()

    with allure.step("Нажать на ссылку Prodoctorov в карточке врача"):
        prodoctorov_link = LinkProdoctorov(page, doctor_card.wrapper, "Prodoctorov")
        with page.context.expect_page() as new_page_info:
            prodoctorov_link.click()

    with allure.step("Проверка Url страницы"):
        new_page = new_page_info.value
        prodoctorov_page = PageProdoctorov(new_page)
        prodoctorov_page.check_is_prodoctorov()
