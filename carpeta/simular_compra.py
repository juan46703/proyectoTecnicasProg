from utils import bcolors
import csv

"""
pre: listaProductos[][] (Contiene un listado con todos los productos )
post: archivo de salida sumulacion_venta.csv. Simular la compra de productos y mostrar el carrito de compras
"""
def simular_compra_funcion(listaProductos: list):
    print(f"{bcolors.HEADER}Simular compra {bcolors.ENDC}")
    carrito = []
    # Obtener la informacón de los productos e imprimir el menú de opciones
    for i, fila in enumerate(listaProductos):
        print(
            f"{bcolors.OKGREEN}{i+1}.{bcolors.ENDC} {fila[1]} - {fila[2]} - {fila[3]} - {fila[4]}"
        )
    # Generar ciclo de compras
    confirmar: bool = True
    # id venta
    id = 1
    while confirmar:
        producto = int(
            input(
                f"{bcolors.HEADER}{bcolors.UNDERLINE}Ingrese el número del producto que desea comprar (0 para salir):{bcolors.ENDC} "
            )
        )
        if producto == 0:
            confirmar = False
        elif producto > len(listaProductos):
            print(f"{bcolors.FAIL}Producto no encontrado{bcolors.ENDC}")
        else:
            cantidad = int(
                input(
                    f"{bcolors.HEADER}{bcolors.UNDERLINE}Ingrese la cantidad que desea comprar:{bcolors.ENDC} "
                )
            )
            if cantidad <= 0:
                print(f"{bcolors.FAIL}Cantidad no válida{bcolors.ENDC}")

            elif cantidad > int(listaProductos[producto - 1][4]):
                print(f"{bcolors.FAIL}Cantidad no disponible{bcolors.ENDC}")
            else:
                # Añadir la seleccion del producto al carrito
                carrito.append(
                    [
                        listaProductos[producto - 1][1],
                        listaProductos[producto - 1][3],
                        cantidad,
                    ]
                )

                # Actualizar la cantidad de productos disponibles
                listaProductos[producto - 1][4] = (
                    int(listaProductos[producto - 1][4]) - cantidad
                )

                # Crear el archivo CSV de la simulacion de la compra, siendo una venta mas
                with open("simulacion_venta.csv", "w", newline="") as archivo:
                    escritor_csv = csv.writer(archivo)
                    encabezado = ["producto", "precio_unidad", "cantidad"]
                    escritor_csv.writerow(encabezado)
                    escritor_csv.writerows(carrito)

                print(f"{bcolors.OKGREEN}Producto agregado al carrito{bcolors.ENDC}")
                print("¿Desea agregar otro producto?")
                print(f"{bcolors.OKGREEN}1.{bcolors.ENDC} Si")
                print(f"{bcolors.OKRED}2.{bcolors.ENDC} No")
                confirmar = int(input("Ingrese el número de la opción: ")) == 1

    print(f"{bcolors.OKRED}Carrito de compras:{bcolors.ENDC} ")

    precio_total = 0
    for i in carrito:
        print(
            f"{bcolors.OKGREEN}Producto:{bcolors.ENDC} {i[0]}, {bcolors.OKGREEN}Precio por unidad:{bcolors.ENDC} {i[1]}, {bcolors.OKGREEN}Cantidad:{bcolors.ENDC} {i[2]}, {bcolors.OKGREEN}Precio total por producto:{bcolors.ENDC} {int(i[2])*int(i[1])}"
        )
        precio_total += int(i[2]) * int(i[1])
    print(f"{bcolors.OKGREEN}Precio total de la compra:{bcolors.ENDC} {precio_total}")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    input("Enter para continuar en el menu: ")
