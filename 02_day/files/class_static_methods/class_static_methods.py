## class_static_methods.py

## TODO `@classmethod`

class User:

    all_users = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        User.all_users.append(self)

    @classmethod
    def get_users(cls):
        print(cls.all_users)

    @classmethod
    def print_first_names(cls):
        for user in cls.all_users:
            print(user.first_name)

## TODO `@staticmethod`
    @staticmethod
    def validate_user(user):
        if len(user.first_name) < 3:
            print("Name is too few chars")
        print(user)

john = User('john', 'doe', 'jd@email.com')
mary = User('mary', 'doe', 'mary@email.com')
ed = User('ed', 'im', 'edog@codingdojo.com')

User.get_users()
User.print_first_names()