from core.page_object.base import PageObject
from core.testcase import TestCase


class Pension(PageObject):
    def __init__(self, tc: TestCase):
        super(Pension, self).__init__(tc, ".//*[@data-wt-label='Pension']", "Pension")
        """
        Describing Pension tab
        """

    # Checking all elements in the tab
    def check_pension_elements(self):
        MyPension(self.tc).check_all_elements()
        PensionII(self.tc).check_all_elements()
        PensionIII(self.tc).check_all_elements()

class MyPension(PageObject):
    def __init__(self, tc: TestCase):
        super(MyPension, self).__init__(tc, ".//*[@label-id='My pension']", "My pension")
        self.my_pension = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My pension']", PageObject
            )

class PensionII(PageObject):
    def __init__(self, tc: TestCase):
        super(PensionII, self).__init__(tc, ".//*[@label-id='II pillar']", "II pillar")
        self.swedbank_pension = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Swedbank pension']", PageObject
            )
        self.pension_funds = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Pension funds results']", PageObject
            )

class PensionIII(PageObject):
    def __init__(self, tc: TestCase):
        super(PensionIII, self).__init__(tc, ".//*[@label-id='III pillar']", "III pillar")
        self.safe_pension = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Safe pension fund']", PageObject
            )
        self.investment_results = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Results of investment directions']", PageObject
            )
        self.pension_funds_results = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Pension funds results']", PageObject
            )
