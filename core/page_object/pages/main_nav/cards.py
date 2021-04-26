from core.page_object.base import PageObject
from core.testcase import TestCase


class Cards(PageObject):
    def __init__(self, tc: TestCase):
        super(Cards, self).__init__(tc, ".//*[@data-wt-label='Cards']", "Cards")
        """
        Describing Cards tab
        """

    # Checking all elements in the tab
    def check_cards_elements(self):
        CardManagement(self.tc).check_all_elements()
        CardsMenu(self.tc).check_all_elements()
        DigitalWallets(self.tc).check_all_elements()

class CardManagement(PageObject):
    def __init__(self, tc: TestCase):
        super(CardManagement, self).__init__(tc, ".//*[@label-id='Card management']", "Card management")
        self.my_cards = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My cards']", PageObject
            )
        self.internet_shoping = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Internet shopping']", PageObject
            )

class CardsMenu(PageObject):
    def __init__(self, tc: TestCase):
        super(CardsMenu, self).__init__(tc, ".//*[@label-id='Cards']", "Cards Menu")
        self.debit_cards = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Debit cards']", PageObject
            )
        self.credit_cards = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Credit cards']", PageObject
            )

class DigitalWallets(PageObject):
    def __init__(self, tc: TestCase):
        super(DigitalWallets, self).__init__(tc, ".//*[@label-id='Digital wallets']", "Digital wallets")
        self.google_play = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Google Pay™']", PageObject
            )
        self.apple_play = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Apple Pay']", PageObject
            )
        self.mobile_payment = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Mobile contactless payments (Android)']", PageObject
            )
        self.garmin_pay = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Mobile contactless payments (Android)']", PageObject
            )
        self.manage_mii = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Fidesmo, Manage-Mii']", PageObject
            )
