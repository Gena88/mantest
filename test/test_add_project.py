

def test_add_project(app):
    app.session.logIn(username="administrator", password="1904")
    app.project.create()
    app.session.logOut()