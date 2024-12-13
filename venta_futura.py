import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def obtener_ventas(id_producto: str):
    with open('ventas_actualizadas.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar la cabecera
        listaVentas = list(lector)
    listaVentasProducto = []
    for venta in listaVentas:
        if venta[1] == id_producto:
            listaVentasProducto.append(venta)
    
    # Ordenar la lista por fecha
    listaVentasProducto.sort(key=lambda x: datetime.strptime(x[3], "%Y-%m-%d"))

    # Solo retornar la cantidad de ventas
    cantidadDeVenta = [int(venta[2]) for venta in listaVentasProducto]
    return cantidadDeVenta

def crecimiento_porcentual(menor, mayor):
    return ((mayor - menor) / menor) * 100

def proyeccion_crecimiento_divide_venceras(ventas):
    # Caso base: si solo hay un punto, no se puede calcular el crecimiento porcentual
    if len(ventas) <= 1:
        crecimientos.append(0)

    # Caso base: si solo hay dos puntos, calcular el crecimiento porcentual entre ellos
    elif len(ventas) == 2:
        crecimientos.append(crecimiento_porcentual(ventas[0], ventas[1]))
    
    else:
        # Dividir el conjunto de datos en dos mitades
        mitad = len(ventas) // 2
        ventas_izquierda = ventas[:mitad]
        ventas_derecha = ventas[mitad:]

        # Calcular el crecimiento porcentual para cada mitad
        proyeccion_crecimiento_divide_venceras(ventas_izquierda)
        proyeccion_crecimiento_divide_venceras(ventas_derecha)


crecimientos = []

listaVentas= obtener_ventas('102')
print("Ventas:", listaVentas)

# Calcular el crecimiento porcentual promedio usando divide y vencerás
proyeccion_crecimiento_divide_venceras(listaVentas)
print(crecimientos)
suma = 0
for i in crecimientos:
    suma+=i
crecimiento_promedio = suma/len(crecimientos)

print("Crecimiento porcentual promedio (divide y vencerás): ", round(crecimiento_promedio,1),"%")

# Proyección de la próxima venta utilizando el crecimiento porcentual promedio
ultima_venta = listaVentas[-1]
proxima_venta = ultima_venta * (1 + crecimiento_promedio / 100)

print("Proyección para el próximo mes (divide y vencerás):", round(proxima_venta,0))