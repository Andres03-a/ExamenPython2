
def ver_productos():
    print("Productos disponibles")
    for nombre, precio in productos.items():
        print(f"{nombre} - ${precio}")
    print()

def agregar_al_carrito():
    producto = input("Escibre el producto que deseas agregar: ").lower()

    if producto in productos:
        cantidad = int(input("Cantidad: "))
        if producto in carrito:
            carrito[producto] += cantidad
        else:
            carrito[producto] = cantidad
            
        print(f"{cantidad} {producto} agregado al carrito")
    else:
        print("El producto no existe en la tienda")

def ver_carrito():
    if len(carrito) == 0:
        print("El carrito esta vacio")
    else:
        print("Carrito de compras")
        total = 0
        for item, cantidad in carrito.items():
            precio = productos[item]
            subtotal = precio * cantidad
            print(f"{item} x {cantidad} - ${subtotal}")
            total += subtotal
        print(f"Total a pagar: ${total}")

def pagar():
    if len(carrito) == 0:
        print("No puedes pagar porque el carrito esta vacio")
        return False
    total = sum(productos[item] * cantidad for item, cantidad in carrito.items())
    print(f"Total a pagar:  ${total}")
    confirmacion = input("¿Deseas pagar? Si/No: ").lower()
    if confirmacion == "si":
        print("Gracias por su compra")
        return True
    else:
        print("Pago cancelado")
        return False


productos = {
    "papas" : 2500,
    "gaseosa": 3000,
    "galletas": 1800,
    "chocolate": 2200,
    "jugo": 2800,
}

carrito = {}



while True:
    print("SUPERMERCADO OLYMPO")
    print("1. Ver productos disponibles")
    print("2. Agregar productos al carrito")
    print("3. Ver carrito de compras")
    print("4. Pagar y salir")    
    print("0. Salir sin comprar")   

    option = input("Seleccione una opcion: ")
    
    if option == "1":
        ver_productos()
    elif option == "2":
        agregar_al_carrito()
    elif option == "3":
        ver_carrito()
    elif option == "4":
        if pagar():
            break
    elif option == "0":
        print("Saliste sin comprar")
        break
    else:
        print("Opcion invalida")