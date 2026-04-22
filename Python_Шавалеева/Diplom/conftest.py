import pytest


@pytest.fixture(scope="function")
def page(playwright):
    context = playwright.chromium.launch_persistent_context(
        user_data_dir="/tmp/test-user-data",
        headless=False,
        args=["--start-maximized"],
        no_viewport=True)
    page = context.new_page()

    def close_cookie():
        try:
            cookie_notif = page.locator("#cookie_notification")
            cookie_notif.wait_for(state="visible", timeout=2000)
            if cookie_notif.is_visible():
                accept_button = cookie_notif.locator("button.cookie_accept")
                if accept_button.count() > 0:
                    accept_button.click()
                    cookie_notif.wait_for(state="hidden", timeout=5000)
        except Exception:
            pass
    page.on("load", lambda: close_cookie())

    yield page
    context.close()
