import csv
from collections import defaultdict

def cargar_datos():
    with open("clientes.csv", "r") as archivo:
        clientesReader = csv.reader(archivo)
        next(clientesReader)
        clientes = list(clientesReader)

    with open("ventas_actualizadas.csv", "r") as archivo:
        ventasReader = csv.reader(archivo)
        next(ventasReader)
        ventas = list(ventasReader)

    with open("productos.csv", "r") as archivo:
        productosReader = csv.reader(archivo)
        next(productosReader)
        productos = list(productosReader)

    categorias = list({producto[2] for producto in productos})
    return clientes, ventas, productos, categorias

def obtener_clientes_por_categoria(categoria, productos, ventas, clientes):
    clientesDeCategoria = []

    productos_categoria = {producto[0]: producto[1] for producto in productos if producto[2] == categoria}

    for venta in ventas:
        producto_id = venta[1]
        if producto_id in productos_categoria:
            cliente_id = venta[4]
            for cliente in clientes:
                if cliente[0] == cliente_id:
                    clientesDeCategoria.append([cliente[1], cliente[2], int(venta[2]), productos_categoria[producto_id]])

    return clientesDeCategoria

def encontrar_cliente_top_divide_venceras(clientes, inicio, fin):
    # Caso base: si hay un solo cliente
    if inicio == fin:
        return clientes[inicio]

    # Dividir la lista en dos mitades
    mitad = (inicio + fin) // 2

    # Encontrar el cliente que más compró en cada mitad
    cliente_izquierda = encontrar_cliente_top_divide_venceras(clientes, inicio, mitad)
    cliente_derecha = encontrar_cliente_top_divide_venceras(clientes, mitad + 1, fin)

    # Comparar los resultados y retornar el cliente con mayor cantidad
    return cliente_izquierda if cliente_izquierda[2] >= cliente_derecha[2] else cliente_derecha

def clientes_productos():
    clientes, ventas, productos, categorias = cargar_datos()

    print('Lista de categorias:')
    for i, categoria in enumerate(categorias):
        print(f"{i + 1}. {categoria}")

    while True:
        try:
            opcion = input("Ingrese el número de la categoria (0 para salir): ")
            if not opcion.isdigit():
                print("Por favor, ingrese un número válido.")
                continue

            categoria_idx = int(opcion)
            if categoria_idx == 0:
                print("Saliendo...")
                break

            if categoria_idx < 1 or categoria_idx > len(categorias):
                print("Categoría no encontrada. Intente nuevamente.")
                continue

            categoria_seleccionada = categorias[categoria_idx - 1]
            clientesDeCategoria = obtener_clientes_por_categoria(categoria_seleccionada, productos, ventas, clientes)

            if not clientesDeCategoria:
                print(f"No se encontraron clientes para la categoría '{categoria_seleccionada}'.")
                continue

            print(f"\nClientes que compraron en la categoría '{categoria_seleccionada}':")
            for cliente in clientesDeCategoria:
                print(f"{cliente[0]} {cliente[1]} compró {cliente[2]} unidades de {cliente[3]}")

            # Usar divide y vencerás para encontrar al cliente top
            cliente_top = encontrar_cliente_top_divide_venceras(clientesDeCategoria, 0, len(clientesDeCategoria) - 1)
            if cliente_top:
                print(f"\nEl cliente que más compró es: {cliente_top[0]} {cliente_top[1]}, con {cliente_top[2]} unidades de {cliente_top[3]}.")
            print("\n")

        except Exception as e:
            print(f"Ocurrió un error: {e}")

# Ejecutar el programa
clientes_productos()