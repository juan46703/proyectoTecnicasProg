def encontrarMenorValor(productos: list):
    menorValor = float("inf")
    for i in productos:
        if i[1] < menorValor:
            menorValor = i[1]
    return menorValor

# No se pase del presupuesto (valorProducto + acumulado <= presupuesto)
def esViable1(valorProducto: float, acumulado: float, presupuesto: float):
    return valorProducto + acumulado <= presupuesto

# Los productos en carritos no excedan la cantidad disponible del producto que se agregará
def esViable2(producto: str, cantidad: int, carrito: list):
    return carrito.count(producto) < cantidad

def contar_productos(carrito, acumulado, presupuesto):
    # Crear un diccionario para almacenar las cantidades de cada producto
    contador_productos = {}

    # Recorrer cada producto en el carrito
    for producto in carrito:
        if producto in contador_productos:
            contador_productos[producto] += 1  # Incrementar el conteo si el producto ya está en el diccionario
        else:
            contador_productos[producto] = 1  # Añadir el producto al diccionario con un conteo inicial de 1

    # Crear una lista para almacenar las partes del mensaje
    mensaje_partes = []
    for producto, cantidad in contador_productos.items():
        mensaje_partes.append(f"{producto}: {cantidad}")

    # Unir las partes del mensaje en una sola cadena
    mensaje_final = ", ".join(mensaje_partes)
    print(mensaje_final,', Devuelta: ', presupuesto-acumulado)


def combinacionDeProductos(productos: list, carrito: list, k: int, presupuesto: float, acumulado: float):
    # Condición de corte
    if presupuesto - acumulado < precioMenor or k == len(productos):
        contar_productos(carrito, acumulado, presupuesto)
    else:
        for i in range(k, len(productos)):
            producto, precio, cantidadDisponible = productos[i]
            # Verificar si el producto a añadir es viable
            if esViable1(precio, acumulado, presupuesto) and esViable2(producto, cantidadDisponible, carrito):
                # Añadir el producto al carrito
                carrito.append(producto)
                acumulado += precio
                combinacionDeProductos(productos, carrito, i, presupuesto, acumulado)
                # Restaurar el estado después de la recursión
                carrito.pop()
                acumulado -= precio
            # Si no hay presupuesto suficiente
            if (not(esViable2(producto, cantidadDisponible, carrito))):
                contar_productos(carrito, acumulado, presupuesto)

# Parámetros iniciales
presupuesto = 75
acumulado = 0
productos = [
    ["laptop", 1200, 3],
    ["smartphone", 700, 2],
    ["tablet", 250, 1],
    ["audifonos", 150, 2],
    ["cargador", 50, 2],
    ["chaquetas", 120, 2],
    ["jeans", 50, 3],
    ["manzanas", 2, 10],
    ["peras", 3, 5],
    ["uvas", 1, 100]
]
precioMenor = encontrarMenorValor(productos)
k = 0
carrito = []
print(f'Posibles compras con presupuesto de: {presupuesto}')
combinacionDeProductos(productos, carrito, k, presupuesto, acumulado)