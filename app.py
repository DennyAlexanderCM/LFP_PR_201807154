from tkinter import Tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np


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

def analizarDatos(data):
    #Mes
    estadoMes = False
    nombreMes = ""
    #año
    estadoAnio = False
    anio = ""
    #productos
    addProducts = True
    productsList = []

    #producto
    addProductA = False
    addProductB = False

    #comillas 
    state = 0
  
    aux = ""

    for caracter in data:
        if estadoMes == False:
            if caracter != ":":
                aux += caracter
            else:
                nombreMes = aux
                estadoMes = True
                aux = ""
        elif estadoAnio == False:
            if caracter != "=":
                aux += caracter
            else:
                anio = aux
                estadoAnio = True
                aux = ""
        elif caracter == "(":
            addProducts = True
        
        elif caracter == ")":
            print("Archivo leído correctamente")

        elif addProducts == True and estadoAnio == True and estadoMes == True:
            if caracter == "[":
                addProductA = True
            elif caracter == "]":
                addProductB = True

            elif caracter == '\"':
                state += 1
            elif caracter == ";" and addProductA == True and addProductB == True and state ==2:
                lista = aux.split(",")
                lista[1] = float(lista[1])
                lista[2] = int(lista[2])
                productsList.append(lista)
                addProductA = False
                addProductB = False
                state = 0
                aux = ""
            else:
                aux += caracter

    print(nombreMes, anio)
    print(productsList)

def analizarInstrucciones(data):
    pass