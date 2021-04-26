from core.page_object.base import Input, PageObject, Checkbox
from core.testcase import TestCase


class MortgageLoanPage(PageObject):
    def __init__(self, tc: TestCase):
        super(MortgageLoanPage, self).__init__(tc, ".//*[@data-wt-page-title='Mortgage loan']", "Mortgage Loan Page")
        """
        Here can be added elements of Mortgage loan page
        and can be added action functions
        """


class Calculator(PageObject):
    def __init__(self, tc: TestCase):
        super(Calculator, self).__init__(tc, ".//*[@id='homeloan-calculator']", PageObject)
        """
        Described Calculator
        Can be added action functions
        """

        # calculator filling elements
        self.co_applicant = self.get_element_by_selector(".//*[@for='borrowersCheck']", Checkbox)
        self.more_than_one_dep = self.get_element_by_selector(".//*[@for='dependantsCheck']", Checkbox)
        self.exiting_loan = self.get_element_by_selector(".//*[@for='obligationsCheck']", Checkbox)
        self.one_dependant = self.get_element_by_selector(".//*[@for='dependants1']", Checkbox)
        self.two_dependants = self.get_element_by_selector(".//*[@for='dependants2']", Checkbox)
        self.monthly_income = self.get_element_by_selector(".//*[@data-wt-label='Total monthly income']//*[@name='income']", Input)
        self.down_payment = self.get_element_by_selector(".//*[@data-wt-label='Down payment']//*[@name='downpayment']", Input)
        self.loan_amount = self.get_element_by_selector(".//*[@data-wt-label='Choose loan amount']//*[@type='text']", Input)
        self.loan_term = self.get_element_by_selector(".//*[@data-wt-label='Choose loan term']//*[@type='text']", Input)
        self.home_loan = self.get_element_by_selector(".//*[@name='home_loan']", Input)
        self.credit_line = self.get_element_by_selector(".//*[@name='credit_line']", Input)
        self.credit_financing = self.get_element_by_selector(".//*[@name='car_financing']", Input)
        self.short_term = self.get_element_by_selector(".//*[@name='short_term']", Input)
        self.monthly_sum = self.get_element_by_selector(".//*[@name='monthly_sum']", Input)

        # calculator result elements
        self.home_insurance_payment = self.get_element_by_selector(".//*[@id='homeInsurancePayment']", Input)
        self.life_insurance_payment = self.get_element_by_selector(".//*[@id='lifeInsurancePayment']", Input)
        self.loan_insurance_payment = self.get_element_by_selector(".//*[@id='loanInsurancePayment']", Input)
        self.monthly_loan_payment = self.get_element_by_selector(".//*[@class='calculator-result']", Input)
        self.max_loan_amount = self.get_element_by_selector(".//*[@id='slider-financed']", Input)
        self.max_home_price = self.get_element_by_selector(".//*[@id='maximumHomePrice']", Input)

        # calculator action buttons
        self.co_applicant_button = self.get_element_by_selector(".//*[@data-wt-label='coapplicant-application-calculator']", PageObject)
        self.fill_application_button = self.get_element_by_selector(".//*[@data-wt-label='fill-application-calculator']", PageObject)
        self.different_options = self.get_element_by_selector(f"{self.locator}//*[@class='default-link']", PageObject)
