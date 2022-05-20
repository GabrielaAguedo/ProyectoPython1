
from msilib.schema import Class

from operator import add
from itertools import accumulate


global listaP

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
    print()
    for prod in listaP :
        print(prod.id, "------", prod.nombre, "------", prod.precio, "------", prod.cantidad_p)


def buscar_producto () :
    print("Busqueda de Productos")
    id = input("Ingrese el id del Producto a buscar: ")

    for prod in listaP :
        if prod.id == id :
            print(prod.id, "--", prod.nombre, "--", prod.precio, "--", prod.cantidad_p)


def eliminar_producto () :
    print("Eliminar Producto del Stock")
    id_prodE = input("Ingrese el Identificador del producto que desea eliminar: ")
    for prod in listaP :
        if prod.id == id_prodE :
            while(True):
                resp = input("¿Realmente desea eliminar? [s/n]: ")
                resp = resp.lower()
                if(resp == "s" or resp == "n") :
                    break
            if (resp == "s") :
                listaP.remove(prod)
                print("El producto ha sido eliminado del Stock")


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
            listaCarrito.append(carrito_com)
            print("El producto se agrego correctamente al carrito")

            
       
def remover_carrito() :
    print("Remover Producto del Carrito de Compras")
    id_ing = input("Ingrese el Identificador del producto que desea eliminar: ")
    for carrito_com in listaCarrito :
        if carrito_com.id_compra == id_ing :
            while(True):
                resp = input("¿Realmente desea eliminar? [s/n]: ")
                resp = resp.lower()
                if(resp == "s" or resp == "n") :
                    break
            if (resp == "s") :
                listaCarrito.remove(carrito_com)
                print("El producto ha sido eliminado del carrito de compras")



def cobrar() :
    print("--------------------------------\n          ¡LA TIENDA!\n--------------------------------")
    for carrito_com in listaCarrito :
        
        print("Producto:", carrito_com.product_compra, "----------","CANT:",carrito_com.cantidad_prod, "----------" "Precio U:", carrito_com.precio_prod)
        vari = int(carrito_com.total_pago)
        suma = sum(vari)
        print("TOTAL: ", suma)
        print()
    print("--------------------------\n¡GRACIAS POR SU COMPRA\n--------------------------")



def salir () :
    print("--------------------------------\n¡GRACIAS POR USAR LA APLICACIÓN!\n--------------------------------")
    

def menu ():

    op = 0

    salirmenu = 8

    while op != salirmenu :
       
        print("♦♦♦♦ MENÚ ♦♦♦♦")
        print("1.- Registrar Producto ")
        print("2.- Mostrar Productos")
        print("3.- Buscar Producto")
        print("4.- Eliminar Producto")
        print("5.- Agregar Producto al Carrito")
        print("6.- Remover Producto del Carrito")
        print("7.- Cobrar")
        print("8.- Salir")

        op = int(input("Digite opción: "))

        if (op == 1) :
            while(True) :
                registrar_producto()
                resp = input("¿Desea agregar otro producto al Stock? [s/n]: ")
                resp = resp.lower()
                if (resp == "n") :
                    break
        elif (op == 2) :
            listar_producto()

        elif (op == 3) :
            buscar_producto()
        
        elif (op == 4) :
           eliminar_producto()

        elif (op == 5) :
            while(True) :
                agregar_carrito()
                resp = input("¿Desea agregar otro producto al Carrito? [s/n]: ")
                resp = resp.lower()
                if (resp == "n") :
                    break
            carrito_com = (Carrito)    
            vari = int(carrito_com.total_pago)
            suma = sum(vari)
            print("El TOTAL de la Compra es: ", suma)    
            res = input("¿Confirma la compra? [s/n]: ")
            res = res.lower()
            if res ==  "s" :
                cobrar()
            else :
                opc = int(input("Digite opción: "))
                print("1.-Desea Eliminar un producto del Carrito")
                print("2.-Volver al Menú y Cancelar la Compra")
                if (opc == 1) :
                    remover_carrito()
                else :
                    listaCarrito.clear()
                    
            
        elif (op == 6) :
            remover_carrito()
        
        elif (op == 7) :
            cobrar()

        elif (op == 8) :
            salir()

menu ()


