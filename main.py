from enum import Enum, auto
from parser import parse_input
from handlers import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from serialization import load_data, save_data
from interface import ConsoleInterface



def main():
    book = load_data()
    ui = ConsoleInterface()
    ui.display_welcome()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            ui.display_goodbye()
            break

        elif command == "hello":
            ui.display_message("How can I help you?")

        elif command == "add":
            result = add_contact(args, book)
            ui.display_message(result)
            save_data(book)

        elif command == "change":
            result = change_contact(args, book)
            ui.display_message(result)
            save_data(book)

        elif command == "phone":
            result = show_phone(args, book)
            ui.display_contact(result)

        elif command == "all":
            result = show_all(book)
            ui.display_contacts([result])

        elif command == "add-birthday":
            result = add_birthday(args, book)
            ui.display_message(result)
            save_data(book)

        elif command == "show-birthday":
            result = show_birthday(args, book)
            ui.display_message(result)

        elif command == "birthdays":
            result = birthdays(book)
            ui.display_message(result)

        elif command == "help":
            ui.display_help()

        else:
            ui.display_error("Invalid command.")

if __name__ == '__main__':main()