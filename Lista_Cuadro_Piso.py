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

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.cuadro_derecha
                aux = aux.cuadro_abajo
                print("")

    def LimpiarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    aux2 = auxi
                    auxi = auxi.cuadro_derecha
                    aux2 = None    
                aux3 = aux
                aux = aux.cuadro_abajo
                aux3 = None
                print("")


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
    

