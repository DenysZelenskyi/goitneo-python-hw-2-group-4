class Phone:
    def __init__(self, number):
        if not self.validate_phone_number(number):
            raise ValueError("Invalid phone number format. It should have 10 digits.")
        self.number = number

    @staticmethod
    def validate_phone_number(number):
        return len(number) == 10 and number.isdigit()