from menus.start import Start as StartMenu
from menus.user import User as UserMenu
from menus.admin import Admin as AdminMenu
from entities.user import User
from product_list import ProductList

user = User(-1, "x", "x", "USER")
products = ProductList()

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
                StartMenu()
            elif user.role == "ADMIN":
                AdminMenu()
            elif user.role == "USER":
                UserMenu()