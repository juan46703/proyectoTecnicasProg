import csv
from datetime import datetime
from utils import bcolors

"""
   Pre: listaProductos[][] (Contiene un listado con todos los productos dispoinibles), listaVentas[] (Contiene una lita con todas las ventas)
   Pos: Proyeccion del mes siguiente teniendo en cuenta las ventas de un porducto en los meses anteriores
"""
def venta_futura(listaProductos: list):

    """
     Pre: str id_producto (el id del producto a estimar venta siguiente)
     Pos: cantidadDeVenta[][] (matriz que contiene en orden ascendente por fecha las ventas de cada mes del producto)
    """
    def obtener_ventas(id_producto: str):
        with open("ventas_actualizadas.csv", "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar e encabezado
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

    """
     Pre: int menor, mayor (la cantidad de ventas de un periodo de tiempo y las del siguiente a este)
     Pos: float crecimiento_porcentual (el crecimiento porcentual de la cantida de ventas un periodo de tiempo con repecto al siguiente)
    """
    def crecimiento_porcentual(menor, mayor):
        # Validar cual de los dos es el mayor y el menor
        if menor > mayor:
            aux = menor
            mayor = aux
            menor = mayor
        # Retornar el crecimiento porcentual
        return ((mayor - menor) / menor) * 100
    
    """
     Pre: ventas [] (lista que contiene la cantidad de ventas de un producto ordenadas por periodos de tiempo ascendentes)
     Pos: agrega a una lista los crecimiento porcentuales de cada periodo respecto al siguiente, si llega a una sublista con un solo valor devuleve 0 porque no hubo crecimiento
    """
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
    
    # While que controla el funcionamiento del ciclo para calcular tendencias que quiera el usuario
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
            # Calcular los crecimientos porcentuales usando divide y vencerás
            proyeccion_crecimiento_divide_venceras(listaVentas)

            suma = 0
            for i in crecimientos:
                suma += i
            # Promediar los crecimientos porcentuales
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
