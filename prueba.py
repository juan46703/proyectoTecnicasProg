def combinacionDeProductosBacktracking(productos, carrito, k, n, presupuesto, acumulado, mejor_carrito):
    # Caso base: si hemos alcanzado el presupuesto o recorrido todos los productos
    if acumulado > presupuesto:
        return
    if k == n:
        if acumulado <= presupuesto and len(carrito) > len(mejor_carrito[0]):
            mejor_carrito[0] = list(carrito)
        return

    # Tomar el producto actual
    objetoActual = productos[k][0]
    precioActual = productos[k][1]

    # Incluyendo el producto actual
    if acumulado + precioActual <= presupuesto:
        carrito.append(objetoActual)
        acumulado += precioActual
        combinacionDeProductosBacktracking(productos, carrito, k, n, presupuesto, acumulado, mejor_carrito)
        carrito.pop()
        acumulado -= precioActual

    # No incluyendo el producto actual
    combinacionDeProductosBacktracking(productos, carrito, k + 1, n, presupuesto, acumulado, mejor_carrito)

# Ejemplo de uso
productos = [('Producto1', 50), ('Producto2', 30), ('Producto3', 20)]
carrito = []
mejor_carrito = [[]]
presupuesto = 70
combinacionDeProductosBacktracking(productos, carrito, 0, len(productos), presupuesto, 0, mejor_carrito)

print("Mejor combinación:", mejor_carrito[0])
print("Presupuesto restante:", presupuesto - sum(product[1] for product in mejor_carrito[0]))
