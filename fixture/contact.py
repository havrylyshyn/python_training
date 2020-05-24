from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_xpath("//input[@value='Send e-Mail']")

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_xpath("//input[@value='Send e-Mail']")

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # open contact creation page
        wd.find_element_by_link_text("add new").click()
        # input contact data
        self.fill_contact_data(contact)
        # save contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def update_first_contact(self, contact):
        self.update_contact_by_index(0)
        self.contact_cache = None

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contacts_page()
        # select contact
        self.select_contact_by_index(index)
        # open edit page
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_data(contact)
        # save contact
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def update_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.open_contacts_page()
        # select contact
        self.select_contact_by_id(id)
        # open edit page
        wd.find_element_by_xpath("//input[@value='%s']/../..//img[@title='Edit']" % id).click()
        self.fill_contact_data(contact)
        # save contact
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contact_cache = None

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.switch_to_window("")
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.return_to_contacts_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.switch_to_window("")
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.return_to_contacts_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                last_name = element.find_element_by_xpath("td[2]").text
                first_name = element.find_element_by_xpath("td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_xpath("td[4]").text
                allemails = element.find_element_by_xpath("td[5]").text
                allphones = element.find_element_by_xpath("td[6]").text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id, address=address,
                                                  all_emails_from_home_page=allemails,
                                                  all_phones_from_home_page=allphones))
        return list(self.contact_cache)

    def open_contact_edit_form_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_view_form_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def get_contact_from_edit_form(self, index):
        wd = self.app.wd
        self.open_contact_edit_form_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email=email,
                       email2=email2, email3=email3)
