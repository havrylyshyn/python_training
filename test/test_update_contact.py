from model.contact import Contact
import random


def test_update_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Bohdan", lastname="Havrylyshyn", address="UA, Kyiv, KPI",
                                   homephone="0123456789", email="test@mail.com"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="updatedName", lastname="updatedLastName", address="123")
    contact_to_update = random.choice(old_contacts)
    contact.id = contact_to_update.id
    app.contact.update_contact_by_id(contact, contact_to_update.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_update)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
