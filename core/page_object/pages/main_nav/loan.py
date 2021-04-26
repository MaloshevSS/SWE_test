from core.page_object.base import PageObject
from core.testcase import TestCase
from core.page_object.pages.mortgage_loan import MortgageLoanPage


class Loan(PageObject):
    def __init__(self, tc: TestCase):
        super(Loan, self).__init__(tc, ".//*[@data-wt-label='Loan, leasing']", "Loan")
        """
        Describing Loan tab
        """

    # Checking all elements in the tab
    def check_loan_elements(self):
        Comparison(self.tc).check_all_elements()
        Obligations(self.tc).check_all_elements()
        Loans(self.tc).check_all_elements()
        Leasing(self.tc).check_all_elements()

class Comparison(PageObject):
    def __init__(self, tc: TestCase):
        super(Comparison, self).__init__(tc, ".//*[@label-id='Comparison']", "Comparison")
        self.find_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Find the suitable loan']", PageObject
            )

class Obligations(PageObject):
    def __init__(self, tc: TestCase):
        super(Obligations, self).__init__(tc, ".//*[@label-id='Obligations']", "Obligations")
        self.my_contracts = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My contracts']", PageObject
            )
        self.loan_repayment = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='When loan repayment difficulties are encountered']", PageObject
            )

class Loans(PageObject):
    def __init__(self, tc: TestCase):
        super(Loans, self).__init__(tc, ".//*[@label-id='Loans']", "Loans")
        self.small_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Small loan']", PageObject
            )
        self.home_small_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Home small loan']", PageObject
            )
        self.mortgage_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Mortgage loan']", PageObject
            )
        self.home_energy_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='For home energy efficiency']", PageObject
            )
        self.loan_solar_panels = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Loan for solar panels']", PageObject
            )
        self.application_co_borrower = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Application for co-borrower or surety provider']", PageObject
            )
        self.students_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Students loans']", PageObject
            )
        self.credit_line = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Credit line']", PageObject
            )

    def open_mortgage_loan_page(self):
        self.mortgage_loan.click()
        return MortgageLoanPage(self.tc)

class Leasing(PageObject):
    def __init__(self, tc: TestCase):
        super(Leasing, self).__init__(tc, ".//*[@label-id='Leasing']", "Leasing")
        self.car_financing = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Car financing']", PageObject
            )
        self.car_lease = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Car lease']", PageObject
            )
        self.car_loan = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Car loan']", PageObject
            )
        self.leasing_agreements = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Leasing agreements signing']", PageObject
            )
