# Generated by Selenium IDE*
# from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
import os
import time
EMAIL = os.getenv('LOGIN_EMAIL')
PASSWORD = os.getenv('LOGIN_PASSWORD')

#self.driver = webdriver.Chrome(ChromeDriverManager().install())


class HomepageLoggedOut():
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


class TestSearchBarTest():
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


class TestLogin():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_loginTest(self):
        load_dotenv()
        # Test name: LoginTest
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x849 |
        self.driver.set_window_size(1552, 849)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | type | id=id_username | EMAIL
        self.driver.find_element(By.ID, "id_username").send_keys(
            EMAIL)
        # 5 | type | id=id_password | PASSWORD
        self.driver.find_element(By.ID, "id_password").send_keys(
            PASSWORD)
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


class TestProfile():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_testProfile(self):
        # Test name: TestProfile
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x848 |
        self.driver.set_window_size(1552, 848)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 6 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 7 | doubleClick | id=id_username |
        element = self.driver.find_element(By.ID, "id_username")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 8 | type | id=id_username | mrrmoc@gmail.com
        self.driver.find_element(
            By.ID, "id_username").send_keys(EMAIL)
        # 9 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 10 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 11 | doubleClick | id=id_password |
        element = self.driver.find_element(By.ID, "id_password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 12 | type | id=id_password | 1234
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 13 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 14 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 15 | click | linkText=Perfil |
        self.driver.find_element(By.LINK_TEXT, "Perfil").click()
        # 16 | click | css=.form-group:nth-child(1) > .col-lg-4 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(1) > .col-lg-4").click()
        # 17 | click | css=.form-group:nth-child(2) > .col-lg-4 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(2) > .col-lg-4").click()
        # 18 | click | css=.form-group:nth-child(3) > .col-lg-4 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(3) > .col-lg-4").click()
        # 19 | click | css=.form-group:nth-child(4) > .col-lg-4 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(4) > .col-lg-4").click()
        # 20 | click | css=.col-lg-10 |
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-10").click()
        # 21 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 22 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class TestFavourtiesNone():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_favourtiesNone(self):
        # Test name: FavourtiesNone
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1552x848 |
        self.driver.set_window_size(1552, 848)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 6 | doubleClick | id=id_username |
        element = self.driver.find_element(By.ID, "id_username")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 7 | type | id=id_username | mrrmoc@gmail.com
        self.driver.find_element(
            By.ID, "id_username").send_keys(EMAIL)
        # 8 | type | id=id_password | 1234
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 9 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 10 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 11 | click | css=h1 |
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        # 12 | click | css=p:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").click()


class TestFavouritesExisting():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_favouritesExisting(self):
        # Test name: FavouritesExisting
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1053x817 |
        self.driver.set_window_size(1053, 817)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | css=.row > .col-lg-12:nth-child(1) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".row > .col-lg-12:nth-child(1)").click()
        # 5 | type | id=id_username | mrrmoc@gmail.com
        self.driver.find_element(EMAIL)
        # 6 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 7 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 8 | doubleClick | id=id_password |
        element = self.driver.find_element(By.ID, "id_password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 9 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 10 | type | id=id_password | 1234
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 11 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 12 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 13 | click | css=h1 |
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        # 14 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # 15 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 16 | click | css=.fa-trash |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-trash").click()
        # 17 | click | css=.col-lg-12:nth-child(2) |
        self.driver.find_element(
            By.CSS_SELECTOR, ".col-lg-12:nth-child(2)").click()


class TestEditProfile():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_editProfile(self):
        # Test name: EditProfile
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://localhost:8000/")
        # 2 | setWindowSize | 1052x818 |
        self.driver.set_window_size(1052, 818)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 6 | doubleClick | id=id_username |
        element = self.driver.find_element(By.ID, "id_username")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 7 | type | id=id_username | mrrmoc@gmail.com
        self.driver.find_element(By.ID, "id_username").send_keys(EMAIL)
        # 8 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 9 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 10 | doubleClick | id=id_password |
        element = self.driver.find_element(By.ID, "id_password")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 11 | type | id=id_password | 1234
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 12 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 13 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 14 | click | linkText=Perfil |
        self.driver.find_element(By.LINK_TEXT, "Perfil").click()
        # 15 | click | id=nome |
        self.driver.find_element(By.ID, "nome").click()
        # 16 | click | id=nome |
        self.driver.find_element(By.ID, "nome").click()
        # 17 | doubleClick | id=nome |
        element = self.driver.find_element(By.ID, "nome")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 18 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 19 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 20 | doubleClick | id=morada |
        element = self.driver.find_element(By.ID, "morada")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 21 | click | id=zipcode |
        self.driver.find_element(By.ID, "zipcode").click()
        # 22 | click | id=zipcode |
        self.driver.find_element(By.ID, "zipcode").click()
        # 23 | doubleClick | id=zipcode |
        element = self.driver.find_element(By.ID, "zipcode")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 24 | click | id=pais |
        self.driver.find_element(By.ID, "pais").click()
        # 25 | click | id=pais |
        self.driver.find_element(By.ID, "pais").click()
        # 26 | doubleClick | id=pais |
        element = self.driver.find_element(By.ID, "pais")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 27 | click | css=.form-group:nth-child(5) #pais |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) #pais").click()
        # 28 | click | css=.form-group:nth-child(5) #pais |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) #pais").click()
        # 29 | doubleClick | css=.form-group:nth-child(5) #pais |
        element = self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) #pais")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 30 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 31 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 32 | doubleClick | id=email |
        element = self.driver.find_element(By.ID, "email")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 33 | click | linkText=Editar perfil |
        self.driver.find_element(By.LINK_TEXT, "Editar perfil").click()
        # 34 | click | css=.row |
        self.driver.find_element(By.CSS_SELECTOR, ".row").click()
        # 35 | type | id=name | Rui Coelho
        self.driver.find_element(By.ID, "name").send_keys("Rui Coelho")
        # 36 | click | css=.form-group:nth-child(4) |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4)").click()
        # 37 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 38 | click | css=.row |
        self.driver.find_element(By.CSS_SELECTOR, ".row").click()
        # 39 | type | id=morada | Rua dos Doutores
        self.driver.find_element(By.ID, "morada").send_keys("Rua dos Doutores")
        # 40 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 41 | click | css=.form-group:nth-child(1) > .col-lg-6 |
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .col-lg-6").click()
        # 42 | click | css=.col-lg-10 |
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-10").click()
        # 43 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 44 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 45 | doubleClick | id=morada |
        element = self.driver.find_element(By.ID, "morada")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 46 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 47 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 48 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
