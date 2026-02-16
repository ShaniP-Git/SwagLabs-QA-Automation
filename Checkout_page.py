class CheckoutPage:
    def __init__(self, page):
        self.page = page
        # שדות פרטי הלקוח
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        # כפתור הסיום והודעת ההצלחה
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator("[data-test='complete-header']")

    def fill_customer_info(self, first, last, zip_code):
        """מילוי פרטים אישיים והמשך"""
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def click_finish(self):
        """לחיצה על כפתור ה-Finish (הכפתור שלא מגיב ב-error_user)"""
        self.finish_button.click()