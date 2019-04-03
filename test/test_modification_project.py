

def test_modification_project(app):
    old_project = app.project.get_project_list()
    app.project.modification()
    new_project = app.project.get_project_list()
    assert len(old_project) == len(new_project)
