import csv
from utils import bcolors

""" Pre: listaClientes[][] (Contiene un listado con todos los clientes), listaVentasActualizadas[][] (Contiene una lista con todas las ventas actualizadas), listaProductos[][] (Contiene una lista con todos los productos)"""
def fuerzaBrutaMejorada(
    listaClientes: list, listaVentasActualizada: list, listaProductos: list
):
    
    """
    Post: Carga los datos de las listas y retorna una nueva lista que solo contiene las categorias de los productos
    """
    def cargar_datos():
        categorias = list({producto[2] for producto in listaProductos})
        return listaClientes, listaVentasActualizada, listaProductos, categorias
    """"
    Pre: categoria (str), listaProductos [][], listaVentasActualizada [][], listaClientes [][]
    Pos: clientesDeCategoria [][]  (lista con los clientes que compraron productos de la categoria seleccionada)"""
    def obtener_clientes_por_categoria(
        categoria, listaProductos, listaVentasActualizada, listaClientes
    ):
        clientesDeCategoria = []

        # Crear un diccionario con los productos de la categoría
        productos_categoria = {
            producto[0]: producto[1]
            for producto in listaProductos
            if producto[2] == categoria
        }

        # Iterar sobre las ventas y obtener los clientes que compraron productos de la categoría
        for venta in listaVentasActualizada:
            producto_id = venta[1]

            if producto_id in productos_categoria:
                cliente_id = venta[4]
                for cliente in listaClientes:
                    if cliente[0] == cliente_id:
                        clientesDeCategoria.append(
                            [cliente[1],cliente[2],int(venta[2]),productos_categoria[producto_id]]
                        )

        return clientesDeCategoria
    """ Pre: clientesDeCategoria [][] (lista con los clientes que compraron productos de la categoria seleccionada), inicio (int), fin (int)
    Pos: cliente[] con la mayor cantidad de unidades compradas"""
    def encontrar_cliente_top_divide_venceras(clientes, inicio, fin):
        # Caso base: si hay un solo cliente
        if inicio == fin:
            return clientes[inicio]

        # Dividir la lista en dos mitades
        mitad = (inicio + fin) // 2

        # Encontrar el cliente que más compró en cada mitad, dividir el array en dos subarrays y asi recursivamente
        cliente_izquierda = encontrar_cliente_top_divide_venceras(
            clientes, inicio, mitad
        )
        cliente_derecha = encontrar_cliente_top_divide_venceras(
            clientes, mitad + 1, fin
        )

        # Comparar los resultados y retornar el cliente con mayor cantidad
        return (cliente_izquierda if cliente_izquierda[2] >= cliente_derecha[2] else cliente_derecha)

    
        """ Post: Muestra el cliente que más compró de una categoría seleccionada por el usuario
        """
    def clientes_productos():
        clientes, ventas, productos, categorias = cargar_datos()

        print(f"{bcolors.HEADER}Lista de categorias:{bcolors.ENDC}")
        for i, categoria in enumerate(categorias):
            print(f"{bcolors.OKGREEN}{i + 1}. {categoria}{bcolors.ENDC}")

        bool = True
        while bool:
            try:
                opcion = input("Ingrese el número de la categoria (0 para salir): ")
                if not opcion.isdigit():
                    print("Por favor, ingrese un número válido.")
                    continue

                categoria_idx = int(opcion)
                if categoria_idx == 0:
                    print("Saliendo...")
                    bool = False

                if categoria_idx < 1 or categoria_idx > len(categorias):
                    print("Categoría no encontrada. Intente nuevamente.")
                    continue

                categoria_seleccionada = categorias[categoria_idx - 1]
                clientesDeCategoria = obtener_clientes_por_categoria(
                    categoria_seleccionada, productos, ventas, clientes
                )

                if not clientesDeCategoria:
                    print(f"No se encontraron clientes para la categoría '{categoria_seleccionada}'.")
                    continue

                print(
                    f"\n{bcolors.OKBLUE}Clientes que compraron en la categoría '{categoria_seleccionada}{bcolors.ENDC}"
                )
                for cliente in clientesDeCategoria:
                    print(
                        f"{cliente[0]} {cliente[1]} compró {bcolors.OKGREEN}{cliente[2]}{bcolors.ENDC} unidades de {cliente[3]}"
                    )

                # Usar divide y vencerás para encontrar al cliente top
                cliente_top = encontrar_cliente_top_divide_venceras(
                    clientesDeCategoria, 0, len(clientesDeCategoria) - 1
                )
                if cliente_top:
                    print(
                        f"\n{bcolors.OKBLUE}El cliente que más compró es: {bcolors.ENDC}{bcolors.HEADER}{cliente_top[0]} {cliente_top[1]}{bcolors.ENDC}, con {bcolors.OKGREEN}{cliente_top[2]}{bcolors.ENDC} unidades de {bcolors.FAIL}{cliente_top[3]}{bcolors.ENDC}"
                    )

            except Exception as e:
                print(f"Ocurrió un error: {e}")

    clientes_productos()
