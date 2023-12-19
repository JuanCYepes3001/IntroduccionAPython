n = int(input("¿Cuántos datos ingresará? "))
datos = []

for i in range(n):
  datos.append(float(input("Ingrese el dato {}: ".format(i + 1))))

promedio = sum(datos) / n
cantidad = 0

for dato in datos:
  if dato > promedio:
    cantidad += 1

print("Hay {} datos mayores que el promedio".format(cantidad))
