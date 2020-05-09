from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    phone = string.digits + " " + "(" + ")" + "+" + "-"
    return "".join([random.choice(phone) for i in range(maxlen)])


def random_domain(maxlen):
    symbols = string.ascii_letters
    return "@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    email = string.ascii_letters + string.digits + "."
    return "".join([random.choice(email) for i in range(random.randrange(maxlen))]) + random_domain(5)


test_data = [Contact(firstname="", lastname="", address="", homephone="", email="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            address=random_string("address", 30), homephone=random_phone(15), email=random_email(20))
    for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
