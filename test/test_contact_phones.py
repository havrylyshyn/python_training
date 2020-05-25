import re
from model.contact import Contact


def test_contact_phones_on_home_page(app, db):
    home_page_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert sorted(home_page_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)
    sorted_home_page_contacts = sorted(home_page_contacts, key=Contact.id_or_max)
    sorted_db_contacts = sorted(db_contacts, key=Contact.id_or_max)
    for i in range(len(sorted_home_page_contacts)):
        assert sorted_home_page_contacts[i].all_emails_from_home_page == merge_emails_like_on_home_page(sorted_db_contacts[i])
        assert sorted_home_page_contacts[i].all_phones_from_home_page == merge_phones_like_on_home_page(sorted_db_contacts[i])


def clear(s):
    s = re.sub("[() -]", "", s)
    if s.startswith("00"):
        s = s.replace("00", "+", 1)
    return s


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                                  contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
