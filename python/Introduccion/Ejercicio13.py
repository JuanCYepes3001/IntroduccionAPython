
a = int(input("Juegos ganados por A: "))
b = int(input("Juegos ganado por B "))

if a >= b and a == a+2:
  print("Gano A")

elif b >= a and b == b+2:
  print("Gano B")

elif b > a:
  print("Aun no termina")

elif a > b:
  print("Aun no termina")

else:
  print("Puntaje Invalido")