from Nodo_Cuadro_Piso import Nodo_Cuadro_Piso as dt


class Lista_Cuadro_Piso():
    
    def __init__(self):
        self.inicio = None
    
    #creo la matriz 
#dddd
    """def creacion_matriz(self,filas,columnas,Datos):
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

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.right
                aux = aux.down
                print("")

    def LimpiarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    aux2 = auxi
                    auxi = auxi.right
                    aux2 = None    
                aux3 = aux
                aux = aux.down
                aux3 = None
                print("")

    def crear_mat(self, filas, columnas, Datos):
        it_row = 0
        it_column = 0
        it_datos = 0
        temp = self.inicio
        
        while(it_row < filas):
            while(it_column <columnas):
                nuevoNodo = dt(it_datos)
                
                temp = nuevoNodo
                temp.right = None
                temp.down = None
                it_column +=1
                it_datos +=1
                temp = temp.right
            it_row_temp = 0
            it_row+=1
            temp2 = self.inicio 
            if(temp2 != None):
                while  it_row != it_row_temp:
                    temp2 = temp2.down
                temp = temp2 
                
            
                


        
        return 



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
    

