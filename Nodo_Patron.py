class Nodo_Patron():
 
    def __init__(self,codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater):
        self.codigo = codigo
        self.nombre_piso = nombre_piso
        self.filas = filas
        self.columnas = columnas
        self.precio_cambio = precio_cambio
        self.precio_volteo = precio_volteo
        self.patron_mater = patron_mater
        self.siguiente = None
        self.anterior = None
