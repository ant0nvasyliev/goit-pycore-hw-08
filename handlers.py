from decorators import input_error
from address_book import Record
from helpers import string_to_date, date_to_string


@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return f"Contact {name} updated!"



@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    return str(record) if record else f'Contact {name} not found.'

@input_error
def show_all(book):
    if not book.data:
        return "There are no contacts yet!"
    contacts = [str(record) for record in book.data.values()]
    return "\n".join(contacts)


@input_error
def add_birthday(args, book):
    name, birthday_date, *_ = args
    record = book.find(name)
    if record is None:
        return f"Contact '{name}' not found in the address book."
    record.add_birthday(birthday_date)
    return 'Birthday added'


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)

    if record:
        if record.birthday:
            birthday_date = string_to_date(record.birthday.value)
            return f"{name}'s birthday is on {date_to_string(birthday_date)}"
        else:
            return f"{name} does not have a birthday recorded."
    else:
        return f'Contact {name} not found.'


@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays(days=7)

    if not upcoming_birthdays:
        return "No upcoming birthdays in the next 7 days."

    return "\n".join(f"{entry['name']}'s birthday is on {entry['birthday']}." for entry in upcoming_birthdays)