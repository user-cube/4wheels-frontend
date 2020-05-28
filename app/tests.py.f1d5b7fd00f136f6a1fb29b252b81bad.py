# Generated by Selenium IDE*
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
EMAIL = os.getenv('LOGIN_EMAIL')
PASSWORD = os.getenv('LOGIN_PASSWORD')
EMAIL2 = os.getenv('LOGIN_EMAIL2')
PASSWORD2 = os.getenv('LOGIN_PASSWORD2')
# self.driver = webdriver.Chrome(ChromeDriverManager().install())

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
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) #pais").click()
        # 28 | click | css=.form-group:nth-child(5) #pais |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) #pais").click()
        # 29 | doubleClick | css=.form-group:nth-child(5) #pais |
        element = self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(5) #pais")
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
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(4)").click()
        # 37 | click | id=morada |
        self.driver.find_element(By.ID, "morada").click()
        # 38 | click | css=.row |
        self.driver.find_element(By.CSS_SELECTOR, ".row").click()
        # 39 | type | id=morada | Rua dos Doutores
        self.driver.find_element(By.ID, "morada").send_keys("Rua dos Doutores")
        # 40 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 41 | click | css=.form-group:nth-child(1) > .col-lg-6 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(1) > .col-lg-6").click()
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


class TestProfileType():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_profileType(self):
        # Test name: ProfileType
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1052x821 |
        self.driver.set_window_size(1052, 821)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | type | id=id_username |
        self.driver.find_element(By.ID, "id_username").send_keys(EMAIL)
        # 5 | type | id=id_password |
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 6 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 7 | click | id=navbarDefault |
        self.driver.find_element(By.ID, "navbarDefault").click()
        # 8 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 9 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 10 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # 11 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 12 | type | id=id_username |
        self.driver.find_element(By.ID, "id_username").send_keys(EMAIL2)
        # 13 | type | id=id_password |
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD2)
        # 14 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 15 | click | id=navbarDefault |
        self.driver.find_element(By.ID, "navbarDefault").click()
        # 16 | click | linkText=Seller Panel |
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        # 17 | click | css=.thead-dark > tr |
        self.driver.find_element(By.CSS_SELECTOR, ".thead-dark > tr").click()
        # 18 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 19 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class TestAddFavourites():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_addFavourites(self):
        # Test name: AddFavourites
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1052x821 |
        self.driver.set_window_size(1052, 821)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | type | id=id_username
        self.driver.find_element(
            By.ID, "id_username").send_keys(EMAIL)
        # 5 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 6 | type | id=id_password
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 7 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 8 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 9 | click | css=p:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(1)").click()
        # 10 | click | linkText=Home |
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        # 11 | click | linkText=Ver mais |
        self.driver.find_element(By.LINK_TEXT, "Ver mais").click()
        # 12 | click | css=strong |
        self.driver.find_element(By.CSS_SELECTOR, "strong").click()
        # 13 | click | linkText=Favourites |
        self.driver.find_element(By.LINK_TEXT, "Favourites").click()
        # 14 | click | css=.thead-dark > tr |
        self.driver.find_element(By.CSS_SELECTOR, ".thead-dark > tr").click()
        # 15 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # 16 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 17 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class TestSellerPanel():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_sellerPanel(self):
        # Test name: SellerPanel
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1052x824 |
        self.driver.set_window_size(1052, 824)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 6 | click | css=.form-group:nth-child(4) > .col-lg-12 |
        self.driver.find_element(
            By.CSS_SELECTOR, ".form-group:nth-child(4) > .col-lg-12").click()
        # 7 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 8 | type | id=id_password
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 9 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 10 | click | linkText=Seller Panel |
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        # 11 | click | css=.thead-dark > tr |
        self.driver.find_element(By.CSS_SELECTOR, ".thead-dark > tr").click()
        # 12 | click | css=.col-lg-12 |
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-12").click()
        # 13 | click | css=.fa-plus |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
        # 14 | click | linkText=Seller Panel |
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        # 15 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 16 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        # 17 | type | id=id_username |
        self.driver.find_element(
            By.ID, "id_username").send_keys(EMAIL)
        # 18 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()


class TestDeleteCar():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_deleteCar(self):
        # Test name: DeleteCar
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1051x815 |
        self.driver.set_window_size(1051, 815)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | type | id=id_username |
        self.driver.find_element(By.ID, "id_username").send_keys(EMAIL)
        # 5 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 6 | type | id=id_password |
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 7 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 8 | click | linkText=Seller Panel |
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        # 10 | click | css=tr:nth-child(3) .btn-danger |
        self.driver.find_element(
            By.CSS_SELECTOR, "tr:nth-child(3) .btn-danger").click()
        # 11 | assertConfirmation | Are you sure? |
        assert self.driver.switch_to.alert.text == "Are you sure?"
        # 12 | webdriverChooseOkOnVisibleConfirmation |  |
        self.driver.switch_to.alert.accept()
        # 13 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 14 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()


class TestEditCar():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()

    def test_editCar(self):
        # Test name: EditCar
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        # 2 | setWindowSize | 1052x817 |
        self.driver.set_window_size(1052, 817)
        # 3 | click | linkText=Log in |
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | type | id=id_username |
        self.driver.find_element(By.ID, "id_username").send_keys(EMAIL)
        # 6 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        # 7 | type | id=id_password |
        self.driver.find_element(By.ID, "id_password").send_keys(PASSWORD)
        # 8 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 9 | click | linkText=Seller Panel |
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        # 10 | click | css=tr:nth-child(1) .btn-primary > .fa |
        self.driver.find_element(
            By.CSS_SELECTOR, "tr:nth-child(1) .btn-primary > .fa").click()
        # 11 | click | id=model |
        self.driver.find_element(By.ID, "model").click()
        # 12 | type | id=model | Model SS
        self.driver.find_element(By.ID, "model").send_keys("Model SS")
        # 13 | click | css=.btn |
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        # 14 | click | id=navbarDropdown |
        self.driver.find_element(By.ID, "navbarDropdown").click()
        # 15 | click | linkText=Logout |
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

class TestAddCar():
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def tearDown(self) -> None:
        self.driver.quit()
  
    def test_addCar(self):
        self.driver.get("https://tqsfrontendtest.herokuapp.com/")
        self.driver.set_window_size(1053, 819)
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("ruicoelho@ua.pt")
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > .col-lg-12").click()
        self.driver.find_element(By.ID, "id_password").click()
        self.driver.find_element(By.ID, "id_password").send_keys("Abcd1234!")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.LINK_TEXT, "Seller Panel").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fa-plus").click()
        self.driver.find_element(By.ID, "brand").click()
        self.driver.find_element(By.ID, "brand").send_keys("Teste")
        self.driver.find_element(By.ID, "model").click()
        self.driver.find_element(By.ID, "model").send_keys("Teste")
        self.driver.find_element(By.ID, "month").click()
        self.driver.find_element(By.ID, "month").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "model").send_keys("Teste")
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys("0")
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys("Ola Test")
        self.driver.find_element(By.ID, "typeOfFuel").click()
        self.driver.find_element(By.ID, "typeOfFuel").click()
        self.driver.find_element(By.ID, "kilometers").click()
        self.driver.find_element(By.ID, "kilometers").send_keys("0")
        self.driver.find_element(By.ID, "price").click()
        self.driver.find_element(By.ID, "price").send_keys("11600")
        self.driver.find_element(By.ID, "picture").click()
        self.driver.find_element(By.ID, "picture").send_keys("C:\\fakepath\\teslaModelX.jpg")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(2)").click()
        self.driver.find_element(By.ID, "navbarDropdown").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()