from rich.console import Console
from Console import View
from rich.table import Table
from Users import UserManagement, User, Admin, Employee
from Products import InventoryManagement, Products


class Controller:
    print("usted va a crear otro usuario administrador, la estructura de este se ve asi: ")
    View.example_register_administrator()
    print("")

    print("ahora que sabe la esctructura por favor ingrese: ")

    print("")

    while True:
        name = str(input("nombre: "))
        email = str(input("email: "))
        password = str(input("contraseña: "))

        if Admin.create_admin_user(name, email, password):
            break
        else:
            print("no se pudo hacer el ingreso correcto del usuario , intentelo de nuevo")

    def login(self):

        while True:

            View.login()
            choice = int(input("[red]por favor escoja una de las siguientes opciones para continuar: "))

            if choice == 1:

                while True:
                    user = str(input("por favor ingrese su usuario: "))
                    password = str(input("por favor ingrese su clave: "))

                    if UserManagement.verify_admin_credential(user, password):
                        self.main_admin_menu()

                    if UserManagement.verify_employee_credential(user, password):
                        self.main_employee_menu()

                    else:
                        print("el usuario ingresado no existe")

            if choice == 2:
                break


    def main_admin_menu(self):

        while True:

            View.main_admin_menu()

            choice = int(input("[red]por favor escoja una de las siguientes opciones para continuar"))

            # Registrar usuario administrador
            if choice == 1:

                print("usted va a crear otro usuario administrador, la estructura de este se ve asi: ")
                View.example_register_administrator()
                print("")

                print("ahora que sabe la esctructura por favor ingrese: ")

                print("")

                while True:
                    name = str(input("nombre: "))
                    email = str(input("email: "))
                    password = str(input("contraseña: "))

                    if Admin.create_admin_user(name, email, password):
                        break
                    else:
                        print("no se pudo hacer el ingreso correcto del usuario , intentelo de nuevo")

            # Modificar usuario administrador (solo se pueden modificar los datos de la sesion actual)
            if choice == 2:
                pass

            # Crear producto
            if choice == 3:
                print("usted ingreso la opcion de crear producto, la estructrua se ve algo asi: ")
                View.example_create_product()

                print("ahora que usted sabe la estructura de la creacion del producto, ingrese: ")

                while True:
                    codigo = str(input("ingrese el codigo del producto: "))
                    nombre = str(input("ingrese el nombre del producto: "))
                    precio = int(input("ingrese el precio del producto: "))
                    marca = str(input("ingrese la marca del producto: "))

                    if InventoryManagement.create_product(codigo, nombre, precio, marca):
                        break
                    else:
                        print("No se pudo ingresar el producto , por favor intentelo de nuevo: ")

            # Agregar cantidad de producto
            if choice == 4:
                print("usted ingreso la opcion de agregar por cantidad un producto, la estructrua se ve algo asi: ")
                View.example_create_product()

                print("ahora que usted sabe la estructura de la agregacion del producto, ingrese: ")

                View.product_item_list()

                codigo = int(input("ingrese el codigo del producto que quiere escoger , aqui estan la lista de productos: "))


                cantidad = int(input("ingrese la cantidad de productos que quiere agregar: "))

                InventoryManagement.quantity_product(codigo, cantidad)

                print(f"los productos actualizados son: {View.product_item_list()}")

            # Modificar producto
            if choice == 5:
                pass

            # Eliminar producto
            if choice == 6:
                pass

            # Registrar venta
            if choice == 7:
                pass

            # Mostrar todos los productos
            if choice == 8:
                pass

            # Mostrar todos los usuarios administradores
            if choice == 9:
                pass

            # Mostrar todos los usuarios empleados
            if choice == 10:
                pass

            # Registrar Usuario empleado
            if choice == 11:
                pass

            # Modificar usuario empleado ( se puede modificar cualquier empleado)
            if choice == 12:
                pass

            # Cerrar sesión
            if choice == 13:
                break

            print("Por favor realize una elección válida")

    def main_employee_menu(self):

        while True:
            View.main_employee_menu()

            choice = int(input("[red]por favor escoja una de las siguientes opciones para continuar"))

            # Verificar lista de productos
            if choice == 1:
                pass

            # Registrar venta
            if choice == 2:
                pass

            # Modificar datos de sesio
            if choice == 3:
                pass

            # Cerrar sesión
            if choice == 4:
                pass

            print("por favor realize una elección valida")


objeto = Controller()
objeto.login()
