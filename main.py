import csv
from utils import bcolors
from carpeta import resumen_inicial as ri
from carpeta import estimacion_venta_futura as evf
from carpeta import simular_compra as sc
from carpeta import backtracking as b
from carpeta import fuerza_bruta as fb
from carpeta import fuerza_bruta_mejorada as fbm
from carpeta import informacion_grafica as gr

# Leer los archivos CSV
with open("productos.csv", "r") as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)
    listaProductos = list(lector_csv)

with open("clientes.csv", "r") as archivo:
    clientesReader = csv.reader(archivo)
    # Saltar el encabezado
    next(clientesReader)
    listaClientes = list(clientesReader)

with open("ventas.csv", "r") as archivo:
    ventasReader = csv.reader(archivo)
    next(ventasReader)
    listaVentas = list(ventasReader)

with open("ventas_actualizadas.csv", "r") as archivo:
    ventasReader = csv.reader(archivo)
    next(ventasReader)
    listaVentasActualizadas = list(ventasReader)

""" 
    post: imprimir en la consola el menu principal    
"""

def mostrar_menu():
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKRED}Sistema de Análisis de Ventas - Menú Principal{bcolors.ENDC}"
    )
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    print(f"{bcolors.OKGREEN}1. Mostrar resumen inicial{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}2. Estimar ventas futuras de un producto{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}3. Simular compra{bcolors.ENDC}")
    print(
        f"{bcolors.OKGREEN}4. Revisión de productos dentro de un presupuesto{bcolors.ENDC}"
    )
    print(f"{bcolors.OKGREEN}5. Análisis de clientes y productos{bcolors.ENDC}")
    print(
        f"{bcolors.OKGREEN}6. Análisis de clientes y productos optimizada{bcolors.ENDC}"
    )
    print(f"{bcolors.OKGREEN}7. Informes gráficos{bcolors.ENDC}")
    print(f"{bcolors.WARNING}8. Salir{bcolors.ENDC}")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )

productos = [
    ["laptop", 1200, 3],
    ["smartphone", 700, 2],
    ["tablet", 250, 1],
    ["audifonos", 150, 2],
    ["cargador", 50, 2],
    ["chaquetas", 120, 2],
    ["manzanas", 2, 10],
]
continuar = True
while continuar:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )

    if opcion == "1":
        ri.resumenInicial(listaClientes, listaProductos, listaVentas)
    elif opcion == "2":
        evf.venta_futura(listaProductos)
    elif opcion == "3":
        sc.simular_compra_funcion(listaProductos)
    elif opcion == "4":
        # revision_productos_presupuesto(productos:list, acumulado:float, carrito:list)
        b.revision_productos_presupuesto(productos, 0, [])
    elif opcion == "5":
        fb.clientes_productos(listaClientes, listaVentasActualizadas, listaProductos)
    elif opcion == "6":
        fbm.fuerzaBrutaMejorada(listaClientes, listaVentasActualizadas, listaProductos)
    elif opcion == "7":
        gr.graficos()
    elif opcion == "8":
        print("Saliendo del programa...")
        continuar = False
    else:
        print("Opción no válida, por favor intenta de nuevo.")
