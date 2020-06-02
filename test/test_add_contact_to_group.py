from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact", lastname="forGroup", address="UA, Kyiv, KPI", homephone="0123456789", email="test@mail.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupForContact", header="header", footer="footer"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact.id, group.id)
    assert object_in_list(contact, db.get_contacts_from_group(group))
#    assert db.get_contacts_from_group(group).__contains__(contact)


def test_add_contact_to_group_2(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact", lastname="forGroup", address="UA, Kyiv, KPI", homephone="0123456789", email="test@mail.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="groupForContact", header="header", footer="footer"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    app.contact.add_contact_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)


def object_in_list(object, list):
    if object in list:
        return True
    else:
        return False
