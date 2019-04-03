

def test__del_project(app):
    # if app.project.count() == 0:
    #     app.project.create()
    app.project.delete_first_project()
