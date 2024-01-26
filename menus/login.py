import program
from database import login_query, check_if_user_exist, create_user
from entities.user import User

class Login:
    def __init__(self):
        pass

    def menu(self):
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
                    self.create_user()

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
                        db_user = login_query(username, password)
                        if len(db_user) == 1:
                            print("Du har loggat in!")
                            program.user = User(db_user[0]["id"], db_user[0]["username"], db_user[0]["password"], db_user[0]["role"])
                            run = False
                            run_head_loop = False
                        else:
                            print("Fel användarnamn eller lösenord!")

                case "b":
                    run = False

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller B!")

        return run_head_loop

    def create_user(self):
        username = ""
        password = ""
        run_head_loop = True

        run = True
        while run:
            answer = input("\nSkapa Konto\n"
                           f"\n1. Användarnamn -> {username}"
                           f"\n2. Lösenord -> {password}"
                           f"\n\n3. Skapa konto"
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
                        if len(check_if_user_exist(username)) > 0:
                            print("Detta användarnamnet är upptaget!")
                        else:
                            print(create_user(username, password))
                            print(f"Ett konto för - {username} - har skapats!")
                            run = False

                case "b":
                    run = False

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller B!")

        return run_head_loop