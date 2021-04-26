import unittest
import warnings

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from core.report import Report

from conf import URL


class TestCase(unittest.TestCase):

    _report: Report = None

    def setUp(self):
        self.url = URL
        self.addCleanup(self.cleanup)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait_duration = 10
        self.driver.get(self.url)
        self.driver.add_cookie({'name':'COOKIE_CONSENT', 'value':'{"NECESSARY":1,"ANALYTICAL":1,"TARGETING":1}'})
        current_url = self.driver.current_url
        self.driver.get(current_url + '?language=en')

    def cleanup(self):
        ok = self._get_test_status()

        if not ok and self._report and self._report.current_step():
            print(f"FAIL!!!! Step {self._report.current_step().num} | " +
                  self._report.current_step().text)
        self.driver.quit()


    def _get_test_status(self):
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)

        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)

        return not error and not failure

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]
