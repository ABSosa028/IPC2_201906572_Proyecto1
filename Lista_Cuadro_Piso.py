from Nodo_Cuadro_Piso import Nodo_Cuadro_Piso as dt
import sys,os
from PIL import Image

class Lista_Cuadro_Piso():
    
    def __init__(self):
        self.inicio = None
        self.siguiente = None
        self.anterior = None

    def CrearMatriz(self,n,m,Datos):
        q = None
        s = None
        k = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                nuevoNodo = dt(Datos[k])
                k = k + 1
                nuevoNodo.siguiente = None
                nuevoNodo.abajo = None
                if j == 1:
                    nuevoNodo.anterior = None
                    if self.inicio == None:
                        self.inicio = nuevoNodo
                    q = nuevoNodo
                else:
                    nuevoNodo.anterior = q
                    q.siguiente = nuevoNodo
                    q = nuevoNodo
                if i == 1:
                    nuevoNodo.arriba = None
                    q = nuevoNodo
                else:
                    nuevoNodo.arriba = s
                    s.abajo = nuevoNodo
                    s = s.siguiente
            s = self.inicio
            while s.abajo != None:
                s = s.abajo

    def MostrarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    auxi.Mostrar()
                    auxi = auxi.siguiente
                aux = aux.abajo
                print("")

    def LimpiarMat(self):
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    aux2 = auxi
                    auxi = auxi.siguiente
                    aux2 = None    
                aux3 = aux
                aux = aux.abajo
                aux3 = None
                print("")

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

    def imagen(self,nombre):
        file = open("Reporte.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.inicio
        i = 1
        file.write("{"+str(nombre)+"|")
        while p != None:
            file.write(str(i))
            i = i + 1
            p = p.abajo
            if p != None:
                file.write("|")
        file.write("}|")

        aux = self.inicio
        s = 1
        while aux != None:
            file.write("{"+str(s)+"|")
            auxi = aux
            while auxi != None:
                file.write(auxi.getDato())
                auxi = auxi.abajo
                if auxi != None:
                    file.write("|")
            aux = aux.siguiente
            file.write("}")
            s = s + 1
            if aux != None:
                file.write("|")
   
        file.write("\"];} ")
        file.close()
        os.system("dot -Tpng Reporte.dot -o "+str(nombre)+".png")
        im = Image.open(str(nombre)+".png")
        im.show()



"""
    def incert_nodo(self, fila, columna, dato):
        temp = self.inicio
        if(self.inicio == None):
            self.inicio = dt(dato)
            temp = self.inicio
            temp = temp.right
        else:
            temp = temp.right
            it_row = 0
            it_column = 0
            while(it_row <=fila):
                while(it_column <= columna):
                    if(it_column ==columna and it_row ==fila):
                        temp = dt(dato)
                        
                    else:
                        temp = temp.right
                        it_column +=1
                temp = temp.down
                it_row += 1
    
    
    def crear_mat(self, filas, columnas, Datos):
        it_row = 0
        it_column = 0
        it_datos = 0
        temp = self.inicio
        print()
        while(it_row <filas):
            
            while(it_column < columnas):
                if(it_datos<len(Datos)):
                    nuevoNodo = dt(Datos[it_datos])
                    print(Datos[it_datos])
                    if(temp == None):
                        temp = dt(Datos[it_datos])
                        temp = self.inicio
                    if(temp==None):
                        temp = nuevoNodo
                        temp.right = None
                        temp.down = None
                        it_column +=1
                        it_datos +=1
                        temp = temp.right
                else:
                    return
                it_row_temp = 0
                it_row+=1
                temp2 = self.inicio 
                print(self.inicio)
                if(temp2 != None):
                    print(self.inicio)
                    while  it_row > it_row_temp:
                        print(it_row, it_row_temp)
                        temp2 = temp2.down
                        it_row_temp +=1

                    temp = temp2 

        return 

    def delet_mat(self,filas,columnas,Datos):

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
    

