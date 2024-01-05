import tkinter as tk
from tkinter import messagebox
import csv

def guardar_datos():
        identificacion = entry_identificacion.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        direccion = entry_direccion.get()
        acudiente = entry_acudiente.get()
        telefono = entry_telefono.get()

        if not (identificacion and nombre and apellido and direccion and acudiente and telefono):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        with open('datos.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([identificacion, nombre, apellido, direccion, acudiente, telefono])

        entry_identificacion.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_acudiente.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Datos guardados correctamente.")

def insertar_datos():
    
        label_identificacion = tk.Label(ventana, text="Identificación:")
        label_identificacion.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        entry_identificacion = tk.Entry(ventana)
        entry_identificacion.grid(row=0, column=1, padx=10, pady=5)

        label_nombre = tk.Label(ventana, text="Nombre:")
        label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        label_apellido = tk.Label(ventana, text="Apellido:")
        label_apellido.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        entry_apellido = tk.Entry(ventana)
        entry_apellido.grid(row=2, column=1, padx=10, pady=5)

        label_direccion = tk.Label(ventana, text="Dirección:")
        label_direccion.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        entry_direccion = tk.Entry(ventana)
        entry_direccion.grid(row=3, column=1, padx=10, pady=5)

        label_acudiente = tk.Label(ventana, text="Acudiente:")
        label_acudiente.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
        entry_acudiente = tk.Entry(ventana)
        entry_acudiente.grid(row=4, column=1, padx=10, pady=5)

        label_telefono = tk.Label(ventana, text="Teléfono:")
        label_telefono.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        entry_telefono = tk.Entry(ventana)
        entry_telefono.grid(row=5, column=1, padx=10, pady=5)

        boton_guardar = tk.Button(ventana, text="Guardar Datos", command=RegistrarCamper.guardar_datos)
        boton_guardar.grid(row=6, column=0, columnspan=2, pady=10)