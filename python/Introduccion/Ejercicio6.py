
hr = int(input("Ingrese la hora: "))
qhr = int(input("Ingrese cuantas horas van a pasar: "))

fhr = (hr + qhr)%12
print("En " + str(qhr) + ", el reloj marcara las " + str(fhr))

