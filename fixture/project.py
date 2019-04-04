import random
import string


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def delete_first_project(self):
        wd = self.app.wd
        self.open_project_page()
        self.select_project()
        wd.find_element_by_css_selector("input.btn:nth-child(3)").click()
        wd.find_element_by_css_selector("input.btn").click()

    def select_project(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            "div.table-responsive:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(1)").click()

    def create(self):
        wd = self.app.wd
        self.open_project_page()
        self.open_create_project_page()
        self.fill_element(name="name", text_element="".join(random.choice(string.ascii_letters) for i in range(8)))
        wd.find_element_by_css_selector("input.btn").click()

    def fill_element(self, name, text_element):
        wd = self.app.wd
        wd.find_element_by_name("%s" % name).click()
        wd.find_element_by_name("%s" % name).clear()
        wd.find_element_by_name("%s" % name).send_keys(text_element)

    def modification(self):
        wd = self.app.wd
        self.open_project_page()
        self.select_project()
        self.fill_element(name="name", text_element= "Скорректированный" + " - " + "".join(random.choice(string.ascii_letters) for i in range(8)))
        wd.find_element_by_css_selector(
            "#manage-proj-update-form > div:nth-child(1) > div:nth-child(3) > input:nth-child(2)").click()



    def open_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            "div.widget-box:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > fieldset:nth-child(1) > button:nth-child(2)").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".fa-gears").click()
        wd.find_element_by_css_selector(".nav-tabs > li:nth-child(3) > a:nth-child(1)").click()

    # def count(self):
    #     wd = self.app.wd
    #     wd

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        list_project = []
        for element in wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id')]"):
            list_project.append(element)
        return list_project