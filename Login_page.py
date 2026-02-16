class LoginPage:
    def __init__(self, page):
        self.page = page
        # לוקייטורים (Locators) - זיהוי האלמנטים לפי ה-data-test של SauceDemo
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """פונקציה לניווט לדף הלוגין"""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        """פונקציה המבצעת לוגין מלא"""
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_text(self):
        """פונקציה להוצאת טקסט השגיאה (בשביל טסטים שליליים)"""
        return self.error_message.inner_text()