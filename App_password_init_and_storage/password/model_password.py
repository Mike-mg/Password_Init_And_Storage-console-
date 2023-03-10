"""
Module model password
"""

import random
import string


class ModelPassword:
    """
    Model for generate a password and label
    """

    password_generate = ()

    def __init__(self):

        self.numbers = list(string.digits)
        self.str_upper = list(string.ascii_uppercase)
        self.str_lower = list(string.ascii_lowercase)
        self.str_punctuation = list(string.punctuation)

    def generate_password(
            self, chars_no_permit: list, label_password: str) -> tuple:
        """
        Generate the password
        """

        password = ""
        password_label = ""

        for chars in chars_no_permit:

            if chars in self.numbers:
                self.numbers.remove(chars)

            elif chars in self.str_upper:
                self.str_upper.remove(chars)

            elif chars in self.str_lower:
                self.str_lower.remove(chars)

            elif chars in self.str_punctuation:
                self.str_punctuation.remove(chars)

        nb_int = 0
        while nb_int < 4:

            password += random.choice(self.numbers)
            nb_int += 1

        nb_str = 0
        while nb_str < 2:

            password += random.choice(self.str_upper)
            password += random.choice(self.str_lower)
            password += random.choice(self.str_punctuation)
            nb_str += 1

            password_label = label_password.capitalize()
            password = "".join(random.sample(password, len(password)))

        self.password_generate = (None, password_label, password)

        return self.password_generate
