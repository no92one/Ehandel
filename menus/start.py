from menus.login import Login
import program

class Start:
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
                    program.close_program()
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def __init__(self):
        self.start_menu()