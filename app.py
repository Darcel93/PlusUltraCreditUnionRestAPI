import json

from flask import Flask, request, jsonify
from UserService import UserService
app = Flask(__name__)
user_service = UserService()
#Controller Class: Controls flow - navigates to appropriate functionality

@app.route("/")
def test():
    return "Darcel"

@app.route("/Tester")
def test2():
    return "Ocean Gang"

@app.route("/Login", methods = ["POST"])
def login():
    user = request.get_json()['Username']
    passkey = request.get_json()['Password']
    user_service.login(user, passkey)

@app.route("/register", methods = ["POST"])
def register():
    firstname = request.get_json()['Firstname']
    lastname = request.get_json()['Lastname']
    username = request.get_json()['Username']
    password = request.get_json()['Password']
    email = request.get_json()['Email']
    user_service.register(firstname,lastname,email,username,password)
    return "New User Saved"

@app.route("/allusers", methods = ["GET"])
def getusers():
    user_list = user_service.GetUsers()
    serialized_list = [user.__dict__ for user in user_list]
    return serialized_list



if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 8080, threaded = True, debug = True)


