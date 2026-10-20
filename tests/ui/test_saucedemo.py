import pytest

from playwright.sync_api import expect

@pytest.mark.ui
def test_saucedemo_title(page):
    # Открываем сайт в текущей вкладке браузера
    page.goto("https://www.saucedemo.com/")

    # Проверяем, что заголовок вкладки стал "Swag Labs"
    expect(page).to_have_title("Swag Labs")