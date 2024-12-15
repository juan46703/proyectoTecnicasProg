import matplotlib.pyplot as plt
from matplotlib import cm
from utils import bcolors
from collections import defaultdict

"""
Pre: listaClientes[][] (Contiene un listado con todos los clientes), listaVentasActualizadas[][] (Contiene un listado con todas las ventas), listaProductos[][] (Contiene un listado con todos los productos)
Post: Muestra un menú con las opciones de gráficos y ejecuta la opción seleccionada por el usuario
"""
def graficos(listaClientes: list, listaVentasActualizadas: list, listaProductos: list):
    continuar = True
    while continuar:
        menu()
        opcion = input("Selecciona una opción: ")
        print(
            f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
        )

        if opcion == "1":
            ventas_totales_categoria(listaProductos, listaVentasActualizadas)
        elif opcion == "2":
            productosMasVendidos(listaProductos, listaVentasActualizadas)
        elif opcion == "3":
            tendenciasPorFechas(listaVentasActualizadas)
        elif opcion == "4":
            comparativoPorCategoria(listaProductos, listaVentasActualizadas)
        elif opcion == "5":
            tendenciasPorClientes(listaVentasActualizadas, listaClientes)
        elif opcion == "6":
            print("Saliendo al menú")
            continuar = False
        else:
            print("Opción no válida, por favor intenta de nuevo.")


""" 
Pre: listaProductos[][] (Contiene un listado con todos los productos )
Post: grafico de barras con las ventas totales por categoria
"""
def ventas_totales_categoria(listaProductos: list, listaVentas: list):
    # Obtener las categorías únicas
    categorias = []
    for producto in listaProductos:
        if producto[2] not in categorias:
            categorias.append(producto[2])

    # Calcular ventas totales por categoría
    ventas_por_categoria = []
    for categoria in categorias:
        ventas_categoria = 0
        for venta in listaVentas:
            for producto in listaProductos:
                if producto[0] == venta[1] and producto[2] == categoria:
                    ventas_categoria += int(venta[2])
        ventas_por_categoria.append(ventas_categoria)

    # Generar gráfico de barras
    colors = cm.tab20.colors  # Colores dinámicos
    plt.figure(figsize=(len(categorias) * 1.0, 6))  # Tamaño dinámico
    bars = plt.bar(categorias, ventas_por_categoria, color=colors[: len(categorias)])
    plt.xlabel("Categorías")
    plt.ylabel("Ventas Totales")
    plt.title("Ventas Totales por Categoría")
    plt.xticks(rotation=45)  # Rotar etiquetas para mejor visibilidad

    # Agregar etiquetas al final de cada barra
    for bar, valor in zip(bars, ventas_por_categoria):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3,
            str(valor),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()
    plt.show()

""" 
Pre: listaProductos[][] (Contiene un listado con todos los productos ), listaVentas[] (Contiene un listado con todas las ventas)
Post: grafico de barras con los productos mas vendidos
"""
def productosMasVendidos(listaProductos: list, listaVentas: list):

    # Obtener los productos mas vendidos
    ventas_por_producto = []
    for producto in listaProductos:
        ventas_producto = 0
        for venta in listaVentas:
            if producto[0] == venta[1]:
                ventas_producto += int(venta[2])
        ventas_por_producto.append([producto[1], ventas_producto])
    
    # Ordenar los productos por ventas
    ventas_por_producto.sort(key=lambda x: x[1], reverse=True)
    
    productos= [producto[0] for producto in ventas_por_producto]
    ventas= [producto[1] for producto in ventas_por_producto]

    
    # Generar gráfico de barras
    colors = cm.tab20.colors  # Colores dinámicos
    plt.figure(figsize=(len(productos) * 0.5, 6))  # Tamaño dinámico
    bars = plt.bar(productos, ventas, color=colors[: len(productos)])
    plt.xlabel("Productos")
    plt.ylabel("Ventas Totales")
    plt.title("Productos más vendidos")
    plt.xticks(rotation=90)  # Rotar etiquetas para mejor visibilidad

    # Agregar etiquetas al final de cada barra
    for bar, valor in zip(bars, ventas):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 3,
            str(valor),
            ha="center",
            va="bottom",
            fontsize=10,
        )

    plt.tight_layout()
    plt.show()

