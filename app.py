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
    try:
        user = request.get_json()['Username']
        passkey = request.get_json()['Password']
        results = user_service.login(user, passkey)
        print(results.amount)
        return jsonify(results.__dict__)
    except:
        return jsonify({
            "status_code" : 401,
            "error_message" : "Username or Password is incorrect"

        }), 401


@app.route("/register", methods = ["POST"])
def register():
    profile_pic = request.get_json()['Profile_pic']
    firstname = request.get_json()['Firstname']
    lastname = request.get_json()['Lastname']
    username = request.get_json()['Username']
    password = request.get_json()['Password']
    email = request.get_json()['Email']
    user_service.register(profile_pic, firstname,lastname,email,username,password)
    return "New User Saved"

@app.route("/allusers", methods = ["GET"])
def getusers():
    user_list = user_service.GetUsers()
    serialized_list = [user.__dict__ for user in user_list]
    return serialized_list



if __name__ == "__main__":
    app.run(host ="0.0.0.0", port = 8080, threaded = True, debug = True)


