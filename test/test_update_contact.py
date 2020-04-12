from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName="Bohdan", lastName="Havrylyshyn", address="UA, Kyiv, KPI", phoneHome="0123456789", email="test@mail.com"))
    app.contact.update_first_contact(Contact(firstName="updatedName", lastName="updatedLastName", address="DE, Berlin", phoneHome="11112222", email="test2@mail.com"))
