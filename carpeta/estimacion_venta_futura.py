import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from utils import bcolors


def venta_futura(listaProductos: list):
    def obtener_ventas(id_producto: str):
        with open("ventas_actualizadas.csv", "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar la cabecera
            listaVentas = list(lector)
        listaVentasProducto = []
        for venta in listaVentas:
            if int(venta[1]) == int(id_producto):
                listaVentasProducto.append(venta)
        # Ordenar la lista por fecha
        listaVentasProducto.sort(key=lambda x: datetime.strptime(x[3], "%Y-%m-%d"))

        # Solo retornar la cantidad de ventas
        cantidadDeVenta = [int(venta[2]) for venta in listaVentasProducto]
        return cantidadDeVenta

    def crecimiento_porcentual(menor, mayor):
        if menor > mayor:
            aux = menor
            mayor = aux
            menor = mayor
        return ((mayor - menor) / menor) * 100

    def proyeccion_crecimiento_divide_venceras(ventas: list):
        # Caso base: si solo hay un punto, no se puede calcular el crecimiento porcentual
        if len(ventas) <= 1:
            crecimientos.append(0)
            return
        # Caso base: si solo hay dos puntos, calcular el crecimiento porcentual entre ellos
        elif len(ventas) == 2:
            crecimientos.append(crecimiento_porcentual(ventas[0], ventas[1]))
            return
        else:
            # Dividir el conjunto de datos en dos mitades
            mitad = len(ventas) // 2
            ventas_izquierda = ventas[:mitad]
            ventas_derecha = ventas[mitad:]
            # Calcular el crecimiento porcentual para cada mitad
            proyeccion_crecimiento_divide_venceras(ventas_izquierda)
            proyeccion_crecimiento_divide_venceras(ventas_derecha)

    print(f"{bcolors.HEADER}Estimar ventas futuras{bcolors.ENDC}")
    # Obtener la informacón de los productos e imprimir el menú de opciones
    for i, fila in enumerate(listaProductos):
        print(
            f"{bcolors.OKGREEN}{i+1}.{bcolors.ENDC} {fila[1]} - {fila[2]} - id: {fila[0]}"
        )
    bool = True
    while bool:
        print(
            f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
        )
        id_producto = int(
            input(
                f"{bcolors.HEADER}{bcolors.UNDERLINE}Ingrese el id del producto (0 para salir):{bcolors.ENDC} "
            )
        )
        if id_producto == 0:
            bool = False
        if id_producto not in list(map(lambda x: int(x[0]), listaProductos)):
            bool = False
            print(f"\n{bcolors.OKBLUE}Producto no encontrado{bcolors.ENDC}")

        else:
            listaVentas = []
            listaVentas = obtener_ventas(id_producto)
            print("Ventas:", listaVentas)
            crecimientos = []
            # Calcular el crecimiento porcentual promedio usando divide y vencerás
            proyeccion_crecimiento_divide_venceras(listaVentas)

            suma = 0
            for i in crecimientos:
                suma += i
            crecimiento_promedio = suma / len(crecimientos)
            print(
                f"\n{bcolors.OKBLUE}Crecimiento porcentual promedio: {bcolors.ENDC} {bcolors.WARNING}{round(crecimiento_promedio, 1)}{bcolors.ENDC}"
            )
            # Proyección de la próxima venta utilizando el crecimiento porcentual promedio
            ultima_venta = listaVentas[-1]
            proxima_venta = ultima_venta * (1 + crecimiento_promedio / 100)
            print(
                f"{bcolors.OKGREEN}Proyección para el próximo mes: {bcolors.ENDC} {bcolors.WARNING}{round(proxima_venta,0)}{bcolors.ENDC}"
            )
