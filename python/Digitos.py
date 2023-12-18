def contar_digitos(numero):
  if numero == 0:
    return 1

  cantidad_digitos = 0
  while numero > 0:
    numero //= 10
    cantidad_digitos += 1

  return cantidad_digitos



numero = int(input("Ingrese numero: "))
cantidad_digitos = contar_digitos(numero)
print(f"{numero} tiene {cantidad_digitos} digitos")
