
height = float(input("Ingrese su estatuta: "))
weight = float(input("Ingrese su peso: "))
age = int(input("Ingrese su edad: "))

imc = (weight)/(height**2)

if age < 45 and imc < 22:
  print("Tiene un riesgo bajo")

elif age >= 45 and imc < 22:
  print("Tiene un riesgo medio")

elif age < 45 and imc >= 22:
  print("Tiene un riesgo medio")

elif age >= 45 and imc >= 22:
  print("Tiene un riesgo alto")

else:
  print("No tiene riesgo ")