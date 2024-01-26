from menus.start import Start
from menus.user import User
from menus.admin import Admin
from entities.user import User

user = User(-1, "x", "x", "x")

def logout():
    global user
    user = User(-1, "x", "x", "x")

def close_program():
    global user
    user = False

class Program:
    def __init__(self):
        while user != False:
            print(user.role)
            if user.role == "x":
                Start()
            elif user.role == "ADMIN":
                Admin()
            elif user.role == "USER":
                User()