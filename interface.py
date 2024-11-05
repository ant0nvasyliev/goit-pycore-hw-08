from abc import ABC, abstractmethod


class UserInterface(ABC):

    @abstractmethod
    def display_welcome(self):
        pass

    @abstractmethod
    def display_goodbye(self):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_error(self, error_message):
        pass

    @abstractmethod
    def display_contact(self, contact):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_help(self):
        pass


class ConsoleInterface(UserInterface):

    def display_welcome(self):
        print("Welcome to the assistant bot!")

    def display_goodbye(self):
        print("Good bye!")

    def display_message(self, message):
        print(message)

    def display_error(self, error_message):
        print(f"Error: {error_message}")

    def display_contact(self, contact):
        print(contact)

    def display_contacts(self, contacts):
        if not contacts:
            print("There are no contacts yet!")
        else:
            print("\n".join(contacts))

    def display_help(self):
        print("Available commands:\n"
              "hello - greet the bot\n"
              "add <name> <phone> - add new contact\n"
              "change <name> <old_phone> <new_phone> - change contact's phone\n"
              "phone <name> - show contact's phone\n"
              "all - show all contacts\n"
              "add-birthday <name> <date> - add a birthday to contact\n"
              "show-birthday <name> - show contact's birthday\n"
              "birthdays - show upcoming birthdays\n"
              "exit/close - exit the bot")
