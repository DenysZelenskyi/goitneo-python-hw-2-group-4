from dec.dec import input_error
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    @input_error
    def add_record(self, record):
        self.data[record.name] = record

    @input_error
    def find(self, name):
        for record in self.data.values():
            if record.name == name:
                return record
        return None

    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f"Deleted record for {name}")
        else:
            print(f"Record for {name} not found.")