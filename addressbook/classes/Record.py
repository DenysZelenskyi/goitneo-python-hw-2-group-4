from .Name import Name
from .Phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        if Phone.validate_phone_number(number):
            phone = Phone(number)
            self.phones.append(phone)
            print(f"Added phone {number} for {self.name}")
        else:
            raise ValueError("Invalid phone number format. It should have 10 digits.")

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                self.phones.remove(phone)
                print(f"Removed phone {number} for {self.name}")
                return
        print(f"Phone {number} not found for {self.name}")

    def edit_phone(self, old_number, new_number):
        phone_to_edit = self.find_phone(old_number)
        if phone_to_edit:
            phone_to_edit.number = new_number
            print(f"Edited phone from {old_number} to {new_number} for {self.name}")
        else:
            print(f"Phone {old_number} not found for {self.name}")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                return phone
        return None
    
    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.phones))}"
