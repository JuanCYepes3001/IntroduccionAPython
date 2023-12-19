from math import sqrt as sqrt

def desviacion_estandar(valores):
 
  media = sum(valores) / len(valores)
 
  distancias_al_cuadrado = []
  for valor in valores:
    distancia_al_cuadrado = (valor - media)**2
    distancias_al_cuadrado.append(distancia_al_cuadrado)

  varianza = sum(distancias_al_cuadrado) / (len(valores) - 1)

  desviacion_estandar = sqrt(varianza)

  return desviacion_estandar

print(desviacion_estandar([1.3, 1.3, 1.3]))  # 0.0
print(desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]))  # 4.88535225615
print(desviacion_estandar([1.5, 9.5]))  # 5.65685424949
