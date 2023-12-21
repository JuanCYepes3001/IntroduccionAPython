n = int(input("Cual numero desea ingresar: "))
lsnum = []
for i in range(n):
  num = int(input("Ingrese un numero: "))
  lsnum.append(num)

lsnum.sort()
print(lsnum)
