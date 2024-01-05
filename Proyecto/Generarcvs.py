import csv
from faker import Faker
import random

fake = Faker()

def generar_datos_camper():
    nombre_camper = fake.first_name()
    apellidos_camper = fake.last_name()
    numero_identificacion = fake.unique.random_number(9, True)
    nombre_acudiente = fake.name()
    direccion_camper = fake.address()
    telefono_camper = fake.phone_number()
    estado_camper = random.choice(['A', 'R'])
    ruta = random.choice(['NodeJS', 'Java', 'NetCore'])
    profesor = random.choice(['Carlos', 'Pedro', 'Andres', 'Pepe', 'Mario'])
    salon = random.choice(['Artemis', 'Sputnik', 'Apolo'])
    horario = random.choice(['Mañana1', 'Mañana2', 'Tarde1', 'Tarde2'])
    modulo = random.choice(['fundamentos', 'ProgramacionWeb', 'ProgramacionNormal', 'DB', 'backend'])

    return [nombre_camper, apellidos_camper, str(numero_identificacion), nombre_acudiente,
            direccion_camper, telefono_camper, estado_camper, ruta, profesor, salon,
            horario, modulo]

# Generar 100 conjuntos de datos
datos_camper = [generar_datos_camper() for _ in range(100)]

# Escribir los datos en un archivo CSV
with open('datos_camper.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Escribir la fila de encabezado
    csv_writer.writerow(['Nombre Camper', 'Apellidos Camper', 'Numero de identificacion', 'Nombre Acudiente',
                         'Direccion Camper', 'Telefono Camper', 'Estado Camper', 'Ruta', 'Profesor',
                         'Salon', 'Horario', 'Modulo'])
    # Escribir los datos
    csv_writer.writerows(datos_camper)

print("Archivo CSV generado con éxito: datos_camper.csv")
