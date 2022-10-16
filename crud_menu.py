import sys
from connector import DBhelper

class ChalDal:

    def __init__(self):
        self.db = DBhelper()
        self.menu()


    def menu(self):
        user_input = input("""
        enter 1 to register
        enter 2 to login
        enter anything else to leave
        """)
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name = input("enter your name")
        email = input("enter your email")
        password = input("enter your password")
        response = self.db.register(name, email, password)
        if response:
            print("registration successful")
        else:
            print("registration failed")
    def login(self):
        email = input("enter your email: ")
        password = input("enter your password: ")
        status = self.db.login(email, password)
        if status:
            print(status[0][1])
        else:
            print("login unsuccessful")

obj = ChalDal()