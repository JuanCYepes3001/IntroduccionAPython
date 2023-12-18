def calcular_digito_verificador(rol):

  longitud_rol = len(rol)

  rol_invertido = rol[::-1]
  
  multiplicaciones = []
  for i in range (int(longitud_rol)):
    if i % 6 == 0:
      multiplicaciones.append(int(rol_invertido[i]))
    else:
      multiplicaciones.append(int(rol_invertido[i] * (i % 6 + 2)))

    resultado = sum(multiplicaciones)

  resto = resultado % 11

  digito_verificador = 11 - resto
  return digito_verificador


rol = str(input("Ingrese su rol UTFSM sin guión ni dígito verificador: "))
digito_verificador = calcular_digito_verificador(rol)
print(f"El dígito verificador de su rol es {rol} - {digito_verificador}")
