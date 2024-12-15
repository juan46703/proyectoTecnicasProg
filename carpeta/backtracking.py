from utils import bcolors

"""
Pre: listProductos[][] (matriz que contiene la información de los productos disponibles), float acumulado (la cantidad de dinero que se ha gastado la persona en cada producto agregado al carrito), carrito[]
Pos: imprime todas las posibles combinaciones de productos que puede hacer el usuario dependiendo de su presupuesto y de la disponibildad de los productos
"""
def revision_productos_presupuesto(listProductos: list, acumulado: float, carrito: list):
    k = 0
    carrito = []

    # Pedir presupuesto
    presupuesto = int(input("Ingrese el presupuesto: "))
    print(
        f"{bcolors.OKGREEN}Posibles compras con presupuesto de: {bcolors.ENDC}{bcolors.OKCYAN}{presupuesto}{bcolors.ENDC}"
    )
    # Guardar en una matriz el nombre del producto, el valor por unidad y la cantidad disponible
    productos =[]
    for producto in listProductos:
        productos.append([producto[1], int(producto[3]), int(producto[4])])

    precioMenor = encontrarMenorValor(productos)
    combinacionDeProductos(productos, carrito, k, presupuesto, acumulado, precioMenor)
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    input("Enter para continuar en el menu: ")

"""
    Pre: productos [][] (matriz que contiene la informacion de cada producto(nombre, precio, cantidad))
    Pos: float menorValor (el precio del producto que menos vale por unidad)
"""
def encontrarMenorValor(productos: list):
    menorValor = float("inf")
    for i in productos:
        if i[1] < menorValor:
            menorValor = i[1]
    return menorValor

"""
    Pre: float valorProducto, acumulado, presupuesto
    Pos: bool que indica que el producto es viable para añadir al carrito (si al añadirlo no se pasa del presupuesto)
"""
def esViable1(valorProducto: float, acumulado: float, presupuesto: float):
    # No se pase del presupuesto
    return valorProducto + acumulado <= presupuesto

"""
    Pre: str producto (nombre), int cantidad, carrito[]
    Pos: bool que indica que el producto es viable para añadir al carrito (si al añadirlo no se pasa de la cantidad disponible de ese producto)
"""
def esViable2(producto: str, cantidad: int, carrito: list):
    # Los productos en carritos no excedan la cantidad disponible del producto que se agregará
    return carrito.count(producto) < cantidad

"""
    Pre: carrito[], float acumulado, presupuesto
    Pos: imprime el carrito, mostrando la cantidad que se compró de cada producto y cuuanto dinero se le debería devolver al cliente si esocge esa combinación
"""
def contar_productos(carrito, acumulado, presupuesto):
    # Crear un diccionario para almacenar las cantidades de cada producto
    contador_productos = {}

    # Recorrer cada producto en el carrito
    for producto in carrito:
        if producto in contador_productos:
            contador_productos[producto] += 1  # Incrementar el conteo si el producto ya está en el diccionario
        else:
            contador_productos[producto] = (1  # Añadir el producto al diccionario con un conteo inicial de 1
                                            )

    # Crear una lista para almacenar las partes del mensaje
    mensaje_partes = []
    for producto, cantidad in contador_productos.items():
        mensaje_partes.append(
            f"{bcolors.OKBLUE}{producto}{bcolors.ENDC}: {bcolors.HEADER}{cantidad}{bcolors.ENDC}"
        )

    # Unir las partes del mensaje en una sola cadena
    mensaje_final = ", ".join(mensaje_partes)
    print(
        f"{mensaje_final}, {bcolors.FAIL}Devuelta: {bcolors.ENDC}{bcolors.WARNING}{presupuesto-acumulado}{bcolors.ENDC}"
    )


"""
    Pre: productos[][] (matriz con la informacion de los productos), carrito[] (donde se guardarán los nombres de los productos a añadir), int k (maneja profundidad del árbol, indica desde donde avanzar en el recorrido de los productos), float presupuesto, acumulado, precioMenor (precio del producto que menos cuesta)
    Pos: recorre las posibles combinaciones con cada producto y verifica si es una solucion, una vez la encuentra imprime el carrito y se devuelve en el árbol para hallar más combinaciones
"""
def combinacionDeProductos(
    productos: list, carrito: list, k: int, presupuesto: float, acumulado: float, precioMenor: float
):
    # Condición de corte (si lo que queda de dinero no es suficiente para comprar el producto de menor valor o si he llegado a la profundidad máxima)
    if presupuesto - acumulado < precioMenor or k == len(productos):
        contar_productos(carrito, acumulado, presupuesto)
    else:
        for i in range(k, len(productos)):
            producto, precio, cantidadDisponible = productos[i]
            # Verificar si el producto a añadir es viable
            if esViable1(precio, acumulado, presupuesto) and esViable2(
                producto, cantidadDisponible, carrito
            ):
                # Añadir el producto al carrito
                carrito.append(producto)
                acumulado += precio
                combinacionDeProductos(
                    productos, carrito, i, presupuesto, acumulado, precioMenor
                )
                # Restaurar el estado después de la recursión
                carrito.pop()
                acumulado -= precio
            # Si hay presupuesto pero no hay mas de ese producto
            if not (esViable2(producto, cantidadDisponible, carrito)):
                contar_productos(carrito, acumulado, presupuesto)

