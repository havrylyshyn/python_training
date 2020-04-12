from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="groupForDeleting", header="header", footer="footer"))
    app.group.update_first_group(Group(name="updatedName", header="updatedHeader", footer="updatedFooter"))