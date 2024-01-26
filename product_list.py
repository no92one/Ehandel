from database import get_all_products
from entities.product import Product

class ProductList:

    def print_list(self):
        print("Index | Name | Price | Quantity ")
        for index, product in enumerate(self.list):
            print(f"{index + 1} | {product.name} | {product.price} | {product.stock}")
    def populate_list(self):
        products_list = []

        products_data = get_all_products()
        for item in products_data:
            products_list.append(Product(item["id"], item["name"], item["price"], item["stock"]))

        return products_list

    def __init__(self):
        self.list = self.populate_list()
