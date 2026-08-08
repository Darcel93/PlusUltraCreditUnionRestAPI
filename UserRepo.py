
class UserRepo:
    def __init__(self):
        self.users = []

    def NewUser(self, user):
        self.users.append(user)

    def get_user(self):
        return self.users