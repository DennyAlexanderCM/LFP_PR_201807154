from distutils.log import error
import matplotlib.pyplot as plt
import numpy as np

class Graficas():
    def __init__(self):
        self.mes = ""
        self.grafica = ""
        self.titulo = ""
        self.titulox = ""
        self.tituloy = ""
        self.ejex = []
        self.ejey = []

    def generarGrafica(self, data, dataInstructions, mesAnio):
        tipoGrafica = dataInstructions['grafica']
        if tipoGrafica == 'barras':
            self.crearGraficaBarras(data, dataInstructions, mesAnio)
        elif tipoGrafica == 'lineas':
            self.crearGraficaLineal(data, dataInstructions, mesAnio)
        elif tipoGrafica == 'líneas':
            self.crearGraficaLineal(data, dataInstructions, mesAnio)
        elif tipoGrafica == 'pie':
            self.crearGraficaSectores(data, dataInstructions, mesAnio)
        else:
            print("Tipo de gráfica incorrecto\n")

    def crearGraficaBarras(self, data, dataInstructions, mesAnio):
        #asociamos los datos
        productos = np.array(data['Nombres'])
        ventas = np.array(data['Ventas'])
        #Realizamos cambios al formato de la gráfica
        plt.figure(figsize=(10,5))
        plt.subplots_adjust(bottom=0.3, right=0.93)
        plt.xticks(size = 'small', rotation = 60, ha = 'right')
        plt.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
        #Agregamos los datos a la gráfica
        plt.bar(productos, ventas, color = '#f06123')
        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        else: plt.title(mesAnio[0] + " - " + mesAnio[1], fontdict = {'fontsize':14, 'fontweight':'bold'})

        if 'titulox' in dataInstructions:
            plt.xlabel(dataInstructions['titulox'], fontdict = {'fontsize':12, 'fontweight':'bold'})
        if 'tituloy' in dataInstructions:
            plt.ylabel(dataInstructions['tituloy'], fontdict = {'fontsize':12, 'fontweight':'bold'})
        #Para que guarde todos los cambios
        plt.savefig(dataInstructions['nombre']+'.png')
        plt.show()

    def crearGraficaLineal(self, data, dataInstructions, mesAnio):
        #asociamos los datos
        productos = np.array(data['Nombres'])
        ventas = np.array(data['Ventas'])
        #Realizamos cambios al formato de la gráfica
        plt.figure(figsize=(10,5))
        plt.subplots_adjust(bottom=0.3, right=0.93)
        plt.xticks(size = 'small', rotation = 60, ha = 'right')
        plt.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
        #Agregamos los datos a la gráfica
        plt.plot(productos, ventas, marker = 'o',color = '#f06123')

        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        else: plt.title(mesAnio[0] + " - " + mesAnio[1], fontdict = {'fontsize':14, 'fontweight':'bold'})
        if 'titulox' in dataInstructions:
            plt.xlabel(dataInstructions['titulox'], fontdict = {'fontsize':12, 'fontweight':'bold'})
        if 'tituloy' in dataInstructions:
            plt.ylabel(dataInstructions['tituloy'], fontdict = {'fontsize':12, 'fontweight':'bold'})
        #Para que guarde todos los cambios    
        plt.savefig(dataInstructions['nombre']+'.png')    
        plt.show()

    def crearGraficaSectores(self, data, dataInstructions, mesAnio):

        productos = np.array(data['Nombres'])
        ventas = data['Ventas']
        plt.pie(ventas, labels = productos, autopct="%0.1f %%")
        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        else: plt.title(mesAnio[0] + " - " + mesAnio[1], fontdict = {'fontsize':14, 'fontweight':'bold'})
        plt.savefig(dataInstructions['nombre']+'.png')
        plt.show() 