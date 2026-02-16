class HomePage:
    def __init__(self, page):
        self.page = page
        # כפתור הוספת התיק (המוצר שנבדוק ב-TC-11 וב-TC-20)
        self.backpack_add_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        # אייקון העגלה למעלה
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_backpack_to_cart(self):
        """פונקציה להוספת התיק לעגלה"""
        self.backpack_add_btn.click()

    def go_to_cart(self):
        """מעבר לעמוד העגלה"""

        self.cart_link.click()
