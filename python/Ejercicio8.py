c1 = float(input("Ingrese nota certamen 1: "))
c2 = float(input("Ingrese nota certamen 2: "))
l1 = float(input("Ingrese nota laboratorio: "))

c3 = ((3*60) - (0.9*l1) - (0.7*c1) - (0.7*c2))/0.7
c3 = int(c3)
print("Necesita nota " + str(c3) + " en el certamen 3")