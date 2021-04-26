from core.page_object.base import PageObject
from core.testcase import TestCase


class SavingsInvestments(PageObject):
    def __init__(self, tc: TestCase):
        super(SavingsInvestments, self).__init__(tc, ".//*[@data-wt-label='Savings, Investments']", "Savings Investments")
        """
        Describing Saving, Investments tab
        """

    # Checking all elements in the tab
    def check_savings_elements(self):
        MyInvestments(self.tc).check_all_elements()
        NewsInformation(self.tc).check_all_elements()
        Deposits(self.tc).check_all_elements()
        SavingsFunds(self.tc).check_all_elements()
        Securities(self.tc).check_all_elements()

class MyInvestments(PageObject):
    def __init__(self, tc: TestCase):
        super(MyInvestments, self).__init__(tc, ".//*[@label-id='My investments']", "My investments")
        self.my_portfolio = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My portfolio']", PageObject
            )
        self.investment_reports = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Investment reports']", PageObject
            )
        self.investment_advice = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Investment advice']", PageObject
            )
        self.watchlist = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Watchlist']", PageObject
            )
        self.account_statement = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Account statement']", PageObject
            )
        self.new_securities_account = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='New securities account']", PageObject
            )

class NewsInformation(PageObject):
    def __init__(self, tc: TestCase):
        super(NewsInformation, self).__init__(tc, ".//*[@label-id='News and legal information']", "News and legal information")
        self.news_analysis = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='News and Analysis']", PageObject
            )
        self.overview_research = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Overview and research']", PageObject
            )
        self.legal_tax_info = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Legal and tax information']", PageObject
            )

class Deposits(PageObject):
    def __init__(self, tc: TestCase):
        super(Deposits, self).__init__(tc, ".//*[@label-id='Deposits']", "Deposits")
        self.my_deposits = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My deposits']", PageObject
            )
        self.easy_saver = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Easy Saver']", PageObject
            )
        self.saving_deposits = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Savings deposits']", PageObject
            )
        self.term_deposits = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Term deposits']", PageObject
            )

class SavingsFunds(PageObject):
    def __init__(self, tc: TestCase):
        super(SavingsFunds, self).__init__(tc, ".//*[@label-id='Savings and funds']", "Savings and funds")
        self.child_fund = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='A unit-linked life insurance “Safe child fund”']", PageObject
            )
        self.private_portfolio = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Private Portfolio']", PageObject
            )
        self.investment_results = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Results of investment directions']", PageObject
            )
        self.investing_funds = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Investing in funds']", PageObject
            )
        self.investment_funds_list = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Investment funds list']", PageObject
            )

class Securities(PageObject):
    def __init__(self, tc: TestCase):
        super(Securities, self).__init__(tc, ".//*[@label-id='Securities']", "Securities")
        self.stocks = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Stocks']", PageObject
            )
        self.exchange_traded = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Exchange traded funds (ETF)']", PageObject
            )
        self.fixed_securities = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Fixed income securities']", PageObject
            )
        self.government_notes = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Government savings notes']", PageObject
            )
        self.prices_history = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Prices history']", PageObject
            )
        self.corporate_actions = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Corporate Actions, Offers']", PageObject
            )
        self.securities_transfer = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Securities transfer']", PageObject
            )
        self.appropriateness_questionary = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Appropriateness questionnaire']", PageObject
            )
