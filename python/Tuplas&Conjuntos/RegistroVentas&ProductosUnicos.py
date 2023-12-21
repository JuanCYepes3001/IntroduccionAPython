ventas = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
]

ventas_por_producto = {}

for producto, cantidad, precio in ventas:
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0

    ventas_por_producto[producto] += cantidad

productos_con_mas_de_10_ventas = set()

for producto, cantidad in ventas_por_producto.items():
    if cantidad > 10:
        productos_con_mas_de_10_ventas.add(producto)


ganancia_total = 0

for producto, cantidad, precio in ventas:
    ganancia_total += precio * cantidad

print(ventas_por_producto)
print(productos_con_mas_de_10_ventas)
print(ganancia_total)
