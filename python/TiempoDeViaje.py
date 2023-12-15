def calcular_tiempo_viaje(tiempos):
    total_minutos = 0
    for tiempo in tiempos:
        if tiempo == 0:
            return total_minutos // 60, total_minutos % 60
        total_minutos += tiempo
    return total_minutos // 60, total_minutos % 60

tiempos = []
while True:
    tiempo = int(input("Ingrese el tiempo de un tramo del viaje (0 para terminar): "))
    if tiempo == 0:
        break
    tiempos.append(tiempo)

horas, minutos = calcular_tiempo_viaje(tiempos)
print("El tiempo total del viaje es:", horas, ":", minutos)
