from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('A contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()


@given('A contact with <firstname>, <lastname>, <address>, <homephone>, <email>', target_fixture='new_contact')
def new_contact(firstname, lastname, address, homephone, email):
    return Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone, email=email)


@when('Add a new contact')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('The new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, check_ui, app):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
