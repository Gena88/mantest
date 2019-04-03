from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
import random
import string


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(8)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)





    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-2.20.0/login_page.php")

    def destroy(self):
        self.wd.quit()
