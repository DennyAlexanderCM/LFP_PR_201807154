from tkinter import Tk
from tkinter import filedialog
import webbrowser

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(">Introduce una Opción: "))
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
    

def ordenarDatos(dataList1):
    dataList = []
    longitud = len(dataList1)
    for i in dataList1:
        dataList.append(i)

    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
            if dataList[indice_actual].getTotalGanancias() < dataList[indice_siguiente_elemento].getTotalGanancias():
                # ... intercambiamos los elementos
                dataList[indice_siguiente_elemento], dataList[indice_actual] = dataList[indice_actual], dataList[indice_siguiente_elemento]
    return dataList


def productosMasMenosVendido(dataList):
    longitud = len(dataList)
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
            if dataList[indice_actual].getVendido() < dataList[indice_siguiente_elemento].getVendido():
                # ... intercambiamos los elementos
                dataList[indice_siguiente_elemento], dataList[indice_actual] = dataList[indice_actual], dataList[indice_siguiente_elemento]
    return dataList
 

def generarReporte(dataProducts,mesAnio):
    dataProductos = ordenarDatos(dataProducts)
    masVendidos = productosMasMenosVendido(dataProducts)
    nombreArchivo = "Reportes -"+mesAnio[0]+mesAnio[1]+".html"
    archi1=open(nombreArchivo,"w",encoding='utf-8')

    archi1.write("""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
                            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                        <style>
                            body {
                                background-color: #eaeefc;
                            }
                            h1 {
                                margin-top: 50px;

                                font-size: 3rem;
                                color: #214471;
                            }
                            .content {
                                text-align: center;
                                width: 350px;
                                margin: 125px auto;
                                box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
                            }
                            .section{
                                margin-top: 4rem;
                            }
                        </style>
                        <title>Reporte del mes</title>
                    </head>

                    <body>
                        <section class="container">
                            <h1 class="text-center">DATOS DE LAS VENTAS DE """)
    
    archi1.write(mesAnio[0]+" "+mesAnio[1])     

    archi1.write("""</h1><div class="container px-4 px-lg-5">
                                <div class="row gx-4 gx-lg-5 justify-content-center">
                                    <div class="col-md-10 col-lg-8 col-xl-7">
                                        <div class="section">
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th scope="col">Producto</th>
                                                        <th scope="col">Precio (Q)</th>
                                                        <th scope="col">Vendidos</th>
                                                        <th scope="col">Total (Q)</th>
                                                    </tr>
                                                </thead>
                                                <tbody>""")

    for i in dataProductos:
        archi1.write("<tr><td>"+i.getNombre()+"</td><td>"+str(i.getPrecio())+"</td><td>"+str(i.getVendido())+"</td><td>"+str(i.getTotalGanancias())+"</td></tr>")

    
    archi1.write("""                                 </tbody>
                                            </table>
                                        </div>
                                        <!-- Divider-->
                                        <hr class="my-4" />
                                        <!-- Post preview-->
                                        <div class="section">
                                            <h2 class=" text-center  alert alert-primary ">
                                                PRODUCTOS DESTACADOS
                                            </h2>
                                            <h3>Producto más vendido:
                                            </h3>
                                            <table class="table">
                                                <thead>
                                                <tr>
                                                        <th scope="col">Producto</th>
                                                        <th scope="col">Precio (Q)</th>
                                                        <th scope="col">Vendidos</th>
                                                        <th scope="col">Total (Q)</th>
                                                    </tr></thead><tbody>""")

    archi1.write('<tr><th>'+masVendidos[0].getNombre()+'</th><th>'+str(masVendidos[0].getPrecio())+'</th><th>'+str(masVendidos[0].getVendido())+'</th><th>'+str(masVendidos[0].getTotalGanancias())+'</th></tr>')                                                
    archi1.write("""                                            
                                                
                                                    
                                                </tbody>
                                            </table>
                                            <hr class="my-4"/>
                                            <h3>Producto menos vendido</h3>
                                            <table class="table">
                                                <thead>
                                                    <tr>
                                                        <th scope="col">Producto</th>
                                                        <th scope="col">Precio (Q)</th>
                                                        <th scope="col">Vendidos</th>
                                                        <th scope="col">Total (Q)</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    """)
    
    
    archi1.write('<tr><th>'+masVendidos[-1].getNombre()+'</th><th>'+str(masVendidos[-1].getPrecio())+'</th><th>'+str(masVendidos[-1].getVendido())+'</th><th>'+str(masVendidos[-1].getTotalGanancias())+'</th></tr>')                                                
    
    archi1.write(""""
                                                </tbody>
                                            </table>
                                        </div>
                                        <hr class="my-4" />
                                        <div class="content">
                                            <div class="card">
                                                <div class="card-body">
                                                    <h5 class="card-title">Datos del estudiante</h5>
                                                    <p class="card-text text-start"><Span class="fw-bold">Carné:</Span> 201807154</p>
                                                    <p class="card-text text-start"><Span class="fw-bold">Nombre:</Span> Denny Alexander Chalí Miza</p>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </section>
                    </body>

                    </html>""")
    archi1.close()
    webbrowser.open_new_tab(nombreArchivo)

    print("Reporte creado correctamente...")
