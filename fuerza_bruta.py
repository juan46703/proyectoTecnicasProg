import csv
def clientes_productos():
    print('Lista de categorias:') #Agregar colores
    for i, categoria in enumerate(categorias):
       print(f"{i+1}. {categoria}")
    print("Enter para ver el resultado de las categorias seleccion")
    seguir = True
    while seguir:
        categoria=int(input("Ingrese el número de la categoria (0 para salir): "))
        if categoria == 0:
            seguir = False
        if categoria > len(categorias):
            print(f"Categoria no encontrada")
        else:
            clientesDeCategoria = []
            for producto in productos:
                #Encontrar la categoria en la lista de productos
                if producto[2] == categorias[categoria-1]:
                    for venta in ventas:
                        #Encontrar el id del producto en la lista de ventas
                        if venta[1] == producto[0]:
                            for cliente in clientes:
                                #Encontrar el id del cliente en la lista de ventas
                                if cliente[0] == venta[4]:
                                    clientesDeCategoria.append([cliente[1], cliente[2], venta[2], producto[1]])
                                    
                                    print(f"{cliente[1]} {cliente[2]} compró {venta[2]} unidades de {producto[1]}")
                                    
            #Encontrar el cliente que más compró verificando la cantidad de unidades compradas
            clienteFinal=clientesDeCategoria[0]
            for cliente in clientesDeCategoria:
                if int(cliente[2]) > int(clienteFinal[2]):
                    #Guardar el cliente con la mayor cantidad de unidades compradas
                    clienteFinal = cliente
            print(f"{clienteFinal[0]} {clienteFinal[1]} compró {clienteFinal[2]} unidades de {clienteFinal[3]}, siendo el cliente que más compró")

with open("clientes.csv", "r") as archivo:
    clientesReader = csv.reader(archivo)
    next(clientesReader)
    clientes = list(clientesReader)

with open("ventas_actualizadas.csv", "r") as archivo:
    ventasReader = csv.reader(archivo)
    next(ventasReader)
    ventas = list(ventasReader)
    
with open("productos.csv", "r") as archivo:
    productosReader = csv.reader(archivo)
    next(productosReader)
    productos = list(productosReader)
    categorias = []
    for producto in productos:
        if producto[2] not in categorias:
            categorias.append(producto[2])

clientes_productos()