class Producto():
    def __init__(self,nombre,precioUnitario,cantidadVendida):
        self.nombre = nombre
        self.precioUnitario = precioUnitario
        self.cantidadVendida = cantidadVendida

    # METODOS GET
    # Creamos nuestros metodos para obtener la informacion, usando self
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precioUnitario
    
    def getVendido(self):
        return self.cantidadVendida

    def getTotalGanancias(self):
        total = self.cantidadVendida*self.precioUnitario
        return total