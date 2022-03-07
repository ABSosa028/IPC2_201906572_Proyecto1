from traceback import print_tb
from Nodo_Patron import Nodo_Patron 

class Lista_Patrones:
     
    def __init__(self):
        self.cabecera = None
        self.ultimo = None

    def insertar_siguiente_patron(self,codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater):
        #print("agg patron")
        if  self.cabecera == None:
            self.cabecera = self.ultimo = Nodo_Patron(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
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
                nuevaCancion = Nodo_Patron(codigo, nombre_piso, filas, columnas, precio_volteo, precio_cambio, patron_mater)
                nuevaCancion.siguiente = self.cabecera
                self.cabecera.anterior = nuevaCancion
                self.cabecera = nuevaCancion
                #print(nombre_piso, "lo añadimos al inicio") 
            else:
                print(codigo, "no lo añadimos, ya existe este codigo")
        self.__circular    

    def toString(self):
        act = self.cabecera
        Lista = []
        while act :
            Lista.append(act.toString())
            act = act.siguiente
        return Lista

    def __circular(self):
        self.cabecera.anterior = self.ultimo
        self.ultimo.siguiente = self.cabecera

    def busqueda(self, codigo_nodo):
        act = self.cabecera
        busqueda = None
        while act :
            #print(act.codigo)
            if(act.codigo != codigo_nodo):
                act = act.siguiente
            else:
                busqueda = act
                return busqueda
        return busqueda

    def busqueda2(self, nombrepiso):
        act = self.cabecera
        Lista_resp = []
        while act :
            #print(act.codigo)
            if(act.nombre_piso != nombrepiso):
                act = act.siguiente
            else:
                Lista_resp.append(act)
                act = act.siguiente
        return Lista_resp

    def elminar_patron(self, codigo_nodo):
        act = self.cabecera
        ant = None
        while act:
            if(act.codigo != codigo_nodo):
                act = act.siguiente
            else:
                act = None
        act = self.cabecera
        if(self.cabecera== None):
            self.cabecera= self.cabecera.siguiente
            self.cabecera.anterior = self.ultimo
        
            ant = act
            act = ant.siguiente
            if ant is None:
                self.cabecera = act.siguiente
            elif act:
                ant.siguiente = act.siguiente
                act.siguiente = None
    
    def print_lista_patrones(self):
        temp = self.cabecera
        while temp != None:
            print(temp.codigo)
            temp = temp.siguiente
        else:
            print()