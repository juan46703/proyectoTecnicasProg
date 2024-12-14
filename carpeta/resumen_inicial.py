import csv
from utils import bcolors
import random


def resumenInicial(listaClientes: list, listaProductos: list, listaVentas: list):
    print(f"{bcolors.HEADER}Resumen inicial {bcolors.ENDC}")

    with open("ventas.csv", "r") as archivo:
        ventasReader = csv.reader(archivo)
        # Saltar el encabezado
        next(ventasReader)
        # Obtener la venta máxima, y el id del producto
        maxVent: int = 0
        id = ""
        contador = 0
        for venta in ventasReader:
            if int(venta[2]) > maxVent:
                maxVent = int(venta[2])
                id = str(venta[1])
            contador += 1
        print(f"Cantidad de ventas: {bcolors.OKGREEN}{contador}{bcolors.ENDC}")

        print(
            f"Cantidad de clientes: {bcolors.OKGREEN}{len(listaClientes)}{bcolors.ENDC}"
        )

        # Verificar el id del producto con mayor cantidad de ventas
        for producto in listaProductos:
            if producto[0] == id:
                nombre = producto[1]
                categoria = producto[2]
            contador += 1
        print(f"Cantidad de productos: {bcolors.OKGREEN}{contador}{bcolors.ENDC}")
        print(
            f"Producto con mayor cantidad de ventas: {bcolors.OKGREEN}{nombre.lower()}{bcolors.ENDC}, con {bcolors.OKGREEN}{maxVent}{bcolors.ENDC} ventas y su categoria es: {bcolors.OKGREEN}{categoria.lower()}{bcolors.ENDC}"
        )
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )

    """ pre: archivos de entrada: clientes.csv, productos.csv, ventas.csv
        post: archivo de salida: ventas_actualizadas.csv, imprimir en la consola la relación de ventas y clientes
    """

    def relacion_venta_cliente(listaVentas: list):
        print(f"{bcolors.HEADER}Relación de ventas y clientes {bcolors.ENDC}")

        # Añadir la nueva columna a cada fila
        for fila in listaVentas:
            # Añadir el id del cliente al final de la fila
            fila.append(random.randint(1, len(listaClientes)))

        # Escribir el archivo CSV actualizado, con la columna que contiene los id de los clientes
        with open("ventas_actualizadas.csv", "w", newline="") as archivo:
            escritor_csv = csv.writer(archivo)
            encabezado = ["id_venta", "id_producto", "cantidad", "fecha", "id_cliente"]
            escritor_csv.writerow(encabezado)
            escritor_csv.writerows(listaVentas)

        # Leer el archivo ventas_actualizadas.csv para obtener los id de los productos que cada cliente ha comprado y añadirlo al diccionario
        with open("ventas_actualizadas.csv", "r") as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)
            relacion = dict()

            # Obtener la informacón de los clientes
            for line in lector_csv:
                relacion["Venta " + line[0]] = {
                    "id_venta": line[0],
                    "id_producto": line[1],
                    "cantidad": line[2],
                    "fecha": line[3],
                    "id_cliente": line[4],
                }

        for i, venta in relacion.items():
            for j in range(len(listaProductos)):
                if venta["id_producto"] == listaProductos[j][0]:
                    venta["Producto"] = {
                        "nombre_producto": listaProductos[j][1],
                        "categoria_producto": listaProductos[j][2],
                        "precio_producto": listaProductos[j][3],
                    }
            for k in range(len(listaClientes)):
                if venta["id_cliente"] == listaClientes[k][0]:
                    venta["Cliente"] = {
                        "nombre_cliente": listaClientes[k][1],
                        "apellido_cliente": listaClientes[k][2],
                        "email_cliente": listaClientes[k][4],
                    }
            # Imprimir con buen formato la relación de ventas y clientes
            print(
                f"{bcolors.OKGREEN}Id venta:{bcolors.ENDC} {venta['id_venta']}, {bcolors.OKGREEN}Producto:{bcolors.ENDC} {venta['Producto']['nombre_producto']}, {bcolors.OKGREEN}Precio por unidad:{bcolors.ENDC} {venta['Producto']['precio_producto']}, {bcolors.OKGREEN}Cantidad:{bcolors.ENDC} {venta['cantidad']}, {bcolors.OKGREEN}Precio total:{bcolors.ENDC} {int(venta['cantidad'])*int(venta['Producto']['precio_producto'])}, {bcolors.OKGREEN}Cliente:{bcolors.ENDC} {venta['Cliente']['nombre_cliente']} {venta['Cliente']['apellido_cliente']}"
            )

    relacion_venta_cliente(listaVentas)
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    input("Enter para continuar en el menu: ")
