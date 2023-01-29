import re


def has_uppercase_and_digit(string):
    return bool(re.match(r'.*[A-Z].*\d', string))


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 < len(value) or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if 8 < len(self.value) or not has_uppercase_and_digit(value):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*' * len(self.password)}"


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
