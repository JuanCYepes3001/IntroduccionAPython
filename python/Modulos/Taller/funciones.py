def leer_datos(n_maquinas, n_dias):
    horas_trabajadas = [[0 for i in range(n_dias)] for j in range(n_maquinas)]
    for i in range(n_maquinas):
        for j in range(n_dias):
            horas_trabajadas[i][j] = int(input("Ingrese las horas trabajadas por la máquina {} en el día {}: ".format(i + 1, j + 1)))
    return horas_trabajadas

def calcular_promedios(horas_trabajadas):
    promedios_por_dia = [0 for i in range(n_dias)]
    promedios_por_maquina = [0 for i in range(n_maquinas)]
    for i in range(n_maquinas):
        for j in range(n_dias):
            promedios_por_dia[j] += horas_trabajadas[i][j]
            promedios_por_maquina[i] += horas_trabajadas[i][j]
    promedios_por_dia = [promedio / n_maquinas for promedio in promedios_por_dia]
    promedios_por_maquina = [promedio / n_dias for promedio in promedios_por_maquina]
    return promedios_por_dia, promedios_por_maquina

def obtener_maxima_maquina(promedios_por_maquina):
    maxima_maquina = 0
    maximas_horas = 0
    for i in range(n_maquinas):
        if promedios_por_maquina[i] > maximas_horas:
            maxima_maquina = i
            maximas_horas = promedios_por_maquina[i]
    return maxima_maquina, maximas_horas

def obtener_minima_maquina(promedios_por_maquina):
    minima_maquina = 0
    minimas_horas = 9999
    for i in range(n_maquinas):
        if promedios_por_maquina[i] < minimas_horas:
            minima_maquina = i
            minimas_horas = promedios_por_maquina[i]
    return minima_maquina, minimas_horas

def obtener_maximo_dia(promedios_por_dia):
    maximo_dia = 0
    maximas_horas = 0
    for i in range(n_dias):
        if promedios_por_dia[i] > maximas_horas:
            maximo_dia = i
            maximas_horas = promedios_por_dia[i]
    return maximo_dia, maximas_horas

def obtener_minimo_dia(promedios_por_dia):
    minimo_dia = 0
    minimas_horas = 9999
    for i in range(n_dias):
        if promedios_por_dia[i] < minimas_horas:
            minimo_dia = i
            minimas_horas = promedios_por_dia[i]
    return minimo_dia, minimas_horas
