def invertir_digitos(n):
 
  longitud_n = len(str(n))

  n_invertido = 0
  for i in range(longitud_n - 1, -1, -1):
    n_invertido *= 10
    n_invertido += int(str(n)[i])

  return n_invertido

def es_palindromo(n):
  n_invertido = invertir_digitos(n)
  return n == n_invertido



n = int(input("Ingrese n: "))

print (f"El numero invertido es {invertir_digitos(n)}")
es_palindromo = es_palindromo(n)
if es_palindromo:
  print("Es palíndromo")
else:
  print("No es palíndromo")
