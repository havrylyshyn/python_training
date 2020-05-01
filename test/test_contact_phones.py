import re
from random import randrange


def test_contact_phones_on_home_page(app):
    home_page_contacts = app.contact.get_contact_list()
    index = randrange(len(home_page_contacts))
    contact_to_test = home_page_contacts[index]
    edit_form_contact = app.contact.get_contact_from_edit_form(index)
    assert contact_to_test.firstName == edit_form_contact.firstName
    assert contact_to_test.lastName == edit_form_contact.lastName
    assert contact_to_test.address == edit_form_contact.address
    assert contact_to_test.all_phones_from_home_page == merge_phones_like_on_home_page(edit_form_contact)
    assert contact_to_test.all_emails_from_home_page == merge_emails_like_on_home_page(edit_form_contact)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                                  contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
