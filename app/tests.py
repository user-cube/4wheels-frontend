# Generated by Selenium IDE*
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
import os

#self.driver = webdriver.Chrome(ChromeDriverManager().install())


class HomepageLoggedOut(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_untitled(self):
        # Test name: Untitled
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x849 |
        self.driver.set_window_size(1552, 849)
        # 3 | click | id=navbarDefault |
        self.driver.find_element(By.ID, "navbarDefault").click()
        # 4 | click | id=navbarDefault |
        self.driver.find_element(By.ID, "navbarDefault").click()
        # 5 | click | id=navbarDefault |
        self.driver.find_element(By.ID, "navbarDefault").click()
        # 6 | click | css=.navbar |
        self.driver.find_element(By.CSS_SELECTOR, ".navbar").click()
        # 7 | click | css=.navbar > .container |
        self.driver.find_element(
            By.CSS_SELECTOR, ".navbar > .container").click()
        # 8 | click | css=.navbar |
        self.driver.find_element(By.CSS_SELECTOR, ".navbar").click()
        # 9 | click | linkText=Ver mais |
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        # 10 | click | css=.col-lg-12:nth-child(2) th:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(1)").click()
        # 11 | click | css=.col-lg-12:nth-child(2) th:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(1)").click()
        # 12 | doubleClick | css=.col-lg-12:nth-child(2) th:nth-child(1) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 13 | click | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)").click()
        # 14 | click | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)").click()
        # 15 | doubleClick | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 16 | click | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)").click()
        # 17 | click | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)").click()
        # 18 | doubleClick | css=.col-lg-12:nth-child(2) th:nth-child(2) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 19 | click | css=.col-lg-12:nth-child(2) th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(3)").click()
        # 20 | click | css=.col-lg-12:nth-child(2) th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(3)").click()
        # 21 | doubleClick | css=.col-lg-12:nth-child(2) th:nth-child(3) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2) th:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 22 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(1)").click()
        # 23 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(1)").click()
        # 24 | doubleClick | css=.col-lg-12:nth-child(3) > .table th:nth-child(1) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 25 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(2)").click()
        # 26 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(2)").click()
        # 27 | doubleClick | css=.col-lg-12:nth-child(3) > .table th:nth-child(2) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 28 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)").click()
        # 29 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)").click()
        # 30 | doubleClick | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 31 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)").click()
        # 32 | click | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)").click()
        # 33 | doubleClick | css=.col-lg-12:nth-child(3) > .table th:nth-child(3) |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(3) > .table th:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 34 | click | css=th:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").click()
        # 35 | click | css=th:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)").click()
        # 36 | doubleClick | css=th:nth-child(4) |
        element = self.driver.find_element(By.CSS_SELECTOR, "th:nth-child(4)")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 37 | click | css=.card-body |
        self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
        # 38 | click | css=.fa |
        self.driver.find_element(By.CSS_SELECTOR, ".fa").click()


class TestSearchBarTest(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_untitled(self):
        # Test name: Untitled
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x848 |
        self.driver.set_window_size(1552, 848)
        # 3 | click | name=search |
        self.driver.find_element(By.NAME, "search").click()
        # 4 | type | name=search | Tesla
        self.driver.find_element(By.NAME, "search").send_keys("Tesla")
        # 5 | click | css=.example > button |
        self.driver.find_element(By.CSS_SELECTOR, ".example > button").click()
        # 6 | click | css=.col-md-3:nth-child(1) .card-body |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-md-3:nth-child(1) .card-body").click()
        # 7 | click | name=search |
        self.driver.find_element(By.NAME, "search").click()
        # 8 | type | name=search | Model X
        self.driver.find_element(By.NAME, "search").send_keys("Model X")
        # 9 | click | css=input:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(4)").click()
        # 10 | click | css=.example > button |
        self.driver.find_element(By.CSS_SELECTOR, ".example > button").click()
        # 11 | click | css=.card-body |
        self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
        # 12 | click | css=.row |
        self.driver.find_element(By.CSS_SELECTOR, ".row").click()
        # 13 | click | name=search |
        self.driver.find_element(By.NAME, "search").click()
        # 14 | type | name=search | 2020
        self.driver.find_element(By.NAME, "search").send_keys("2020")
        # 15 | click | css=.example |
        self.driver.find_element(By.CSS_SELECTOR, ".example").click()
        # 16 | click | css=input:nth-child(5) |
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(5)").click()
        # 17 | click | css=.example > button |
        self.driver.find_element(By.CSS_SELECTOR, ".example > button").click()
        # 18 | click | css=.col-md-3:nth-child(2) .card-body |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-md-3:nth-child(2) .card-body").click()


class TestLogin(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_loginTest(self):
        import time
        load_dotenv()
        # Test name: LoginTest
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x849 |
        self.driver.set_window_size(1552, 849)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | type | id=id_username | mrrmoc@gmail.com
        self.driver.find_element(By.ID, "id_username").send_keys(
            os.getenv('LOGIN_EMAIL'))
        # 5 | type | id=id_password | 1234
        self.driver.find_element(By.ID, "id_password").send_keys(
            os.getenv('LOGIN_PASSWORD'))
        # 6 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(20)
        # 7 | click | linkText=Ver mais |
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        # 8 | click | css=.card-body |
        self.driver.find_element(By.CSS_SELECTOR, ".card-body").click()
        # 10 | click | css=strong |
        self.driver.find_element(By.CSS_SELECTOR, "strong").click()
        # 11 | assertConfirmation | Are you sure? |
        assert self.driver.switch_to.alert.text == "Are you sure?"
        # 12 | webdriverChooseCancelOnVisibleConfirmation |  |
        self.driver.switch_to.alert.dismiss()
        # 13 | click | css=.fa-envelope |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-envelope").click()
