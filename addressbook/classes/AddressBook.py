from addressbook.dec.dec import input_error
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    @input_error
    def add_record(self, record):
        self.data[record.name.name] = record

    @input_error
    def find(self, name):
        return self.data.get(name)

    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]