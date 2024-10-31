def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) == "Name cannot be empty":
                return "Please provide a name."
            elif str(e) == "Invalid phone number format":
                return "Please provide a valid phone number."
            elif str(e) == "Invalid date format. Use DD.MM.YYYY":
                return "Please enter the date in DD.MM.YYYY format."
            else:
                return "Value error occurred."
        except TypeError:
            return "Wrong type of data"
        except KeyError:
            return "Wrong key value"
        except IndexError:
            return "Enter the argument for the command"
        except Exception as Error:
            return f"Error: {Error}"
    return inner