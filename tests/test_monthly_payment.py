from core.testcase import TestCase
from core.page_object.pages.main_page import MainPage
from core.page_object.pages.main_nav.loan import Loans
from core.page_object.pages.mortgage_loan import Calculator

class TestMonthlyPayment(TestCase):
    def __init__(self, *args):
        super(TestMonthlyPayment, self).__init__(*args)
        self.page = MainPage(self)

    def test_monthly_payment(self):
        # Open Navigation menu
        main_nav = self.page.main_navigation()

        # Open Loan tab
        main_nav.open_loan()

        # Open Mortgage loan page
        mortgage_loan_page = Loans(self).open_mortgage_loan_page()
        mortgage_loan_page.assert_here()

        # Fill all required fields in the calculator
        calculator = Calculator(self)
        calculator.more_than_one_dep.click()
        calculator.two_dependants.click()
        calculator.monthly_income.set_value('1000')
        calculator.loan_amount.set_value('45000')
        calculator.loan_term.set_value('132')
        # required to update values from the result table
        calculator.loan_amount.click()

        # Check results
        self.assertEqual(calculator.monthly_loan_payment.get_value(), '386')
        self.assertEqual(calculator.max_loan_amount.get_value(), '49739')
