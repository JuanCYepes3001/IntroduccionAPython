def todos_distintos(lista):
  conjunto = set(lista)
  return len(lista) == len(conjunto)

def todos_iguales(lista):
  primer_elemento = lista[0]
  for elemento in lista:
    if elemento != primer_elemento:
      return False
  return True

tamaño = int(input("Ingrese el tamaño de la lista: "))

lista = []
for i in range(tamaño):
  dato = input("Ingrese el dato {}: ".format(i + 1))
  lista.append(dato)
opcion = input("¿Desea comprobar si todos los elementos de la lista son iguales (1) o distintos (2)? ")

if opcion == "1":
  distintos = todos_iguales(lista)
  print("Todos los elementos de la lista son iguales:", distintos)
elif opcion == "2":
  iguales = todos_distintos(lista)
  print("Todos los elementos de la lista son distintos:", iguales)
else:
  print("Opción no válida.")



