


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def logIn(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("%s" % username)
        wd.find_element_by_css_selector(".width-40").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("%s" % password)
        wd.find_element_by_css_selector(".width-40").click()

    def logOut(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("i.ace-icon:nth-child(3)").click()
        wd.find_element_by_css_selector(".user-menu > li:nth-child(4) > a:nth-child(1)").click()