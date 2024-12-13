import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def estimacion_venta_futura(id_producto: str):
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

def proyeccion_promedios_divide_venceras(ventas):
    # Caso base: si solo hay un punto, devolver su valor
    if len(ventas) == 1:
        return ventas[0]

    # Caso base: si solo hay dos puntos, devolver el promedio
    if len(ventas) == 2:
        return np.mean(ventas)

    # Dividir el conjunto de datos en dos mitades
    mitad = len(ventas) // 2
    ventas_izquierda = ventas[:mitad]
    ventas_derecha = ventas[mitad:]

    # Calcular el promedio para cada mitad
    promedio_izquierda = proyeccion_promedios_divide_venceras(ventas_izquierda)
    promedio_derecha = proyeccion_promedios_divide_venceras(ventas_derecha)

    # Promediar los resultados
    promedio_final = (promedio_izquierda + promedio_derecha) / 2

    return promedio_final

# Obtener los datos de ventas
ventas = estimacion_venta_futura('102')
print("Ventas:", ventas)

# Calcular la proyección usando promedios con divide y vencerás
proyeccion_futura = proyeccion_promedios_divide_venceras(ventas)

print("Proyección para el próximo mes (divide y vencerás):", proyeccion_futura)

# Graficar los datos y la proyección
plt.scatter(range(1, len(ventas) + 1), ventas, color='blue', label='Datos de ventas')
plt.axhline(y=proyeccion_futura, color='red', linestyle='--', label='Proyección futura')

plt.xlabel('Tiempo')
plt.ylabel('Ventas')
plt.title('Proyección de Ventas con Promedios y Divide y Vencerás')
plt.legend()
plt.grid(True)
plt.show()
