# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstName="Bohdan", lastName="Havrylyshyn", address="UA, Kyiv, KPI", phoneHome="0123456789", email="test@mail.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstName="", lastName="", address="", phoneHome="", email=""))
