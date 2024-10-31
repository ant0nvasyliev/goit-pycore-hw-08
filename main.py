from address_book import AddressBook
from parser import parse_input
from handlers import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from serialization import load_data, save_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
            save_data(book)

        elif command == "change":
            print(change_contact(args, book))
            save_data(book)

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args,book))
            save_data(book)

        elif command == "show-birthday":
            print(show_birthday(args,book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")

if __name__ == '__main__':main()