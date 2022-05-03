from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import scrolledtext as st

from constantes import *

current_directory = Path.cwd()   # Permite conocer el directorio actual.
current_path = Path(current_directory)


class Ventana(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.marco_izq = tk.Frame()            #contenedor izquierdo
        self.marco_izq.config(background="#FDFEFE")
        self.marco_izq.place(relx=0.0, rely=0.0, relwidth=0.85 ,relheight=1)

        self.marco_der = tk.Frame()             #contenedor derecho
        self.marco_der.config(background="#F2F4F4")
        self.marco_der.place(relx=0.85, rely=0.0, relwidth=0.15 ,relheight=1)


        self.etiqueta_entrada_texto = tk.Label(self.marco_izq,text="Ingrese su texto:")   #etiqueta de la entrada de texto
        self.etiqueta_entrada_texto.place(relx=0.01, rely=0.01)
        self.etiqueta_entrada_texto.config(background="white")

        self.entrada_texto = st.ScrolledText(self.marco_izq, font=("Calibri 10"))     #entrada de texto
        self.entrada_texto.config(background="#FCF3CF")
        self.entrada_texto.place(relx=0.01, rely=0.05, relwidth=0.98, relheight= 0.45, )


        self.boton_abrir_archivo = ttk.Button(self.marco_der,text="Abrir", command= lambda: abrir_archivos(self))
        self.boton_abrir_archivo.place(relx=0.1, rely=0.05, relwidth=0.8)       #botón Abrir

        self.boton_guardar = ttk.Button(self.marco_der,text="Guardar", command= lambda: guardar_archivo(self))
        self.boton_guardar.place(relx=0.1, rely=0.12, relwidth=0.8)             #botón Guardar

        self.etiqueta_tamaño_fuente = tk.Label(self.marco_der, text="Tamaño de la letra")   #etiqueta botones cambiar tamaño de la fuente
        self.etiqueta_tamaño_fuente.place(relx=0.1, rely=0.82, relwidth=0.8)

        self.mas_fuente = ttk.Button(self.marco_der, text="+")     
        self.mas_fuente.place(relx=0.1, rely=0.86, relwidth=0.4)

        self.menos_fuente = ttk.Button(self.marco_der, text="-")
        self.menos_fuente.place(relx=0.5, rely=0.86, relwidth=0.4)

        
        def guardar_archivo(self):      #funcion para guardar el archivo enlazada al boton Guardar
            nombre_archivo = fd.asksaveasfilename(initialdir= current_directory, title = "Guardar como", filetypes= (("cody files",".cody"),("todos los archivos","*.*")) )
            if nombre_archivo != '':
                archivo = open(nombre_archivo,"w", encoding= "utf-8")
                archivo.write(self.entrada_texto.get("1.0", "end-1c"))
                archivo.close()
                print("archivo guardado")

        def abrir_archivos(self):       #funcion para abrir un archivo enlazado al boton Abrir
            nombre_archivo = fd.askopenfilename(initialdir= current_directory, title= "Abrir nota", filetypes= (("cody files", ".cody"),("todos los arcivos","*.*")))
            if nombre_archivo != '':
                archivo = open(nombre_archivo, "r", encoding= "utf-8")
                contenido = archivo.read()
                self.entrada_texto.delete(1.0,"end-1c")
                self.entrada_texto.insert(1.0, contenido)


root = tk.Tk()
root.title("Cuaderno de Notas")
root.config(width=WIDTH, height=HEIGHT) #dimensiones de la ventana
root.config(bg="white") #color del fondo
root.iconphoto(True, tk.PhotoImage(file='notepad.png')) #icono el la app

app = Ventana(root)

root.mainloop()