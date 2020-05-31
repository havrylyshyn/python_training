from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    if len(db.get_group_with_contact_list()) == 0:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="contact", lastname="forGroup", address="UA, Kyiv, KPI", homephone="0123456789", email="test@mail.com"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="groupForContact", header="header", footer="footer"))
        contact = random.choice(db.get_contact_list())
        group = random.choice(db.get_group_list())
        app.contact.add_contact_to_group(contact.id, group.id)
    group_with_contact = random.choice(db.get_group_with_contact_list())
    contact_in_group = random.choice(db.get_contacts_from_group(group_with_contact))
    app.contact.remove_contact_from_group(contact_in_group.id, group_with_contact.id)
    assert object_in_list(contact_in_group, db.get_contacts_from_group(group_with_contact)) is False
#    assert db.get_contacts_from_group(group).__contains__(contact)


def object_in_list(object, list):
    if object in list:
        return True
    else:
        return False
