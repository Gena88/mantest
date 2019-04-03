from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
import random
import string


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(8)
        self.session = SessionHelper(self)

    def deleteProject(self):
        wd = self.wd
        wd.find_element_by_css_selector(".nav-list > li:nth-child(7) > a:nth-child(1) > span:nth-child(2)").click()
        wd.find_element_by_css_selector(".nav-tabs > li:nth-child(3) > a:nth-child(1)").click()
        wd.find_element_by_css_selector(
            "div.table-responsive:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()
        wd.find_element_by_css_selector("input.btn:nth-child(3)").click()
        wd.find_element_by_css_selector("input.btn").click()

    def createNewProject(self):
        wd = self.wd
        wd.find_element_by_css_selector(".nav-list > li:nth-child(7) > a:nth-child(1) > span:nth-child(2)").click()
        wd.find_element_by_css_selector(".nav-tabs > li:nth-child(3) > a:nth-child(1)").click()
        wd.find_element_by_css_selector(
            "div.widget-box:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > button:nth-child(2)").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("".join(random.choice(string.ascii_letters) for i in range(8)))
        wd.find_element_by_css_selector("input.btn").click()

    # def logIn(self, username, password):
    #     wd = self.wd
    #     self.open_home_page()
    #     wd.find_element_by_name("username").click()
    #     wd.find_element_by_name("username").clear()
    #     wd.find_element_by_name("username").send_keys("%s" % username)
    #     wd.find_element_by_css_selector(".width-40").click()
    #     wd.find_element_by_name("password").click()
    #     wd.find_element_by_name("password").clear()
    #     wd.find_element_by_name("password").send_keys("%s" % password)
    #     wd.find_element_by_css_selector(".width-40").click()
    #
    # def logOut(self):
    #     wd = self.wd
    #     wd.find_element_by_css_selector("i.ace-icon:nth-child(3)").click()
    #     wd.find_element_by_css_selector(".user-menu > li:nth-child(4) > a:nth-child(1)").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-2.20.0/login_page.php")

    def destroy(self):
        self.wd.quit()
