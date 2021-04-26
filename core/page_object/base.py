import time
from typing import Union

from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from core import testcase


class PageObject:
    el: WebElement = None

    def __init__(self, tc: testcase.TestCase, locator: str, name: str, parent: WebElement = None):
        self.tc = tc
        self.strategy = By.XPATH
        self.locator = locator
        self.name = name
        self.parent = parent

    def get_element_by_selector(self, selector: str, po, locator="", parent=None):
        po_locator = f"element with selector {selector}"
        if locator != "":
            po_locator = locator
        return po(self.tc, selector, po_locator, parent or self.parent)

    def element(self) -> Union[WebElement, list]:
        if self.el is None:
            self.find()
        return self.el

    def click(self, wait: int = None):
        try:
            time.sleep(wait or 0.5)
            self.assert_element_is_clickable()
            self.element().click()
        except WebDriverException:
            self.click_with_offset()

    def click_with_offset(self):
        time.sleep(0.5)
        height_of_screen = self.tc.driver.get_window_size()['height']
        location = self.element().location
        height_of_element = self.element().size['height']
        new_y_offset = (location['y'] // height_of_screen) * height_of_screen + (
                (location['y'] % height_of_screen) - height_of_screen // 2) + height_of_element
        self.tc.driver.execute_script(f'window.scrollTo(0, {new_y_offset})')
        self.element().click()

    def assert_here(self):
        try:
            self.tc.assertTrue(self.find())
        except TimeoutException:
            self.tc.assertTrue(False, f'FAIL! Cannot find element {self.locator}')

    def assert_element_is_clickable(self):
        duration = self.tc.wait_duration
        wait = WebDriverWait(self.parent or self.tc.driver, duration)
        try:
            self.tc.assertTrue(
                wait.until(
                    expected_conditions.element_to_be_clickable((self.strategy, self.locator))
                    )
            )
        except TimeoutException:
            self.tc.assertTrue(False, f'FAIL! Element with {self.locator} is not clickable!')

    def must_no_exists(self, duration=None):
        if duration is None:
            duration = self.tc.wait_duration
        wait = WebDriverWait(self.parent or self.tc.driver, duration)
        try:
            wait.until(
                expected_conditions.invisibility_of_element((self.strategy, self.locator)),
            )
        except TimeoutException:
            self.tc.assertTrue(False, f"FAIL! Element {self.locator} is present at DOM")

    def text(self) -> str:
        return self.element().get_property('textContent')

    def find(self):
        if self.parent:
            try:
                _ = self.parent.text
                driver = self.parent
            except (StaleElementReferenceException, AttributeError):
                driver = self.parent.parent
        else:
            driver = self.tc.driver

        duration = self.tc.wait_duration
        try:
            self.el = WebDriverWait(driver, duration).until(
                expected_conditions.presence_of_element_located((self.strategy, self.locator)),
            )
        except TimeoutException:
            self.tc.assertTrue(False, f'FAIL! Cannot find element with {self.locator}')

        actions = ActionChains(self.tc.driver)
        actions.move_to_element(self.el).perform()

        return self

    def check_all_elements(self):
        all_keys = vars(self)
        not_element_keys = ('tc', 'strategy', 'locator', 'name', 'parent', 'el', 'parent_xpath', 'xpath')
        for key in not_element_keys:
            all_keys.pop(key, None)
        all_elements_in_po = all_keys.values()
        for element in all_elements_in_po:
            if element:
                element.assert_here()

class Field(PageObject):
    def write(self, value):
        pass

    def read(self):
        pass

    def clean(self):
        pass

class Input(Field):

    def write(self, value: str, wait: int = None):
        if not value:
            return
        if wait:
            time.sleep(wait)
        self.element().send_keys(value)

    def write_if_exsist(self, value: str):
        try:
            self.element().clear()
            self.element().send_keys(value)
        except Exception:
            print(f"Cannot write in element {self.locator}")
            pass

    def validation_error_border_only(self) -> PageObject:
        return PageObject(self.tc, "./parent::div[contains(@class, 'TextField__invalid')]",
                          "Validation error field", self.element())

    def clean(self):
        import os
        if 'Darwin' in os.uname():
            self.element().send_keys(Keys.COMMAND + "a")
        else:
            self.element().send_keys(Keys.CONTROL + "a")
        self.element().send_keys(Keys.BACKSPACE)

    def remove_last_char(self):
        self.element().send_keys(Keys.BACKSPACE)

    def get_value(self):
        return self.element().get_property('value')

    def has_value(self):
        if self.element().get_property('value') != '':
            return True
        return False

    def set_value(self, key):
        self.clean()
        self.write(key)


class Checkbox(PageObject):

    # Visible element
    def checkbox(self) -> PageObject:
        return PageObject(self.tc, ".//*[@type='checkbox']", "Checkbox", self.element())

    # Non-visible element, needed for checked/unchecked detection
    def input(self) -> PageObject:
        return PageObject(self.tc, ".//input[@type='checkbox']", "Input element", self.element())


class Select(Field):
    """
     Select for desktop version
    """
    def write(self, value: str):
        self.click()
        el = self.tc.driver.find_element_by_xpath("//div[text()='" + value + "']")
        el.click()

    def write_from_dropdown(self, value: str):
        self.click()
        wait = WebDriverWait(self.parent or self.tc.driver, 20)
        self.el = wait.until(expected_conditions.presence_of_element_located(
            ("xpath", f"//div[contains(@class, 'select-item')][text()='{value}']")))
        actions = ActionChains(self.tc.driver)
        actions.move_to_element(self.el).perform()
        self.el.click()

    def select_by_index(self, value: int):
        btn = self.element().find_element_by_xpath(".//div[starts-with(@class, 'Select__arrow')]")
        btn.click()
        el = self.element().find_element_by_xpath(".//div[starts-with(@class, 'Select__item')][" + str(value) + "]")
        el.click()

    def get_option_count(self):
        el = self.element().find_elements_by_xpath(".//div[starts-with(@class, 'Select__item')]")
        return len(el)

    def get_option_count_two(self):
        el = self.element().find_elements_by_xpath(".//div[starts-with(@data-role, 'selectCard')]")
        return len(el)
