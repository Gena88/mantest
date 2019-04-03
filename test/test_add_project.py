

def test_add_project(app):
    old_project = app.project.get_project_list()
    app.project.create()
    new_project = app.project.get_project_list()
    assert len(old_project) + 1 == len(new_project)
