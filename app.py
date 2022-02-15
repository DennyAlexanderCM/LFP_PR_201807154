from tkinter import *
from tkinter import filedialog

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num 

def leerArchivo():
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Data","*.data"),("Todos los archivos","*.*")))
    if root != "":
        file = open(root,'r')
        contentFile = file.read()
        return contentFile
    return None