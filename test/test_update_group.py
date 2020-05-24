from model.group import Group
import random


def test_update_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupForUpdate", header="header", footer="footer"))
    old_groups = db.get_group_list()
    group = Group(name="updatedName")
    group_to_update = random.choice(old_groups)
    app.group.update_group_by_id(group, group_to_update.id)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_update)
    group.id = group_to_update.id
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
