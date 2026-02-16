class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")

    def proceed_to_checkout(self):
        """לחיצה על כפתור ה-Checkout בעגלה"""
        self.checkout_button.click()