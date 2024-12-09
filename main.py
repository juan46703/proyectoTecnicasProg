import funciones as f
from funciones import bcolors

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
    print(f"{bcolors.OKGREEN}6. Informes gráficos{bcolors.ENDC}")
    print(f"{bcolors.WARNING}7. Salir{bcolors.ENDC}")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )


def opcion2():
    print("Has seleccionado la Opción 2")


def opcion3():
    print("Has seleccionado la Opción 3")


continuar = True
while continuar:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )

    if opcion == "1":
        f.resumenInicial()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        f.simular_compra()
    elif opcion == "7":
        print("Saliendo del programa...")
        continuar = False
    else:
        print("Opción no válida, por favor intenta de nuevo.")
