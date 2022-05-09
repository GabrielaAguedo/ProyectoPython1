global lista
lista = list()

class Producto :
    id = ""
    nombre = ""
    precio = 0

def registrar_producto () :
    print("Registro de Productos")


def listar_producto () :
    print("Listado de Productos")


def buscar_producto () :
    print("Busqueda de Productos")


def agregar_carrito () :
    print("Agregar Producto al Carrito")


def remover_carrito() :
    print("Remover Producto del Carrito de Compras")


def salir () :
    print("Gracias por usar la aplicación")
    


def menu ():

    op = 0

    salirmenu = 6

    while op != salirmenu :

        print("Menú")
        print("1.- Registrar Producto ")
        print("2.- Listar Productos")
        print("3.- Buscar Producto")
        print("4.- Agregar Producto al Carrito")
        print("5.- Remover Producto del Carrito")
        print("6.- Salir")

        op = int(input("Digite opción: "))

        if (op == 1) :
            registrar_producto()

        elif (op == 2) :
            listar_producto()

        elif (op == 3) :
            buscar_producto()

        elif (op == 4) :
            agregar_carrito()
        
        elif (op == 5) :
            remover_carrito()

        elif (op == 6) :
            salir()

menu ()


