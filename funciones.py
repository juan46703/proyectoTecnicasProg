import csv
import random


def resumenInicial():
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

    with open("clientes.csv", "r") as archivo:
        clientesReader = csv.reader(archivo)
        # Saltar el encabezado
        next(clientesReader)
        # Convertir el lector a lista para obtener la cantidad de ventas
        clientes = list(clientesReader)
        print(f"Cantidad de clientes: {bcolors.OKGREEN}{len(clientes)}{bcolors.ENDC}")

    with open("productos.csv", "r") as archivo:
        productosReader = csv.reader(archivo)
        # Saltar el encabezado
        next(productosReader)
        contador = 0
        # Verificar el id del producto con mayor cantidad de ventas
        for producto in productosReader:
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

    def relacion_venta_cliente():
        with open("clientes.csv", "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            filas = list(lector)
            listCliente = []
            # Obtener la informacón de los clientes
            for line in filas:
                listCliente.append(line)

        with open("productos.csv", "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            listProductos = []
            # Obtener la informacón de los productos
            for line in lector:
                listProductos.append(line)

        # Añadir la columna id_cliente al archivo ventas.csv
        with open("ventas.csv", "r") as archivo:
            lector_csv = csv.reader(archivo)
            filas = list(lector_csv)

        # Añadir la nueva columna a cada fila
        for i, fila in enumerate(filas):
            if i == 0:
                # Añadir el encabezado
                fila[4] = "id_cliente"
            else:
                # Añadir el id del cliente al final de la fila
                fila[4] = random.randint(1, len(listCliente))

        # Escribir el archivo CSV actualizado, con la columna que contiene los id de los clientes
        with open("ventas.csv", "w", newline="") as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerows(filas)

        # Leer el archivo ventas.csv para obtener los id de los productos que cada cliente ha comprado y añadirlo al diccionario
        with open("ventas.csv", "r") as archivo:
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
            for j in range(len(listProductos)):
                if venta["id_producto"] == listProductos[j][0]:
                    venta["Producto"] = {
                        "nombre_producto": listProductos[j][1],
                        "categoria_producto": listProductos[j][2],
                        "precio_producto": listProductos[j][3],
                    }
            for k in range(len(listCliente)):
                if venta["id_cliente"] == listCliente[k][0]:
                    venta["Cliente"] = {
                        "nombre_cliente": listCliente[k][1],
                        "apellido_cliente": listCliente[k][2],
                        "email_cliente": listCliente[k][4],
                    }
            # Imprimir con buen formato la relación de ventas y clientes
            print(
                f"{bcolors.OKGREEN}Id venta:{bcolors.ENDC} {venta['id_venta']}, {bcolors.OKGREEN}Producto:{bcolors.ENDC} {venta['Producto']['nombre_producto']}, {bcolors.OKGREEN}Precio por unidad:{bcolors.ENDC} {venta['Producto']['precio_producto']}, {bcolors.OKGREEN}Cantidad:{bcolors.ENDC} {venta['cantidad']}, {bcolors.OKGREEN}Precio total:{bcolors.ENDC} {int(venta['cantidad'])*int(venta['Producto']['precio_producto'])}, {bcolors.OKGREEN}Cliente:{bcolors.ENDC} {venta['Cliente']['nombre_cliente']} {venta['Cliente']['apellido_cliente']}, {bcolors.OKGREEN}Email:{bcolors.ENDC} {venta['Cliente']['email_cliente']}"
            )

    relacion_venta_cliente()
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    input("Enter para continuar en el menu: ")


# Clase para colores en la terminal
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    OKRED = "\033[91m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
