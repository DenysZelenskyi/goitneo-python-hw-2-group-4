def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Invalid input. Please provide valid data.")
            return None
        except KeyError:
            print("User not exist. Please provide valid data.")
            return None
        except IndexError:
            print("Please check your input.")
            return None

    return inner