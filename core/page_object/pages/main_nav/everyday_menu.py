from core.page_object.base import PageObject
from core.testcase import TestCase


class EverydayMenu(PageObject):
    def __init__(self, tc: TestCase):
        super(EverydayMenu, self).__init__(tc, ".//*[@data-wt-label='Everyday banking']", "Everyday banking")
        """
        Describing Everyday banking tab
        """

    # Checking all elements in the tab
    def check_every_day_elements(self):
        AccountInfo(self.tc).check_all_elements()
        Payments(self.tc).check_all_elements()
        DialogBanking(self.tc).check_all_elements()
        EServices(self.tc).check_all_elements()
        DocumentManagement(self.tc).check_all_elements()

class AccountInfo(PageObject):
    def __init__(self, tc: TestCase):
        super(AccountInfo, self).__init__(tc, ".//*[@label-id='Account info']", "Account info")
        self.my_budget = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My Budget']", PageObject
            )
        self.my_finance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='My finances']", PageObject
            )
        self.account_statement = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Account statement']", PageObject
            )
        self.balance = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Balance']", PageObject
            )
        self.add_account = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label=\"Add other bank's accounts\"]", PageObject
            )
        self.service_plans = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Service plans']", PageObject
            )

class Payments(PageObject):
    def __init__(self, tc: TestCase):
        super(Payments, self).__init__(tc, ".//*[@label-id='Payments']", "Payments")
        self.new_payment= self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='New payment']", PageObject
            )
        self.domestic_payments= self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Domestic payments']", PageObject
            )
        self.payments_list = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='List of payments']", PageObject
            )
        self.inter_payment= self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='International payment']", PageObject
            )
        self.incoming_inter_payment= self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Incoming international payments']", PageObject
            )
        self.cart_of_payment= self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Giro and cart of payments']", PageObject
            )
        self.standing_orders = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Standing orders']", PageObject
            )
        self.e_invoices = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='E-invoices']", PageObject
            )
        self.defined_payments = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Defined payments']", PageObject
            )
        self.payment_history = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Payment history']", PageObject
            )
        self.currency_exchange = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Currency exchange']", PageObject
            )
        self.payment_orders = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Payment orders']", PageObject
            )

class DialogBanking(PageObject):
    def __init__(self, tc: TestCase):
        super(DialogBanking, self).__init__(tc, ".//*[@label-id='Digital banking']", "Digital banking")
        self.mobile_app = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Mobile app']", PageObject
            )
        self.notifications = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Notification centre / SMS']", PageObject
            )
        self.security = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Authentication tools and security']", PageObject
            )
        self.electronic_seal = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Electronic seal']", PageObject
            )
        self.payment_limits = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Payment limits and user management']", PageObject
            )
        self.secure_banking = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Secure banking']", PageObject
            )

class EServices(PageObject):
    def __init__(self, tc: TestCase):
        super(EServices, self).__init__(tc, ".//*[@label-id='E-services']", "E-services")
        self.e_state = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='E-State']", PageObject
            )
        self.declaration = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Certificate for declaration']", PageObject
            )

class DocumentManagement(PageObject):
    def __init__(self, tc: TestCase):
        super(DocumentManagement, self).__init__(tc, ".//*[@label-id='Document management']", "Document management")
        self.doc_signing = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Document signing']", PageObject
            )
        self.doc_upload = self.get_element_by_selector(
            f"{self.locator}//*[@data-wt-label='Document upload']", PageObject
            )
