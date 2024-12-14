import csv
from utils import bcolors


def clientes_productos(
    listaClientes: list, listaVentasActualizadas: list, listaProductos: list
):
    categorias = []
    for producto in listaProductos:
        if producto[2] not in categorias:
            categorias.append(producto[2])

    print(f"{bcolors.HEADER}Lista de categorias:{bcolors.ENDC}")
    for i, categoria in enumerate(categorias):
        print(f"{bcolors.OKBLUE}{i + 1}. {categoria}{bcolors.ENDC}")

    seguir = True
    while seguir:
        categoria = int(input("Ingrese el número de la categoria (0 para salir): "))
        print(
            f"{bcolors.OKRED}----------------------------------------------{bcolors.ENDC}"
        )
        print(
            f"{bcolors.OKGREEN}Clientes y productos de la categoría seleccionada:{bcolors.ENDC}"
        )
        if categoria == 0:
            seguir = False
        if categoria > len(categorias):
            print(f"Categoria no encontrada")
        else:
            clientesDeCategoria = []
            for producto in listaProductos:
                # Encontrar la categoria en la lista de productos
                if producto[2] == categorias[categoria - 1]:
                    for venta in listaVentasActualizadas:
                        # Encontrar el id del producto en la lista de ventas
                        if venta[1] == producto[0]:
                            for cliente in listaClientes:
                                # Encontrar el id del cliente en la lista de ventas
                                if cliente[0] == venta[4]:
                                    clientesDeCategoria.append(
                                        [cliente[1], cliente[2], venta[2], producto[1]]
                                    )

                                    print(
                                        f"{cliente[1]} {cliente[2]} compró {venta[2]} unidades de {producto[1]}"
                                    )

            # Encontrar el cliente que más compró verificando la cantidad de unidades compradas
            clienteFinal = clientesDeCategoria[0]
            for cliente in clientesDeCategoria:
                if int(cliente[2]) > int(clienteFinal[2]):
                    # Guardar el cliente con la mayor cantidad de unidades compradas
                    clienteFinal = cliente
            print(
                f"\n{bcolors.OKBLUE}{clienteFinal[0]} {clienteFinal[1]} compró {bcolors.ENDC} {bcolors.WARNING}{clienteFinal[2]} unidades de {clienteFinal[3]}{bcolors.ENDC}, {bcolors.OKGREEN}siendo el cliente que más compró{bcolors.ENDC}"
            )
