
class Products:
    def __init__(self, code: str, name: str, price: int, brand: str):
        self.code: str = code
        self.name: str = name
        self.price: int = price
        self.brand: str = brand
        self.quantity: int = 0


class Inventory:
    products: list[Products] = []

    @staticmethod
    def printear():
        for producto in Inventory.products:
            print(producto.code, producto.name, producto.price, producto.brand, producto.quantity)


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
    def quantity_product(code: str, quantity: int) -> bool:
        if not InventoryManagement.verify_code_in_inventory(code):
            for products in Inventory.products:
                if products.code == code:
                    products.quantity += quantity
                    return True
            else:
                return False

    @staticmethod
    def modify_product_name(code: str, name: str):
        for products in Inventory.products:
            if products.code == code:
                products.name = name
                return True
        return False

    @staticmethod
    def modify_product_brand(code: str, brand: str):
        for products in Inventory.products:
            if products.code == code:
                products.brand = brand
                return True

        return False

    @staticmethod
    def modify_product_price(code: str, price: int):
        for products in Inventory.products:
            if products.code == code:
                products.price = price
                return True

        return False

    @staticmethod
    def delete_product_from_inventory(code: str):

        counter = 0
        for products in Inventory.products:

            if products.code == code:
                Inventory.products.pop(counter)

            counter += 1


"""prueba = Products("001", "semillas", 7000, "viva")

InventoryManagement.create_product("002", "semillas2", 7000, "viva")
InventoryManagement.create_product("003", "semillas3", 7000, "viva")
InventoryManagement.create_product("004", "semillas4", 7000, "viva")
InventoryManagement.create_product("005", "semillas5", 7000, "viva")
Inventory.printear()
print("")
InventoryManagement.quantity_product("002", 99)
Inventory.printear()
print("")
InventoryManagement.delete_product_from_inventory("002")
Inventory.printear()
print("")
print(InventoryManagement.verify_name_in_inventory("semillas3"))
print(InventoryManagement.verify_code_in_inventory("003"))
InventoryManagement.modify_product_name("005", "pepsi")
Inventory.printear()
InventoryManagement.create_product("006", "semillas6", 7000, "viva")
InventoryManagement.create_product("007", "semillas7", 7000, "viva")
InventoryManagement.create_product("008", "semillas58", 7000, "viva")
InventoryManagement.create_product("009", "semillas8", 7000, "viva")
InventoryManagement.quantity_product("009", 999)"""
