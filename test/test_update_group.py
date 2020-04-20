from model.group import Group
from random import randrange


def test_update_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="groupForUpdate", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="updatedName")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.update_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
