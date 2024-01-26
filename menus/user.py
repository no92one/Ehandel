import program


class User:

    def shop_products(self):
        run =True
        while run:
            program.products.print_list()
            answer = input("\nSkriv index på den produkt du vill lägga till i varukorgen -> ").strip()
            if answer.lower() == "b":
                run = False
            elif answer.isdigit():
                answer = int(answer) - 1
                if 0 >= answer < len(program.products.list):
                    print(f"{program.products.list[answer]}")





    def start_menu(self):
        run = True
        while run:
            answer = input(f"\n{program.user.role} MENY - {program.user.username}\n"
                           "\n1. Handla products"
                           "\n2. Varukorg"
                           "\n3. Min beställningar"
                           "\n4. Logga ut"
                           "\nQ. Avsluta programmet"
                           "\n\n-> ").strip()

            match answer.lower():
                case "1":
                    self.shop_products()

                case "2":
                    print("Varukorg")

                case "3":
                    print("Min beställningar")

                case "4":
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