from model.contact import Contact
from random import randrange


def test_update_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Bohdan", lastname="Havrylyshyn", address="UA, Kyiv, KPI",
                                   homephone="0123456789", email="test@mail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="updatedName", lastname="updatedLastName")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

