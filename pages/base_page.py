from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
    
    def isOpen(self):
        assert self.browser.current_url == self.url

