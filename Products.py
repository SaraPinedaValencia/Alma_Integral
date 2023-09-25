class Products:
    def __init__(self, code: str, name: str, price: int, brand: str):
        self.code: str = code
        self.name: str = name
        self.price: int = price
        self.brand: str = brand
        self.quantity: int = 0


class Inventory:
    products: list[Products] = []


class InventoryManagement:

    @staticmethod
    def verify_code_in_inventory(code: str) -> bool:
        for product in Inventory.products:
            if product.code == code:
                return False
        return True

    @staticmethod
    def verify_name_in_inventory(name: str) -> bool:
        for product in Inventory.products:
            if product.name == name:
                return False
        return True

    @staticmethod
    def create_product(code: str, name: str, price: int, brand: str) -> bool:
        product = Products(code, name, price, brand)
        if InventoryManagement.verify_code_in_inventory(product.code) and InventoryManagement.verify_name_in_inventory(
                product.name):
            Inventory.products.append(product)
            return True
        else:
            return False

    @staticmethod
    def quantity_product(code, quantity: int) -> bool:
        if not InventoryManagement.verify_code_in_inventory(code):
            for products in Inventory.products:
                if products.code == code:
                    products.quantity += quantity
                    return True
            else:
                return False

    @staticmethod
    def modify_product_name(product: Products, name: str):
        product.name = name

    @staticmethod
    def modify_product_brand(product: Products, brand: str):
        product.brand = brand

    @staticmethod
    def modify_product_price(product: Products, price: int):
        product.price = price

    @staticmethod
    def delete_product_from_inventory(code: int):
        if code in Inventory.products:
            counter = 0
            for products in Inventory.products:
                if products.code == code:
                    Inventory.products.pop(counter)
                counter += 1
