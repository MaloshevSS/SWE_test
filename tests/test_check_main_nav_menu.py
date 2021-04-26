from core.testcase import TestCase
from core.page_object.pages.main_page import MainPage


class TestMainNavCheck(TestCase):
    def __init__(self, *args):
        super(TestMainNavCheck, self).__init__(*args)
        self.page = MainPage(self)

    def test_main_nav_check(self):
        main_nav = self.page.main_navigation()

        # Checking everyday banking elements
        everyday_banking = main_nav.open_everyday_banking()
        everyday_banking.check_every_day_elements()

        # Checking cards elements
        cards = main_nav.open_cards()
        cards.check_cards_elements()

        # Checking loan elements
        loan = main_nav.open_loan()
        loan.check_loan_elements()

        # Checking savings elements
        savings = main_nav.open_savings_investments()
        savings.check_savings_elements()

        # Checking pension elements
        pension = main_nav.open_pension()
        pension.check_pension_elements()

        # Checking insurance elements
        insurance = main_nav.open_insurance()
        insurance.check_insurance_elements()

        # Checking main navigation elements
        main_nav.check_all_elements()
