from Nodo_Cuadro_Piso import Nodo_Cuadro_Piso as dt


class Lista_Cuadro_Piso():
    
    def __init__(self):
        self.inicio = None

    def eliminar_todo(self):
        temp = self.cabecera
        temp2 = self.cabecera
        while temp or temp2:
            temp = None
            temp = temp.cuadro_derecha

    def creacion_matriz(self,filas,columnas,Datos):
        q = s = None
        it = 0 
        for i in range(1, filas+1):
            for j in range(1, columnas+1):
                NuevoNodo = dt(Datos[it])
                it += 1
                NuevoNodo.cuadro_derecha = None
                NuevoNodo.cuadro_abajo = None
                if j==1:
                    NuevoNodo.cuadro_izquierda = None
                    if self.inicio == None:
                        self.inicio = NuevoNodo
                    q = NuevoNodo
                else:
                    NuevoNodo.cuadro_izquierda = q
                    q.cuadro_derecha = NuevoNodo
                    q = NuevoNodo
                if i == 1:
                    NuevoNodo.cuadro_arriba = q
                else:
                    NuevoNodo.cuadro_arriba = s
                    s = s.cuadro_derecha
            s = self.inicio
            while s.cuadro_abajo != None:
                s = s.cuadro_abajo


    """def delet_mat(self,filas,columnas,Datos):

        q = s = None
        it = 0 
        for i in range(1, filas+1):
            for j in range(1, columnas+1):
                NuevoNodo = dt(Datos[it])
                it += 1
                NuevoNodo.cuadro_derecha = None
                NuevoNodo.cuadro_abajo = None
                if j==1:
                    NuevoNodo.cuadro_izquierda = None
                    if self.inicio == None:
                        self.inicio = NuevoNodo
                    q = NuevoNodo
                else:
                    NuevoNodo.cuadro_izquierda = q
                    q.cuadro_derecha = NuevoNodo
                    q = NuevoNodo
                if i == 1:
                    NuevoNodo.cuadro_arriba = q
                else:
                    NuevoNodo.cuadro_arriba = s
                    s = s.cuadro_derecha
            s = self.inicio
            while s.cuadro_abajo != None:
                s = s.cuadro_abajo"""
            
                    


            
    def insertar_nodo(self, color):
        if self.cabecera == None:
            self.cabecera = dt(color)


    def insertar_siguienteAlb(self, color):
        if  self.cabecera == None:
            self.cabecera = dt(color)
            #print(codigo, "lo añadimos a la cabeza")
            return
        else:
            act = self.cabecera
            bus = self.cabecera

            existe = False
            if(bus != None) :   
                while bus != None:
                    if bus.codigo == codigo:
                        existe = True
                    bus = bus.cuadro_derecha
            if(existe==False):
                nuevo_piso = dt(color)
                nuevo_piso.cuadro_derecha = self.cabecera
                self.cabecera.cuadro_derecha = nuevo_piso
                self.cabecera = nuevo_piso
                #print(codigo, "lo añadimos al final") 

    def elminarUnAlbum(self, nombreAlbum):
        act = self.cabecera
        ant = None
        while act and act.nombreAlbum == nombreAlbum:
            ant = act
            act = ant.siguiente
        if ant is None:
            self.cabecera = act.siguiente
        elif act:
            ant.siguiente = act.siguiente
            act.siguiente = None
    
    def insertarCancion(self,artista, album, nombre, imagen, ruta, vecesReproducidas):
        bus = self.cabecera
        if(bus != None) :   
            while bus != None:
                if bus.nombreAlbum == album:
                    bus.canciones.insertar_siguienteCan(nombre,artista, album,imagen, ruta, vecesReproducidas)
                bus = bus.siguiente
    
    def print_listas_de_rep(self):
        temp = self.cabecera
        while temp != None:
            print(temp.nombreAlbum)
            temp = temp.siguiente

