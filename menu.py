from database import login_query
from user import User


class Menu:

    def __init__(self):
        self.user = ""

    def start_menu_admin(self):
        pass

    def start_menu_user(self):
        pass
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
                    run = self.login_menu()

                case "q":
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def login_menu(self):
        run_head_loop = True
        run = True
        while run:
            answer = input("\nLogin meny\n"
                           "\n1. Login"
                           "\n2. Skapa konto"
                           "\nB. Gå tillbaka"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    run = self.login()
                    run_head_loop = run

                case "2":
                    print("Skapa konto")

                case "b":
                    run = False

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller B!")
        return run_head_loop

    def login(self):
        username = ""
        password = ""
        run_head_loop = True

        run = True
        while run:
            answer = input("\nLogin\n"
                  f"\n1. Användarnamn -> {username}"
                  f"\n2. Lösenord -> {password}"
                  f"\n\n3. Logga in"
                  f"\nB. Gå tillbaka"
                  f"\n\n-> ").strip()

            match answer.lower():
                case "1":
                    username = input("Användarnamn -> ").strip()

                case "2":
                    password = input("Lösenord -> ").strip()

                case "3":

                    if len(username) == 0:
                        print("Du måste ange ett användarman!")
                    elif len(password) == 0:
                        print("Du måste ange ett lösenord!")
                    else:
                        user = login_query(username, password)
                        if len(user) == 1:
                            print("Du har loggat in!")
                            print(user[0])
                            self.user = User(user[0]["id"], user[0]["username"], user[0]["password"], user[0]["role"])
                            run = False
                            run_head_loop = False
                        else:
                            print("Fel användarnamn eller lösenord!")

                case "b":
                    run = False

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller B!")

        return run_head_loop