from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")


ventana = Tk()
ventana.title("Proyecto Algoritmos Geneticos")
ventana.geometry("500x500")

lbl =Label(ventana,text="Generacion de individuos")
lbl.pack()

btn = Button(ventana, text="Generar poblacion aleatoria", command = miFuncion)
btn.pack()
#Agregar cambiar posicion del boton
#Agregar Textboxes para definir los parametros de la generacion


ventana.mainloop()