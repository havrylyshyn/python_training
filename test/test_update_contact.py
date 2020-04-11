from model.contact import Contact


def test_update_first_contact(app):
    app.contact.update_first_contact(Contact(firstName="updatedName", lastName="updatedLastName", address="DE, Berlin", phoneHome="11112222", email="test2@mail.com"))
