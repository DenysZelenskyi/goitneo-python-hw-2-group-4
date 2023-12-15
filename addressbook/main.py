from classes.AddressBook import AddressBook
from classes.Record import Record

# нова книга
book = AddressBook()

# Створення запису
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# add John до книги
book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

#  всі записи
for name, record in book.data.items():
    print(record)

# редагування телефону
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) 

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  

# Видалення запису
book.delete("Jane")
