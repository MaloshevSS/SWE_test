from selenium.webdriver.remote.webdriver import WebElement
from core.page_object.base import PageObject
from core.testcase import TestCase
from core.page_object.pages.main_nav.everyday_menu import EverydayMenu
from core.page_object.pages.main_nav.cards import Cards
from core.page_object.pages.main_nav.loan import Loan
from core.page_object.pages.main_nav.savings_investments import SavingsInvestments
from core.page_object.pages.main_nav.pension import Pension
from core.page_object.pages.main_nav.insurance import Insurance



class MainNavigation(PageObject):
    def __init__(self, tc: TestCase, parent: WebElement):
        super(MainNavigation, self).__init__(tc, ".//*[@id='nav-main']", "Main Navigation", parent)
        """
        In this file is described main navigation menu
        and added functions for opening needed tab
        """

        self.home_button = self.get_element_by_selector(f"{self.locator}//*[@type='primary-icon']", PageObject)
        self.everyday_banking = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Everyday banking']", PageObject)
        self.cards = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Cards']", PageObject)
        self.loan = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Loan, leasing']", PageObject)
        self.savings = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Savings, Investments']", PageObject)
        self.pension = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Pension']", PageObject)
        self.insurance = self.get_element_by_selector(f"{self.locator}//*[@data-wt-label='Insurance']", PageObject)
        self.search_button = self.get_element_by_selector(f"{self.locator}//*[@role='search']", PageObject)


    def open_everyday_banking(self):
        self.everyday_banking.click()
        return EverydayMenu(self.tc)

    def open_cards(self):
        self.cards.click()
        return Cards(self.tc)

    def open_loan(self):
        self.loan.click()
        return Loan(self.tc)

    def open_savings_investments(self):
        self.savings.click()
        return SavingsInvestments(self.tc)

    def open_pension(self):
        self.pension.click()
        return Pension(self.tc)

    def open_insurance(self):
        self.insurance.click()
        return Insurance(self.tc)
