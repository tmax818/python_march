

class User:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.logged_in = False

    def login(self):
        print("user is logged in")
        self.logged_in = True