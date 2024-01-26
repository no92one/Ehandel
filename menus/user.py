import program
from cart import Cart


class User:

    def shop_products(self):
        run =True
        while run:
            program.products.print_list()
            answer = input("\nSkriv index på den produkt du vill lägga till i varukorgen -> ").strip()
            if answer.lower() == "b":
                run = False
            elif answer.isdigit():
                index = int(answer) - 1
                if 0 <= index < len(program.products.list):
                    amount = input(f"Hur många {program.products.list[index].name} vill du ha?"
                                   f"\nIn stock - {program.products.list[index].stock}"
                                   f"\n-> ").strip()
                    if amount.isdigit():
                        amount = int(amount)
                        if 1 <= amount <= program.products.list[index].stock:
                            program.products.list[index].stock -= amount
                            self.cart.add(program.products.list[index], amount)








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
                    print(self.cart.print_list())

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
        self.cart = Cart()
        self.start_menu()
