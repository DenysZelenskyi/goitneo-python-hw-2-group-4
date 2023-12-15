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

# Перевірка, чи правильно знаходимо запис "John" в книзі
john_record_from_book = book.find("John")
print(john_record_from_book)  # Повинно вивести екземпляр Record або None, якщо не знайдено



jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

#  всі записи
for name, record in book.data.items():
    print(record)

# Перевірка, чи правильно знаходимо запис "John" в книзі
john_record_from_book = book.find("John")
print(john_record_from_book)  # Повинно вивести екземпляр Record або None, якщо не знайдено

# Перевірка, чи правильно знаходимо телефон в записі "John"
found_phone = john_record_from_book.find_phone("5555555555")
print(f"{john_record_from_book.name}: {found_phone}")  # Повинно вивести номер телефону або None, якщо не знайдено
