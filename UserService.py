from User import User
from UserRepo import UserRepo
import Repository
user_repo = UserRepo()

class UserService:
    def login(self,username,password):
        return Repository.login(username, password)

    def register(self, firstname, lastname, email, username, password):
        new_user = User(firstname,lastname, email,  username, password)
        user_repo.NewUser(new_user)

    def GetUsers(self):
        return user_repo.get_user()