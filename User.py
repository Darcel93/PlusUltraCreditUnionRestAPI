class User:
    def __init__(self, firstName, lastName, email, username, password, accountNumber = "", amount = 1000, profilepic = ""):
        self.profilepic = profilepic
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.email = email
        self.accountNumber = accountNumber
        self.amount = amount

    def printUser(self):
        print(self.firstName)
        print(self.lastName)
        print(self.username)
        print(self.email)
        print(self.amount)
