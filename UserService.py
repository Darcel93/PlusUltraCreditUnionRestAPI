from User import User
from UserRepo import UserRepo
import Repository
import random
import requests
user_repo = UserRepo()

class UserService:
    def login(self,username,password):
        return Repository.login(username, password)

    def register(self,profile_pic, firstname, lastname, email, username, password):
        account_number = random.randint(1_000_000_00, 9_999_999_99)
        url = self.uploadavatar(profile_pic)
        print("This is the " + url)
        Repository.registration(url, firstname, lastname, email, username, password,account_number)

    def uploadavatar(self,uploaded_file):
        url = "http://127.0.0.1:5000/upload"
        # payload = {
        #     "file": profile_pic
        # }
        files = {
            'file': (
                uploaded_file.filename,
                uploaded_file.stream,
                uploaded_file.content_type,
            )
        }
        # The `json=` parameter handles encoding and headers automatically
        response = requests.post(url, files=files)

        if response.status_code == 200 or response.status_code == 201:
            print("Success!")
            print(response.json())
        else:
            print(f"Failed with status code: {response.status_code}")
        return response.json()['url']

    def GetUsers(self):
        return user_repo.get_user()