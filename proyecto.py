#Agregar productos cantidad nombre precio



precio = []
producto = []
#cantidad = []
#id = []

print("Bienvenido a la Tienda")

print("Elija que desea hacer")
print("1_Agregar Nuevo Producto")
print("2_Remover un producto")
print("3_Agregar un producto al carrito de compras")
print("4_Eliminar un prodcuto del carrito de compras")

opcion =int(input())

if (opcion == 1) :
    #print(usuario,"Ingrese el producto que quieres agregar")
    producIng = input("Ingresa el nombre del producto que quiere agregar:")
    producto.append(producIng)
    precioIng = input("Ingresa el precio del producto que quieres agregar:")
    precio.append(precioIng)


print("Estos son los productos en stock",producto)