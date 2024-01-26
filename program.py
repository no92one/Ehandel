from menu import Menu
from user import User

user = User(-1, "x", "x", "x")

class Program:
    def __init__(self):
        menu = Menu()

        while user != False:
            print(user.role)
            if user.role == "x":
                menu.start_menu()
            elif user.role == "ADMIN":
                menu.start_menu_admin()
            elif user.role == "USER":
                menu.start_menu_user()