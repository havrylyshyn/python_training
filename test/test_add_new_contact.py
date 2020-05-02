# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    phone = string.digits + " " + "(" + ")" + "+" + "-"
    return "".join([random.choice(phone) for i in range(maxlen)])


def random_domain(maxlen):
    symbols = string.ascii_letters
    return "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    email = string.ascii_letters + string.digits + "."
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + random_domain(5)


test_data = [Contact(firstname="", lastname="", address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            address=random_string("address", 30), homephone=random_phone(15), email=random_email(20))
    for i in range(5)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
