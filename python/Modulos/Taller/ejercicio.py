import funciones
n_maquinas = 15
n_dias = 7

# Leer los datos
horas_trabajadas = funciones.leer_datos(n_maquinas, n_dias)

# Calcular las estadísticas
promedios_por_dia, promedios_por_maquina = funciones.calcular_promedios(horas_trabajadas)
maxima_maquina, maximas_horas = funciones.obtener_maxima_maquina(promedios_por_maquina)
minima_maquina, minimas_horas = funciones.obtener_minima_maquina(promedios_por_maquina)
maximo_dia, maximas_horas = funciones.obtener_maximo_dia(promedios_por_dia)

