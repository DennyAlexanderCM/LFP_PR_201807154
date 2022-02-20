from app import *
from analizador import Analizador
from graficas import Graficas
def run():
    txtData = ""
    txtInstrucciones = ""
    end = False
    selection = 0
    a = Analizador()
    b = Graficas()
    
    while not end:
        print("\n=========== Menú ===========\n1. Cargar Data\n2. Cargar Instrucciones\n3. Análizar\n4. Reportes\n5. Salir")
        selection = pedirNumeroEntero()

        if selection == 1:
            txtData = leerArchivo(".data")
            if txtData != None:
                a.analizarDatosVentas(txtData)
            else:
                print("Sin cambios\n")
        
        elif selection == 2:
            txtInstrucciones = leerArchivo(".lfp")
            if txtInstrucciones != None:
                a.analizarDatosIstrucciones(txtInstrucciones)
            else:
                print("Sin cambios\n")

        elif selection == 3:
            #Obtenemos unu diccionario con listas de los nombres de los productos así como de las ganancias
            diccionarioDatosVentas = analizarProductos(a.getDataList())
            mesAnio = [a.getMes(), a.getAnio()]
            diccionarioInstrucciones = a.getDataLlistInstructions()
            b.generarGrafica(diccionarioDatosVentas,diccionarioInstrucciones, mesAnio)
        elif selection == 4:
            aux = a.getDataList()
            mesAnio = [a.getMes(), a.getAnio()]
            generarReporte(aux['productos'],mesAnio)

        elif selection == 5:
            print("Finalizando programa...")
            end = True

        else:
            print("Intente de nuevo")

if __name__ == "__main__":
    run()