

def test_add_and_del_project(app):
    app.session.logIn(username="administrator", password="1904")
    app.project.delete_first_project()
    app.session.logOut()