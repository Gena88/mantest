import random
import string


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def deleteProject(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".nav-list > li:nth-child(7) > a:nth-child(1) > span:nth-child(2)").click()
        wd.find_element_by_css_selector(".nav-tabs > li:nth-child(3) > a:nth-child(1)").click()
        wd.find_element_by_css_selector(
            "div.table-responsive:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()
        wd.find_element_by_css_selector("input.btn:nth-child(3)").click()
        wd.find_element_by_css_selector("input.btn").click()

    def createNewProject(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".nav-list > li:nth-child(7) > a:nth-child(1) > span:nth-child(2)").click()
        wd.find_element_by_css_selector(".nav-tabs > li:nth-child(3) > a:nth-child(1)").click()
        wd.find_element_by_css_selector(
            "div.widget-box:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > button:nth-child(2)").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("".join(random.choice(string.ascii_letters) for i in range(8)))
        wd.find_element_by_css_selector("input.btn").click()
