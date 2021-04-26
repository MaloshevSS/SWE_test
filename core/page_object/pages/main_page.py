from core.testcase import TestCase

from core.page_object.base import PageObject
from core.page_object.pages.page_header import PageHeader
from core.page_object.pages.main_nav.main_navigation import MainNavigation

class MainPage(PageObject):
    def __init__(self, tc: TestCase):
        super(MainPage, self).__init__(tc, "//body", "Main page")
        """
        here can be placed main page elements,
        also can be added functions to return needed page
        """

    # returning header
    def page_header(self):
        return PageHeader(self.tc, self.element())

    # returning main navigation
    def main_navigation(self):
        return MainNavigation(self.tc, self.element())
