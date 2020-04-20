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

    def update_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # select contact
        self.select_first_contact()
        # open edit page
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_data(contact)
        # save contact
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstName)
        self.change_field_value("lastname", contact.lastName)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phoneHome)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.switch_to_window("")
        self.return_to_contacts_page()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contact_list = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            last_name = element.find_element_by_xpath("td[2]").text
            first_name = element.find_element_by_xpath("td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contact_list.append(Contact(firstName=first_name, lastName=last_name, id=id))
        return contact_list
