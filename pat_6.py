from Lista_Cuadro_Piso import Lista_Cuadro_Piso


from Lista_Cuadro_Piso import Lista_Cuadro_Piso

class pat_6():

    def __init__(self):
        self.cabecera = None
        self.ultimo = None
    
    def insertar_siguiente_patron(self,codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater):
        #print("agg patron")
        if  self.cabecera == None:
            self.cabecera = self.ultimo = Lista_Cuadro_Piso(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
            #print(nombre_piso, "lo añadimos a la cabeza")
            return
        else:
            bus = self.cabecera

            existe = False
            if(bus != None) :   
                while bus != None:
                    if bus.codigo == codigo:
                        existe = True
                    bus = bus.siguiente
            if(existe==False):
                nuevaCancion = Lista_Cuadro_Piso(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
                nuevaCancion.siguiente = self.cabecera
                self.cabecera.anterior = nuevaCancion
                self.cabecera = nuevaCancion
                #print(nombre_piso, "lo añadimos al inicio") 
            else:
                print(nombre_piso, "no lo añadimos, ya existe este codigo")
            self.__circular    

    def __circular(self):
        self.cabecera.anterior = self.ultimo
        self.ultimo.siguiente = self.cabecera
