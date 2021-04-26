from core.page_object.base import PageObject
from core.testcase import TestCase


class Insurance(PageObject):
    def __init__(self, tc: TestCase):
        super(Insurance, self).__init__(tc, ".//*[@data-wt-label='Insurance']", "Insurance")
        """
        Describing Insurance tab
        """

    # Checking all elements in the tab
    def check_insurance_elements(self):
        NonLifeInsurance(self.tc).check_all_elements()
        LifeInsurance(self.tc).check_all_elements()
        Accident(self.tc).check_all_elements()

class NonLifeInsurance(PageObject):
    def __init__(self, tc: TestCase):
        super(NonLifeInsurance, self).__init__(tc, ".//*[@label-id='Non-life insurance']", "Non-life insurance")
        self.travel_insurance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Travel insurance']", PageObject
            )
        self.home_insurance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Home insurance']", PageObject
            )
        self.casco_insurance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Casco insurance']", PageObject
            )
        self.credit_card_insurance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Credit card liability insurance']", PageObject
            )
        self.illness_protection = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Illness and unemployment protection']", PageObject
            )

class LifeInsurance(PageObject):
    def __init__(self, tc: TestCase):
        super(LifeInsurance, self).__init__(tc, ".//*[@label-id='Life insurance']", "Life insurance")
        self.my_contracts = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My contracts']", PageObject
            )
        self.life_insurance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Risk life insurance']", PageObject
            )
        self.insurance_safe_child_funds = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='A unit-linked life insurance “Safe child fund”']", PageObject
            )
        self.safe_pension_fund = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Safe pension fund']", PageObject
            )
        self.private_portfolio = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Private Portfolio']", PageObject
            )
        self.results_of_investment = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Results of investment directions']", PageObject
            )
        self.good_to_know = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Good to know']", PageObject
            )

class Accident(PageObject):
    def __init__(self, tc: TestCase):
        super(Accident, self).__init__(tc, ".//*[@label-id='In case of an accident']", "In case of an accident")
        self.report_event = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Report the event']", PageObject
            )
