from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="Bohdan", lastName="Havrylyshyn", address="UA, Kyiv, KPI", phoneHome="0123456789", email="test@mail.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstName="updatedName", lastName="updatedLastName")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

