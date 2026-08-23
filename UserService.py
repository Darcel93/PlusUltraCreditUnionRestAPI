from User import User
from UserRepo import UserRepo
import Repository
import random
user_repo = UserRepo()

class UserService:
    def login(self,username,password):
        return Repository.login(username, password)

    def register(self,profile_pic, firstname, lastname, email, username, password):
        account_number = random.randint(1_000_000_00, 9_999_999_99)
        Repository.registration(profile_pic, firstname, lastname, email, username, password,account_number)



    def GetUsers(self):
        return user_repo.get_user()