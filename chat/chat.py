from datetime import datetime
import collections
from dec import input_error

MENU = """
    # - hello
    # - add <username> <phone>
    # - change <username> <phone>
    # - phone <username>
    # - all
    # - "close", "exit"
"""
FILENAME = "contacts.txt"
Person = collections.namedtuple("Person", ["name", "phone"])


@input_error
def add_contact(person: Person):
    with open(FILENAME, "a") as f:
        current_date = datetime.now().date().strftime("%d-%m-%Y")
        record = f"{current_date: >15}{person.name: ^40}{person.phone: ^10}\n"
        f.write(record)
        print("Contact added.")


@input_error
def change_contact(person: Person):
    file_updated = False
    with open("contacts.txt", "r") as file:
        lines = file.readlines()
    current_date = datetime.now().date().strftime("%d-%m-%Y")
    with open("./contacts.txt", "w") as file:
        for line in lines:
            if person.name in line:
                parts = line.split()
                parts[-1] = person.phone
                line = f"{current_date: >15}{person.name: ^40}{person.phone: ^10}\n"
                file_updated = True
            file.write(line)

    if not file_updated:
        raise KeyError


@input_error
def show_phone(name):
    with open("contacts.txt", "r") as file:
        for line in file:
            if name.lower() in line.lower():
                phone_number = line.split()[-1]
                print(phone_number)
                return

        print("Contact name not found.")


def show_all():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.read()
            if contacts:
                print(contacts)
            else:
                print("No contacts found in the file.")

    except IOError:
        print("Error while accessing the file.")

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def main():
    print(MENU)
    while True:

            command = input("Enter command: ").strip()
            command_name, args = parse_input(command)

            if command_name.lower() == "hello":
                print("How can I help you?")
            elif command_name.startswith("add"):
                add_contact(Person(args[0], args[1]))
            elif command_name.startswith("change"):
                change_contact(Person(args[0], args[1]))
            elif command_name.startswith("phone"):
                show_phone(args[0])
            elif command_name == "all":
                show_all()
            elif command_name in ["close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")



if __name__ == "__main__":
    main()