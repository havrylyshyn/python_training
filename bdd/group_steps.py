from pytest_bdd import given, when, then
from model.group import Group
import random


@given('A group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given('A group with <name>, <header>, <footer>', target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('Add a new group')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('The new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


@given('A non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupForDeleting", header="header", footer="footer"))
    return db.get_group_list()


@given('A random group', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('Delete a group')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('The new group list is equal to the old list without deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, check_ui, app):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert new_groups == old_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@given('A group data', target_fixture='group_data')
def group_data():
    return Group(name="updatedName")


@when('Update a group')
def update_group(app, random_group, group_data):
    app.group.update_group_by_id(group_data, random_group.id)


@then('The new group list is equal to the old list with updated group')
def verify_group_updated(app, db, non_empty_group_list, random_group, group_data, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    group_data.id = random_group.id
    old_groups.append(group_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
