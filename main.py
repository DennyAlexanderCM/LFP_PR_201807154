from app import *

def run():
    txtData = None
    txtInstrucciones = None
    end = False
    selection = 0
    while not end:
        print("------------Menú------------\n1. Cargar Data\n2. Cargar Instrucciones\n3. Análizar\n4. Reportes\n5. Salir")
        selection = pedirNumeroEntero()

        if selection == 1:

            txtData = leerArchivo()
            if rute != None:
                print(txtData)
            else:
                print("sin Cambios")

        elif selection == 2:
            txtInstrucciones = leerArchivo()
            if txtInstrucciones != None:
                print(txtInstrucciones)
            else:
                print("sin Cambios")
        elif selection == 3:
            dataAnalizado = analizarData(txtData)
        elif selection == 4:
            print("3")
        elif selection == 5:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo")

if __name__ == "__main__":
    run()