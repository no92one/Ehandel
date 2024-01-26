from entities.product import Product


class Cart:

    def add(self, product, amount):
        print(f"Add product - {product.id}")
        # använd "any()"-metoden för att få reda på om produkten redan finns i
        # varukorgen t.ex any(product.id == item.id for item in self.list)
        index = next((index for index, item in enumerate(self.list) if product.id == item.id), None)
        print(f"värdet på det index vi hitta = {index}")
        if index is not None:
            self.list[index].stock += amount
            print(f"{self.list[index].name} har nu en stock på {self.list[index].stock}")
        else:
            new_item = Product(product.id, product.name, product.price, amount)
            print(f"New Item added to cart - {new_item}")
            self.list.append(new_item)

    def print_list(self):
        for item in self.list:
            print(item)

    def __init__(self):
        self.list = []

