from rich.console import Console
from rich.table import Table
import pyfiglet
from pyfiglet import Figlet

import Products
from Products import Inventory


class View:

    @staticmethod
    def login():
        table = Table(title="Login")

        table.add_column("Escogencias", style="red", no_wrap=True)
        table.add_column("Opciones", style="magenta")

        table.add_row("1", "Iniciar sesion")
        table.add_row("2", "Salir de la aplicacion")

        console = Console()
        console.print(table)

    @staticmethod
    def main_admin_menu():
        table = Table(title="Alma integral admnistrador", title_style="italic")

        table.add_column("Escogencias", style="red", no_wrap=True)
        table.add_column("Opciones", style="purple")

        table.add_row("1", "Registrar usuario administrador")
        table.add_row("2", "Modificar usuario administrador")
        table.add_row("3", "Crear producto")
        table.add_row("4", "Agregar cantidad de producto")
        table.add_row("5", "Modificar producto")
        table.add_row("6", "Eliminar producto")
        table.add_row("7", "Registrar venta")
        table.add_row("8", "Mostrar todos los productos")
        table.add_row("9", "Mostrar todos los usuarios")
        table.add_row("10", "Mostrar todos los usuarios")
        table.add_row("11", "Mostrar todos los usuarios")
        table.add_row("12", "Mostrar todos los usuarios")
        table.add_row("13", "Cerrar sesión")

        console = Console()
        console.print(table)

    @staticmethod
    def main_employee_menu():
        table = Table(title="Alma integral empleado", title_style="italic")

        table.add_column("Escogencias", style="red", no_wrap=True)
        table.add_column("Opciones", style="purple")

        table.add_row("1", "Verificar lista de productos")
        table.add_row("2", "Registrar venta")
        table.add_row("3", "Modificar datos de sesion")
        table.add_row("4", "Cerrar sesión")

    @staticmethod
    def product_item_list():
        table = Table(title="Alma integral productos", title_style="italic")

        table.add_column("Codigo", style="red", no_wrap=True)
        table.add_column("Nombre", style="purple")
        table.add_column("Precio", style="yellow")
        table.add_column("Marca", style="purple")
        table.add_column("Cantidad", style="blue")

        for productos in Inventory.products:
            codigo = productos.code
            nombre = productos.name
            precio = str(productos.price)
            marca = productos.brand
            cantidad = str(productos.quantity)

            table.add_row(codigo, nombre, precio, marca, cantidad)
            table.add_row("", "", "", "", "")

        console = Console()
        console.print(table)

    @staticmethod
    def example_create_product():
        table = Table(title="Ejemplo crear producto", title_style="italic")

        table.add_column("Nombre", style="red", no_wrap=True)
        table.add_column("Codigo", style="yellow")
        table.add_column("Precio", style="blue")
        table.add_column("Marca", style="purple")
        table.add_column("cantidad", style="purple")

        table.add_row("Un nombre", "Un codigo", "un precio", "una marca")
        table.add_row("", "", "", "")
        table.add_row("Manzanas", "001", "$0.99", "Evergreen", "3")
        table.add_row("Leche", "002", "$2.49", "Colanta", "6")
        table.add_row("Pan", "003", "$1.29", "Bimbo", "99")

        console = Console()
        console.print(table)

    @staticmethod
    def example_modify_product(title="Ejemplo modificar producto"):
        table = Table(title=title, title_style="italic")

        table.add_column("Nombre", style="red", no_wrap=True)
        table.add_column("Codigo", style="yellow")
        table.add_column("Precio", style="blue")
        table.add_column("Marca", style="purple")


        table.add_row("Modificar un nombre", "Modificar un precio", "Modificar una marca")
        table.add_row("", "", "")
        table.add_row("Manzanas", "$0.99", "Evergreen")
        table.add_row("Leche", "$2.49", "Colanta")
        table.add_row("Pan", "$1.29", "Bimbo")

        console = Console()
        console.print(table)

    @staticmethod
    def example_delete_product():
        table = Table(title="Depues de eliminar varios productos", title_style="italic")

        table.add_column("Nombre", style="red", no_wrap=True)
        table.add_column("Codigo", style="yellow")
        table.add_column("Precio", style="blue")
        table.add_column("Marca", style="purple")

        table.add_row("", "", "", "")
        table.add_row("", "", "", "")
        table.add_row("", "", "", "")
        table.add_row("", "", "", "")

        antes = View.example_modify_product("Antes de eliminar")
        console = Console()
        console.print(table)

    @staticmethod
    def example_register_sell():
        table = Table(title="Ejemplo Registrar venta", title_style="italic")

        table.add_column("Producto", style="red", no_wrap=True)
        table.add_column("Codigo", style="black", no_wrap=True)
        table.add_column("Cantidad", style="yellow")
        table.add_column("Precio parcial", style="blue")
        table.add_column("Precio final", style="green")

        table.add_row("Manzanas", "001", "5", "$0.99", "$4.95")
        table.add_row("Leche", "002", "2", "$2.49", "$4.98")
        table.add_row("Pan", "003", "1", "$1.29", "$1.29")
        table.add_row("Arroz", "004", "3", "$0.75", "$2.25")

        console = Console()
        console.print(table)

    @staticmethod
    def example_register_administrator():
        table = Table(title="ejemplo registrar administrador", title_style="italic")

        table.add_column("Nombre", style="red", no_wrap=True)
        table.add_column("Correo", style="blue", no_wrap=True)
        table.add_column("Contrasena", style="yellow")

        table.add_row("Juan Pérez", "juan.perez@example.com", "contraseña1")
        table.add_row("Ana Gómez", "ana.gomez@example.com", "contraseña2")
        table.add_row("Carlos Rodríguez", "carlos.rodriguez@example.com", "contraseña3")
        table.add_row("María García", "maria.garcia@example.com", "contraseña4")

        console = Console()
        console.print(table)

    @staticmethod
    def welcome():
        custom_fig = Figlet()
        custom_fig = Figlet(font='thin')
        bienvenida = (custom_fig.renderText('alma integral'))
        table = Table(title="Bienvenido a alma integral!!!", title_style="italic")

        table.add_column("               tu super mercado de confianza              ", style="yellow", no_wrap=True)
        table.add_row(bienvenida)
        console = Console()
        console.print(table)
