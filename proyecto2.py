
from msilib.schema import Class


global listaP
global listaCarrito
listaP = list()
listaCarrito = list()
class Producto :
    id = ""
    nombre = ""
    precio = 0
    cantidad_p = 0

class Carrito :
    id_compra = ""
    product_compra = ""
    precio_prod = 0
    cantidad_prod = 0
    total_pago = 0

def registrar_producto () :
    print("Registro de Productos")
    prod = Producto()

    prod.id = input("Ingrese Identificador del Producto: ")
    prod.nombre = input("Ingrese Nombre del Producto: ")
    prod.precio = int(input("Ingrese el Precio del Producto: "))
    prod.cantidad_p = int(input("Ingrese la Cantidad de Productos a Agregar: "))
    listaP.append(prod)

def listar_producto () :
    print("Listado de Productos")
    for prod in listaP :
        print(prod.id, "--", prod.nombre, "--", prod.precio, "--", prod.cantidad_p)


def buscar_producto () :
    print("Busqueda de Productos")
    id = input("Ingrese el id del Producto a buscar: ")

    for prod in listaP :
        if prod.id == id :
            print(prod.id, "--", prod.nombre, "--", prod.precio, "--", prod.cantidad_p)


def agregar_carrito () :
    print("Agregar Producto al Carrito")
    carrito_com = Carrito()
    id = input("Ingrese Identificador del Producto: ")
    for prod in listaP :
        if prod.id == id :
            carrito_com.id_compra = prod.id
            carrito_com.product_compra = prod.nombre
            carrito_com.precio_prod = prod.precio
            carrito_com.cantidad_prod = int(input("Ingrese la Cantidad de Productos a Agregar: "))
            carrito_com.total_pago = (carrito_com.precio_prod * carrito_com.cantidad_prod)
           # resp = input("Desea Agregar otro producto al carrito")
            print("LA TIENDA")
            print(carrito_com.product_compra, "----------", carrito_com.precio_prod)
            print("TOTAL: ", carrito_com.total_pago)

    



def remover_carrito() :
    print("Remover Producto del Carrito de Compras")
    id_remover = input("Ingrese el Identificador del producto que desea Remover")
    for carrito_com in listaCarrito :
        if carrito_com.id_compra == id_remover :
            


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


