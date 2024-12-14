from utils import bcolors


#Grafico de ventas totales por categoría.
def ventas_totales_categoria(listaProductos: list, listaVentas: list):
    categorias = []
    for producto in listaProductos:
        if producto[2] not in categorias:
            categorias.append(producto[2])
    ventas_por_categoria = []
    for categoria in categorias:
        ventas_categoria = 0
        for venta in listaVentas:
            for producto in listaProductos:
                if producto[0] == venta[1] and producto[2] == categoria:
                    ventas_categoria += int(venta[2])
        ventas_por_categoria.append(ventas_categoria)
    print(categorias)
    print(ventas_por_categoria)
    
def menu():
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )
    print(f"{bcolors.HEADER}Informes Gráficos{bcolors.ENDC}")

    print(f"{bcolors.OKBLUE}1. Ventas totales por ctegoria{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}2. Productos más vendidosProductos más vendidos.{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}3.{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}4. Comparativo de ventas por categoría{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}5. Gráfico de tendencia de ventas{bcolors.ENDC}")
    print(f"{bcolors.WARNING}6. Salir{bcolors.ENDC}")
    print(
        f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
    )

def graficos():
    continuar = True
    while continuar:
        menu()
        opcion = input("Selecciona una opción: ")
        print(
            f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
        )

        if opcion == "1":
            ventas_totales_categoria()
        elif opcion == "2":
            productosMasVendidos()
        elif opcion == "3":
            tendenciasPorFechas()
        elif opcion == "4":
            comparativoPorCategoria()
        elif opcion == "5":
            tendencias()
        elif opcion == "6":
            print("Saliendo al menú")
            continuar = False
        else:
            print("Opción no válida, por favor intenta de nuevo.")
