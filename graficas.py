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

    def generarGrafica(self, data, dataInstructions):
        tipoGrafica = dataInstructions['grafica']
        if tipoGrafica == 'barras':
            self.crearGraficaBarras(data, dataInstructions)
        elif tipoGrafica == 'lineas':
            self.crearGraficaLineal(data, dataInstructions)
        elif tipoGrafica == 'líneas':
            self.crearGraficaLineal(data, dataInstructions)
        elif tipoGrafica == 'pie':
            self.crearGraficaSectores(data, dataInstructions)
        else:
            print("Tipo de gráfica incorrecto\n")

    def crearGraficabarras(self, data, dataInstructions):
        #asociamos los datos
        productos = np.array(data['Nombres'])
        ventas = np.array(data['Ventas'])
        #agregamos los datos a la grafica
        plt.bar(productos, ventas)
        plt.savefig(dataInstructions['nombre']+'.png')
        
        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        if 'titulox' in dataInstructions:
            plt.xlabel(dataInstructions['titulox'])
        if 'tituloy' in dataInstructions:
            plt.ylabel(dataInstructions['tituloy'])
        plt.show()

    def crearGraficaLineal(self, data, dataInstructions):
        #asociamos los datos
        productos = np.array(data['Nombres'])
        ventas = np.array(data['Ventas'])
        #agregamos los datos a la grafica
        plt.plot(productos, ventas, marker = 'o')
        plt.savefig(dataInstructions['nombre']+'.png')

        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        if 'titulox' in dataInstructions:
            plt.xlabel(dataInstructions['titulox'])
        if 'tituloy' in dataInstructions:
            plt.ylabel(dataInstructions['tituloy'])
        plt.show()

    def crearGraficaSectores(self, data, dataInstructions):

        productos = np.array(data['Nombres'])
        ventas = data['Ventas']
        plt.pie(ventas, labels = productos, autopct="%0.1f %%")
        plt.legend(title = "Four Fruits:")
        if  'titulo' in dataInstructions:
            plt.title(dataInstructions['titulo'], fontdict = {'fontsize':14, 'fontweight':'bold'})
        if 'titulox' in dataInstructions:
            plt.legend(title = dataInstructions['titulox'])
        plt.show() 