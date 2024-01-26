from menus.login import Login
from entities.user import User
import program

class Menu:

    def __init__(self):
        pass

    def start_menu_admin(self):
        run = True
        while run:
            answer = input(f"\n{program.user.role} MENY - {program.user.username}\n"
                           "\n1. Lista av products"
                           "\n2. Logga ut"
                           "\nQ. Avsluta programmet"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    print("Lista av products")

                case "2":
                    self.logout()
                    run = False

                case "q":
                    self.close_program()
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def start_menu_user(self):
        run = True
        while run:
            answer = input(f"\n{program.user.role} MENY - {program.user.username}\n"
                           "\n1. Lista av products"
                           "\n2. Logga ut"
                           "\nQ. Avsluta programmet"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    print("Lista av products")

                case "2":
                    self.logout()
                    run = False

                case "q":
                    self.close_program()
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def start_menu(self):
        run = True
        while run:
            answer = input("\nStart meny\n"
                           "\n1. Lista av products"
                           "\n2. Logga in"
                           "\nQ. Avsluta programmet"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    print("Lista av products")

                case "2":
                    login = Login()
                    run = login.menu()

                case "q":
                    self.close_program()
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def logout(self):
        program.user = User(-1, "x", "x", "x")

    def close_program(self):
        program.user = False