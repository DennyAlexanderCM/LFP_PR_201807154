from app import *

def run():
    txtData = ""
    txtInstrucciones = ""
    end = False
    selection = 0
    
    while not end:

        print("------------Menú------------\n1. Cargar Data\n2. Cargar Instrucciones\n3. Análizar\n4. Reportes\n5. Salir")
        selection = pedirNumeroEntero()

        if selection == 1:

            txtData = leerArchivo(".data")
            if txtData != None:
                print("Datos cargados...\n")
            else:
                print("sin Cambios")

        elif selection == 2:
            txtInstrucciones = leerArchivo(".lfp")
            if txtInstrucciones != None:
                print("Datos cargados...\n")
                print(txtInstrucciones)
            else:
                print("sin Cambios")

        elif selection == 3:
            analizarDatos(txtData)

        elif selection == 4:
            crearGraficaSectores()

        elif selection == 5:
            print("Finalizando programa...")
            end = True

        else:
            print("Intente de nuevo")

if __name__ == "__main__":
    run()