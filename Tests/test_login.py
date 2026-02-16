import pytest
from playwright.sync_api import expect
from Page_Object_SwagLabs.Pages.Login_page import LoginPage


class TestLogin:

    def test_valid_login(self, page):
        """TC-01: Verify successful login with standard_user"""
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        # אימות הגעה לעמוד המוצרים
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_invalid_login(self, page):
        """TC-02: Verify error message with locked_out_user"""
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("locked_out_user", "secret_sauce")

        # אימות הודעת השגיאה
        error_text = login_page.get_error_text()
        assert "Sorry, this user has been locked out" in error_text

    def test_problem_user_login(self, page):
        """TC-03: Verify login with problem_user (Functional check)"""
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("problem_user", "secret_sauce")

        # גם משתמש בעייתי מצליח להיכנס, אז אנחנו בודקים URL
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
