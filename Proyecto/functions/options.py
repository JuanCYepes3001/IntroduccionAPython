import tkinter as tk
from tkinter import messagebox
import RegistrarCamper
def mostrar_opcion(opcion):
    label_resultado.config(text=f'Se seleccionó: {opcion}')

#################
####REPORTES#####
#################
def opcion_1():
        # Limpiar la ventana anterior
        for widget in ventana.winfo_children():
            widget.destroy()

        label_titulo.config(text="Reportes")

        opciones_reportes = [
            "Campers Inscritos",
            "Campers Aprobados examen inicial",
            "Entrenadores",
            "Campers bajo rendimiento",
            "Campers y entrenador por ruta",
            "Campers A/R por modulo"
        ]

        for opcion in opciones_reportes:
            if opcion == "Campers Inscritos":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_1)
                boton_reportes.pack(pady=5)
            elif opcion == "Campers Aprobados examen inicial":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_2)
                boton_reportes.pack(pady=5)
            elif opcion == "Entrenadores":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_3)
                boton_reportes.pack(pady=5)
            elif opcion == "Campers bajo rendimiento":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_4)
                boton_reportes.pack(pady=5)
            elif opcion ==  "Campers y entrenador por ruta":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_5)
                boton_reportes.pack(pady=5)
            elif opcion == "Campers A/R por modulo":
                boton_reportes = tk.Button(ventana, text=opcion, command=opcion_6)
                boton_reportes.pack(pady=5)

            else:
                boton = tk.Button(ventana, text=opcion, command=lambda o=opcion: mostrar_opcion(o))
                boton.pack(pady=5)

        label_resultado = tk.Label(ventana, text="")
        label_resultado.pack(pady=10)

        ventana.mainloop()
        boton_reporte = tk.Button(ventana, text=opcion, command=lambda o=opcion: mostrar_opcion(o))
        boton_reporte.pack(pady=5)
#################
###REPGISTRO-C###
#################
def opcion_2 ():
    for widget in ventana.winfo_children():
        widget.destroy()
    label_titulo.config(text="Registro Camper")
    RegistrarCamper.guardar_datos()
    ventana = tk.Tk()
    ventana.title("Agregar Datos a CSV")
    RegistrarCamper.insertar_datos()
    ventana.mainloop()
#################
####REGISTRO-P###
#################
def opcion_3 ():
    for widget in ventana.winfo_children():
        widget.destroy()
    label_titulo.config(text="Registro Prueba Inicio")

#################
###REGISTRO-A####
#################
def opcion_4 ():
    for widget in ventana.winfo_children():
        widget.destroy()
    label_titulo.config(text="Registro area")
    
#################
###CREAR RUTA####
#################
def opcion_5 ():
    for widget in ventana.winfo_children():
        widget.destroy()
    label_titulo.config(text="Crear Ruta De Aprendizaje")
    
#################
###GESTOR MAT####
#################
def opcion_6 (): 
    for widget in ventana.winfo_children():
        widget.destroy()
    label_titulo.config(text="Gestor De Matricula")
    
def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("Campuslands")

    label_titulo = tk.Label(ventana, text="Campuslands", font=("Helvetica", 16))
    label_titulo.pack(pady=10)

    opciones = [
        "Reportes",
        "Registrar Camper",
        "Registro de Prueba",
        "Registro Areas Entrenamiento",
        "Crear Ruta de Entrenamiento",
        "Gestionar Matricula"
    ]

    for opcion in opciones:
        if opcion == "Reportes":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_1)
            boton_reportes.pack(pady=5)
        elif opcion == "Registrar Camper":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_2)
            boton_reportes.pack(pady=5)
        elif opcion == "Registro de Prueba":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_3)
            boton_reportes.pack(pady=5)
        elif opcion == "Registro Areas Entrenamiento":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_4)
            boton_reportes.pack(pady=5)
        elif opcion == "Crear Ruta de Entrenamiento":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_5)
            boton_reportes.pack(pady=5)
        elif opcion == "Gestionar Matricula":
            boton_reportes = tk.Button(ventana, text=opcion, command=opcion_6)
            boton_reportes.pack(pady=5)
        
        else:
            boton = tk.Button(ventana, text=opcion, command=lambda o=opcion: mostrar_opcion(o))
            boton.pack(pady=5)

    label_resultado = tk.Label(ventana, text="")
    label_resultado.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
