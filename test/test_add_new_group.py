# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="1", header="2", footer="3"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
