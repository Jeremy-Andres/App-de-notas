import tkinter as tk
from tkinter import ttk

from constantes import *

def obtener_texto():
    entrada = entrada_texto.get("1.0", "end-1c")
    return entrada

root = tk.Tk()      #crear y configurar la ventana
root.title("NOTAS")
root.config(width=WIDTH, height=HEIGHT)
root.config(bg="white")


marco_izq = tk.Frame()      #creacion del frame del lado izquierdo
marco_izq.config(background="#FDFEFE")
marco_izq.place(relx=0.0, rely=0.0, relwidth=0.75 ,relheight=1)

marco_der = tk.Frame()      #creacion del frame del lado derecho
marco_der.config(background="#F2F4F4")
marco_der.place(relx=0.76, rely=0.0, relwidth=0.25 ,relheight=1)


etiqueta_entrada_texto = tk.Label(marco_izq,text="Ingrese su texto:")     #etiqueta de la entrada de texto
etiqueta_entrada_texto.place(relx=0.01, rely=0.01)
etiqueta_entrada_texto.config(background="white")

entrada_texto = tk.Text(marco_izq, font=("Calibri 10"))        #entrada de texto
entrada_texto.config(background="#FCF3CF")
entrada_texto.place(relx=0.01, rely=0.05, relwidth=0.99, relheight= 0.45)

boton_guardar = ttk.Button(marco_der,text="Guardar", command= lambda: obtener_texto())
boton_guardar.place(relx=0.1, rely=0.05, relwidth=0.8)

boton_borrar = ttk.Button(marco_der,text="Borrar")
boton_borrar.place(relx=0.1, rely=0.13, relwidth=0.8)




root.mainloop()