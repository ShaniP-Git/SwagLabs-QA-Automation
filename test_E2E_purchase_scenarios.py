import pytest
from playwright.sync_api import expect
from Page_Object_SwagLabs.Pages.Login_page import LoginPage
from Page_Object_SwagLabs.Pages.Home_page import HomePage
from Page_Object_SwagLabs.Pages.Cart_page import CartPage
from Page_Object_SwagLabs.Pages.Checkout_page import CheckoutPage


class TestE2EPurchaseScenarios:

    # --- TC-07: Happy Path (זרימה חיובית מלאה) ---
    def test_tc11_standard_user_e2e_flow(self, page):
        """E2E Scenario: Complete purchase from login to finish message"""
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        home_page.add_backpack_to_cart()
        home_page.go_to_cart()

        cart_page.proceed_to_checkout()

        checkout_page.fill_customer_info("Shani", "Peretz", "12345")
        checkout_page.click_finish()

        expect(checkout_page.complete_header).to_contain_text("Thank you for your order")

    # --- TC-08: Negative Scenario (בדיקת שגיאות בצ'קאאוט) ---
    def test_tc14_checkout_form_validations(self, page):
        """Negative Scenario: Verify system prevents checkout with missing info"""
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")
        home_page.add_backpack_to_cart()
        home_page.go_to_cart()
        cart_page.proceed_to_checkout()

        # ניסיון להמשיך ללא מילוי פרטים
        checkout_page.continue_button.click()

        error_locator = page.locator("[data-test='error']")
        expect(error_locator).to_be_visible()
        assert "First Name is required" in error_locator.inner_text()

    # --- TC-11: Inventory Manipulation (ניהול עגלה) ---
    def test_tc19_cart_item_removal_sync(self, page):
        """Functional Scenario: Add item and remove it, verify cart badge updates"""
        login_page = LoginPage(page)
        home_page = HomePage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        home_page.add_backpack_to_cart()
        # הסרת המוצר מהעגלה ישירות מדף הבית
        remove_btn = page.locator("[data-test='remove-sauce-labs-backpack']")
        remove_btn.click()

        # אימות שהעגלה התעדכנה ל-0 (האייקון נעלם)
        cart_badge = page.locator("[data-test='shopping-cart-badge']")
        expect(cart_badge).not_to_be_visible()

    # --- TC-20: Bug Reproduction (שחזור באג קריטי) ---
    def test_tc20_error_user_finish_action_failure(self, page):
        """Bug Scenario: Verify error_user is blocked on the final 'Finish' action"""
        login_page = LoginPage(page)
        home_page = HomePage(page)
        cart_page = CartPage(page)
        checkout_page = CheckoutPage(page)

        login_page.navigate()
        login_page.login("error_user", "secret_sauce")

        home_page.add_backpack_to_cart()
        home_page.go_to_cart()
        cart_page.proceed_to_checkout()
        checkout_page.fill_customer_info("Shani", "Peretz", "12345")

        # כאן קורה הבאג - הכפתור נלחץ אך לא מעביר עמוד
        checkout_page.click_finish()

        # האוטומציה נכשלת כאן בצדק, מה שמוכיח את קיום הבאג
        expect(checkout_page.complete_header).to_be_visible(timeout=5000)