# empezando con tkinter 
# programa hecho por Daniel Perez

""" tkinter consta de 3 partes
>>> widgets
>>> layout
>>> style
""" 

import tkinter as tk

#from tkinter import ttk
import ttkbootstrap as ttk


def convertir() -> None: 
    entrada_millas: int = entry_Int.get()
    km_salida: float = entrada_millas * 1.61
    output_string.set("Resultado = %.2f" %km_salida)
    #output_string.set(f"Resultado = {km_salida:.2f}") no es necesario poner la l
    #output_string.set("Resultado = {:.2f}".format(km_salida))
    #output_string.set("Resultado = {0:.2f}".format(km_salida))
    #output_string.set("Resultado = {xd:.2f}".format(xd=km_salida))
    
    
# ventana 
#window: object = tk.Tk()
# window: object = ttk.Window(themename="journal")
window: object = ttk.Window(themename="darkly")
window.title(string="Demo")
window.geometry(newGeometry="300x150")

# title
title_label: object = ttk.Label(master=window,text="Miles to kilometers",font=("Fira Code",15,"bold"))
title_label.pack()

# entrada de datos
input_frame: object = ttk.Frame(master=window)
entry_Int: object = tk.IntVar(master=window)
entry = ttk.Entry(master=input_frame,textvariable=entry_Int)
button = ttk.Button(master=input_frame,text="Convertir",command=convertir)
entry.pack(side="left",padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# salida de datos
output_string: object = tk.StringVar()
output_label: object = ttk.Label(master=window,
text="Salida",#no se muestra por que la textvariable lo sobreescribe
font=("Fira Code",15,"bold"),
textvariable=output_string).pack(pady=5)
# ejecutar
window.mainloop()
#14:40