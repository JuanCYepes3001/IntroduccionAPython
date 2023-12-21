def cargar_palabra():
  return input("Ingrese la palabra que desea adivinar: ")

def mostrar_tablero(intentos):
  if intentos == 6:
    print("ahorcado")
  elif intentos == 5:
    print("pierna derecha")
  elif intentos == 4:
    print("pierna izquierda")
  elif intentos == 3:
    print("brazo derecho")
  elif intentos == 2:
    print("brazo izquierdo")
  elif intentos == 1:
    print("tronco")
  else:
    print("cabeza")

def adivinar_letra(letra, palabra, soluciones):
  encontrado = False
  for i in range(len(palabra)):
    if palabra[i] == letra:
      soluciones[i] = letra
      encontrado = True
  return encontrado

print ("Bienvenido al juego del ahorcado")
x = 1
while x ==1 :
  palabra = cargar_palabra()
  soluciones = ["_" for i in range(len(palabra))]
  intentos = 6
  while intentos > 0 and "_" in soluciones:
    letra = input("Ingrese letra: ")
    if letra in soluciones:
      print("Ya ingresaste esa letra!")
      continue
    if adivinar_letra(letra, palabra, soluciones):
      print("Correcto! La palabra es:", "".join(soluciones))
    else:
      intentos -= 1
      mostrar_tablero(intentos)
  if intentos > 0:
    print("Has ganado!")
  else:
    print("Has perdido!")
    print ("¿Deseas jugar de nuevo?")
    print ("1. Continuar juego")
    print ("2. Salir del juego")
    input("  ")
    