""" 
Pre: listaVentas[][] (Contiene un listado con todas las ventas)
Post: grafico de lineas con las tendencias de ventas por fecha
"""
def tendenciasPorFechas(listaVentas: list):
    # Crear un diccionario para almacenar las ventas por año y mes
    ventas_por_mes_y_a = defaultdict(int)
    for venta in listaVentas:
        fecha = venta[3]
        a, mes, _ = fecha.split("-")
        clave = f"{a}-{mes}"  # Formato "Año-Mes"
        ventas_por_mes_y_a[clave] += int(venta[2])

    # Ordenar el diccionario por año y mes
    ventas_por_mes_y_a = dict(sorted(ventas_por_mes_y_a.items(), key=lambda x: x[0]))

    # Crear el gráfico de líneas
    plt.figure(figsize=(12, 6))
    plt.plot(ventas_por_mes_y_a.keys(), ventas_por_mes_y_a.values(), marker='o', linestyle='-', color='blue', label='Ventas Totales')
    plt.xlabel("Meses (Año-Mes)")
    plt.ylabel("Ventas Totales")
    plt.title("Tendencias de Ventas por Fecha")
    plt.xticks(rotation=45)
    plt.legend()

    # Agregar etiquetas en cada punto de la línea
    for clave, valor in ventas_por_mes_y_a.items():
        plt.text(clave, valor + 3, str(valor), ha="center", va="bottom", fontsize=10)

    plt.tight_layout()
    plt.show()


""" 
Pre: listaClientes[][] (Contiene un listado con todos los clientes), listaVentas[][] (Contiene un listado con todas las ventas)
Post: gráfico de líneas con las tendencias de ventas por cliente
"""
def tendenciasPorClientes(listaVentas: list, listaClientes: list):
    # Crear un diccionario para almacenar las ventas por cliente
    ventas_por_cliente = defaultdict(int)
    for venta in listaVentas:
        id_cliente = int(venta[4])
        cantidad = int(venta[2])
        ventas_por_cliente[id_cliente] += cantidad

    # Ordenar el diccionario por ID de cliente
    ventas_por_cliente = dict(sorted(ventas_por_cliente.items(), key=lambda x: x[0]))

    # Extraer nombres de clientes utilizando el ID
    clientes_dict = {int(cliente[0]): f"{cliente[1]} {cliente[2]} - id:{cliente[0]}" for cliente in listaClientes}

    # Crear el gráfico de líneas
    plt.figure(figsize=(12, 6))
    plt.plot(
        [clientes_dict[id_cliente] for id_cliente in ventas_por_cliente.keys()],
        ventas_por_cliente.values(),
        marker='o',
        linestyle='-',
        color='blue',
        label='Ventas Totales'
    )
    plt.xlabel("Clientes")
    plt.ylabel("Ventas Totales")
    plt.title("Tendencias de Ventas por Cliente")
    plt.xticks(rotation=45)
    plt.legend()

    # Agregar etiquetas en cada punto de la línea
    for cliente, ventas in ventas_por_cliente.items():
        nombre_cliente = clientes_dict[cliente]
        plt.text(nombre_cliente, ventas + 3, str(ventas), ha="center", va="bottom", fontsize=10)

    plt.tight_layout()
    plt.show()

""" 
Pre: listaProductos[][] (Contiene un listado con todos los productos), listaVentas[][] (Contiene un listado con todas las ventas)
Post: gráfico de pastel con el comparativo de ventas por categoría
"""
def comparativoPorCategoria(listaProductos: list, listaVentas: list):
    # Obtener las categorías únicas
    categorias = []
    for producto in listaProductos:
        if producto[2] not in categorias:
            categorias.append(producto[2])

    # Calcular ventas totales por categoría
    ventas_por_categoria = []
    for categoria in categorias:
        ventas_categoria = 0
        for venta in listaVentas:
            for producto in listaProductos:
                if producto[0] == venta[1] and producto[2] == categoria:
                    ventas_categoria += int(venta[2])
        ventas_por_categoria.append(ventas_categoria)

    # Calcular el total de ventas
    total_ventas = sum(ventas_por_categoria)

    # Generar gráfico de pastel
    colors = cm.tab20.colors  # Colores dinámicos
    plt.figure(figsize=(8, 8))  # Tamaño del gráfico
    
    # Función para mostrar porcentaje y cantidad en las etiquetas
    def func(pct, allvals):
        absolute = int(pct/100.*sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)
    
    wedges, texts, autotexts = plt.pie(ventas_por_categoria, labels=categorias, colors=colors[: len(categorias)], autopct=lambda pct: func(pct, ventas_por_categoria), startangle=140)
    
    plt.title(f"Comparativo de Ventas por Categoría\nTotal Ventas: {total_ventas}")
    plt.axis('equal')  # Asegura que el gráfico de pastel sea un círculo
    plt.setp(autotexts, size=10, weight="bold")

    plt.tight_layout()
    plt.show()

#Menu para mostrar la informacion sobre las opciones de graficos
def menu():
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    print(f"{bcolors.HEADER}Informes Gráficos{bcolors.ENDC}")

    print(f"{bcolors.OKBLUE}1. Ventas totales por categoria{bcolors.ENDC}")
    print(
        f"{bcolors.OKBLUE}2. Productos más vendidos.{bcolors.ENDC}"
    )
    print(f"{bcolors.OKBLUE}3. Tendencias de ventas por fecha{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}4. Comparativo de ventas por categoría{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}5. Tendencias de ventas por cliente{bcolors.ENDC}")

    print(f"{bcolors.WARNING}6. Salir{bcolors.ENDC}")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )