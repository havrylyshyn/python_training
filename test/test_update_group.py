from model.group import Group


def test_update_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="groupForUpdate", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="updatedName")
    group.id = old_groups[0].id
    app.group.update_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
