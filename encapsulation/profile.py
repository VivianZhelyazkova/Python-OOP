import re


class Profile:
    def __init__(self, username: str, password: str):

        if 4 < len(username) < 16:
            self.username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
        regex = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
        match = re.findall(regex, password)
        if match:
            self.password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

