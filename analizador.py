from producto import Producto

class Analizador():
    def __init__(self):
        self.mes = ""
        self.anio = 0
        self.dataList = {}
        self.instr = {}

    def analizarDatosVentas(self,data):
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

        #Others
        aux = ""

        for caracter in data:
            #Obtenemos el mes
            if estadoMes == False:
                if caracter != ":":
                    aux += caracter
                else:
                    nombreMes = aux
                    estadoMes = True
                    aux = ""
            #Obtenemos año
            elif estadoAnio == False:
                if caracter != "=":
                    aux += caracter
                else:
                    anio = aux
                    estadoAnio = True
                    aux = ""
            #se inicia la captura de productos
            elif caracter == "(":
                addProducts = True
            #indicamos la ficalizacion de lectura de datos
            elif caracter == ")" and estadoAnio and estadoMes:
                    self.mes = nombreMes
                    self.anio = anio
                    self.dataList["productos"] = productsList
                    print("Archivo leído correctamente\n")

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
                    a = Producto(lista[0],lista[1],lista[2])
                    productsList.append(a)
                    addProductA = False
                    addProductB = False
                    state = 0
                    aux = ""
                else:
                    aux += caracter
                
            else:
                print("El archivo contiene errores")
    
    def analizarDatosIstrucciones(self,data):
        addDates = True
        instrucciones = {}
        estado = 0

        init = data[0]+data[1]
        end = data[len(data)-2]+data[len(data)-1]

        if init == "<¿" and end == "?>":
            aux = ""
            auxDate = ""
            #tomamos los datos solo dentro de los signos
            data = data[2:-2]
            data += "#"
            for caracter in data:
                if caracter == ":":
                    addDates = False
                elif addDates == True:
                    aux += caracter
                elif caracter == '\"':
                    estado+=1
                elif estado == 1:
                    auxDate += caracter
                elif (estado == 2 and caracter == ",") or caracter == "#":
                    if aux == "nombre":
                        instrucciones[aux] = auxDate
                    elif aux == "grafica":
                        instrucciones[aux] = auxDate
                    elif aux == "titulo":
                        instrucciones[aux] = auxDate
                    elif aux == "titulox":
                        instrucciones[aux] = auxDate
                    elif aux == "tituloy":
                        instrucciones[aux] = auxDate
                    else:
                        print(aux)
                        print("No se reconoce este comando", aux)
                    #Reiniciamos los datos para una nueva lectura
                    aux = ""
                    auxDate = ""
                    estado = 0
                    addDates = True
                else:
                    print("Archivo con formato incorrecto")

            if 'nombre' in instrucciones and 'grafica' in instrucciones:
                self.instr = instrucciones
                print("Datos cargados correctamente\n")
            else:
                print("No se guardaron cambios, datos insuficientes")
            
        else:
            print("Archivo con formato incorrecto")

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getMes(self):
        return self.mes
    
    def getAnio(self):
        return self.anio
    
    def getDataList(self):
        return self.dataList
    
    def getDataLlistInstructions(self):
        return self.instr
