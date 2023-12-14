from math import sqrt as raiz
print("Encontrar el valor de la hipotenusa")
print ("Ingrese el valor de los catetos")
c1 = float(input("Cateto 1: "))
c2 = float(input("Cateto 2: "))
hh = (c1*c1)+(c2*c2)
h = raiz(hh)
print("La hipotenusa es: ", h)


