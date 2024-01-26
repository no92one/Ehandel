import program


class Admin:
    def start_menu(self):
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
                    program.logout()
                    run = False

                case "q":
                    program.close_program()
                    run = False
                    print("Programet avslutas!")

                case _:
                    print(f"Du skrev in '{answer}'\nDu måste välja 1, 2, eller Q!")

    def __init__(self):
        self.start_menu()