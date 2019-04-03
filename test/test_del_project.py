

def test__del_project(app):
    # if app.project.count() == 0:
    #     app.project.create()
    old_project = app.project.get_project_list()
    app.project.delete_first_project()
    new_project = app.project.get_project_list()
    assert len(old_project) - 1 == len(new_project)

