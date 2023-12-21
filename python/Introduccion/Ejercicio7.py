import math
flt = float(input("Ingrese un numero: "))

prtdem, prtint = math.modf(flt)

print(str(prtdem))