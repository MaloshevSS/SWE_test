from selenium.webdriver.remote.webdriver import WebElement
from core.page_object.base import PageObject
from core.testcase import TestCase



class PageHeader(PageObject):
    def __init__(self, tc: TestCase, parent: WebElement):
        super(PageHeader, self).__init__(tc, ".//*[@id='header']", "Page Header",
                                     parent)
        """
        in this page can be added action functions with header
        """
        self.swedbank_logo = self.get_element_by_selector(".//*[@id='login-button']", PageObject)
        self.language_bar = self.get_element_by_selector(".//*[@id='language-bar']", PageObject)
        self.new_customer = self.get_element_by_selector(".//*[@class='new-customer-link']", PageObject)
        self.login_button = self.get_element_by_selector(".//*[@id='login-button']", PageObject)
        self.environment = self.get_element_by_selector(".//*[@class='environment']", PageObject)
