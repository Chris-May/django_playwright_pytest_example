from playwright.sync_api import expect
import pytest


@pytest.mark.playwright()
def test_can_load_example_page(test_server):
    test_server.screenshot(path='example.png')
    assert 'Sienna' in test_server.content()


@pytest.mark.playwright()
def test_change_a_quanity_and_submit(test_server):
    test_server.locator("#quantity-0").select_option("2")
    test_server.get_by_role("button", name="Checkout").click()
    first_quantity = test_server.locator("#quantity-0")
    expect(first_quantity).to_have_value('1')

