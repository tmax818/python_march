from user_pkg.user import User

class AdminUser(User):

    all_admin_users = []
    
    def __init__(self, name, email) -> None:
        super().__init__(name, email)
        self.is_admin = True
        AdminUser.all_admin_users.append(self)

    def __str__(self):
        return f"{self.name}, {self.email}"

    @classmethod
    def show_admin_users(cls):
        for auser in cls.all_admin_users:
            print(auser)