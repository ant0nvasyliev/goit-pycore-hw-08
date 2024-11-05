from collections import UserDict
from datetime import date
from helpers import string_to_date, date_to_string, adjust_for_weekend, validate_number
from abc import ABC, abstractmethod


class AbstractField(ABC):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    @abstractmethod
    def validate(self, value):
        pass

class Field(AbstractField):
    def __init__(self, value):
        self.value = value
        super().__init__(value)

    def validate(self, value):
        pass


class Name(Field):
    def validate(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be empty")


class Phone(Field):
    def validate(self, value):
        self.value = validate_number(value)


class Birthday(Field):
    def validate(self, value):
        try:
            string_to_date(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class AbstractRecord(ABC):
    def __init__(self, contact_name):
        self.name = Name(contact_name)

    @abstractmethod
    def add_phone(self, phone_number):
        pass

    @abstractmethod
    def add_birthday(self, birthday_date):
        pass

    @abstractmethod
    def remove_phone(self, phone_number):
        pass

    @abstractmethod
    def edit_phone(self, old_phone, new_phone):
        pass

    @abstractmethod
    def find_phone(self, phone_number):
        pass


class Record(AbstractRecord):
    def __init__(self, contact_name) -> None:
        super().__init__(contact_name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        print(f"Phone number {phone_number} not found.")

    def edit_phone(self, old_phone, new_phone):
        validated_new_phone = validate_number(new_phone)
        if not self.find_phone(old_phone):
            raise ValueError(f"Phone number {old_phone} not found")
        self.remove_phone(old_phone)
        self.add_phone(validated_new_phone)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                return phone
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {[obj.value for obj in self.phones]}"





class AbstractAddressBook(ABC):
    @abstractmethod
    def add_record(self, record_item):
        pass

    @abstractmethod
    def find(self, contact_name):
        pass

    @abstractmethod
    def delete(self, contact_name):
        pass

    @abstractmethod
    def get_upcoming_birthdays(self, days=7):
        pass


class AddressBook(AbstractAddressBook, UserDict):

    def add_record(self, record_item):
        self.data[record_item.name.value] = record_item

    def find(self, contact_name):
        return self.data.get(contact_name)

    def delete(self, contact_name):
        if contact_name in self.data:
            del self.data[contact_name]

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                birthday_date = string_to_date(record.birthday.value)
                birthday_this_year = birthday_date.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_date.replace(year=today.year + 1)
                if 0 <= (birthday_this_year - today).days <= days:
                    adjusted_birthday = adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": date_to_string(adjusted_birthday)
                    })
        return upcoming_birthdays

    def __str__(self) -> str:
        if not self.data:
            return "Phone book is empty."
        return "\n".join(
            f"Contact name: {record.name.value} - contact number(s) {', '.join(phone.value for phone in record.phones)}"
            for record in self.data.values())
