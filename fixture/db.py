import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DBFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.passwrod = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for raw in cursor:
                (id, name, header, footer) = raw
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook where deprecated = '0000-00-00 00:00:00'")
            for raw in cursor:
                (id, firstname, lastname, address) = raw
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
