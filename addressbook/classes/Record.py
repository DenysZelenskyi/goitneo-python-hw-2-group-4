import Name
from addressbook.classes.Phone import Phone
from addressbook.classes.Name import Name


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        if Phone.validate_phone_number(number):
            self.phones.append(Phone(number))
        else:
            raise ValueError("Invalid phone number format. It should have 10 digits.")