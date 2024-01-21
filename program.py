from menu import Menu

class Program:
    def __init__(self):
        self.user = ""

        def start_program(self):
            if self.user == "":
                Menu.start_menu()
            elif self.user["role"] == "ADMIN":
                Menu.start_menu_admin()
            elif self.user["role"] == "USER":
                Menu.start_menu_user()