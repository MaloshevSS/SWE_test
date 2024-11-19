import unittest
import warnings
import re


import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from lib.webdriver_manager.chrome import ChromeDriverManager

from core.report import Report

from conf import URL


class TestCase(unittest.TestCase):

    _report: Report = None

    def setUp(self):
        self.url = URL
        self.addCleanup(self.cleanup)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=self.chromeOptions())
   

        self.driver.maximize_window()
        self.wait_duration = 10
        self.driver.get(self.url)
        self.driver.add_cookie({'name':'COOKIE_CONSENT', 'value':'{"NECESSARY":1,"ANALYTICAL":1,"TARGETING":1}'})
        current_url = self.driver.current_url
        self.driver.get(current_url + '?language=en')

    def cleanup(self):
        # ok = self._get_test_status()

        # if not ok and self._report and self._report.current_step():
        #     print(f"FAIL!!!! Step {self._report.current_step().num} | " +
        #           self._report.current_step().text)
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


    def chromeOptions(self):
        options = Options()
        # options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")  # Bypass OS security model
        options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-gpu")  # Applicable to Windows?
        # options.add_argument("--window-size=1920x1080")  # Set a specific window size
        return options
    

    def get_browser_version(self, browser_name):
        try:
            if browser_name.lower() == 'chrome':
                version = subprocess.check_output(['google-chrome', '--version']).decode('utf-8')
            elif browser_name.lower() == 'firefox':
                version = subprocess.check_output(['firefox', '--version']).decode('utf-8')
            elif browser_name.lower() == 'chromium':
                version = subprocess.check_output(['chromium-browser', '--version']).decode('utf-8')
            else:
                return "Browser not supported."
            
            match = re.search(r'(\d+)\.\d+\.\d+\.\d+', version) 
            if match:
                return match.group(1)
            
        except subprocess.CalledProcessError:
            return f"Error retrieving version for {browser_name}."
        except FileNotFoundError:
            return f"{browser_name} is not installed."