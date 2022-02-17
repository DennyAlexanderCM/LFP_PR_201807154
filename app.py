from tkinter import Tk
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

def leerArchivo(tipo):
    root = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(('File',f'*{tipo}'),('All Files','*.*')))
    if root != "":
        #encoding utf-8
        file = open(root,'r',encoding='utf-8')
        #En dado caso hayan espacios al incio y al final de la cadena strip se encarga de eliminarlos
        contentFile = file.read().strip()
        #Convertimos todo el documento en minusculas
        contentFile = cleanData(contentFile.lower())
        return contentFile
    return None

def cleanData(data):
    txt = ""
    add = False
    for caracter in data:
        if caracter != '\"':
            if (caracter != " " and caracter != "\t" and caracter != "\n") or add:
                txt += caracter
        elif not add:
            txt += caracter
            add = True
        else:
            txt += caracter
            add = False    
    return txt

def analizarProductos(data):
    nombres = []
    cantidad = []
    dates = {}
    for i in data['productos']:
        nombres.append(i.getNombre())
        cantidad.append(i.getTotalGanancias())
    
    dates['Nombres'] = nombres
    dates['Ventas'] = cantidad
    
    return dates