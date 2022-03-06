from Nodo_Cuadro_Piso import Nodo_Cuadro_Piso as dt
import sys,os
from PIL import Image

class Lista_Cuadro_Piso():
    
    def __init__(self):
        self.inicio = None

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

    def comparar(self,self2):
        comparacion = []
        print(self.inicio)
        print(self2.inicio)
        if self.inicio != None and self2.inicio != None:
            aux = self.inicio
            aux2 = self2.inicio
            print(aux.dato+aux2.dato)
            while aux != None and aux2!=None:
                auxi = aux
                auxi2 = aux2
                while auxi != None and auxi2!=None:
                    true = auxi.dato == auxi2.dato
                    comparacion.append(true)
                    print(true)
                    auxi = auxi.siguiente
                    auxi2 = auxi2.siguiente
                aux = aux.abajo
                aux2 = aux2.abajo
                print("")
        return comparacion

    def cambios(self,self2):
        recW=0
        recB=0

        if self.inicio != None and self2.inicio != None:
            aux = self.inicio
            aux2 = self2.inicio
            while aux != None and aux2!=None:
                auxi = aux
                auxi2 = aux2
                while auxi != None and auxi2!=None:
                    if(auxi.dato=='W'):
                        recW+=1
                    if(auxi2.dato=='W'):
                        recW-=1
                    if(auxi.dato=='B'):
                        recB+=1
                    if(auxi2.dato=='B'):
                        recB-=1

                    auxi = auxi.siguiente
                    auxi2 = auxi2.siguiente
                aux = aux.abajo
                aux2 = aux2.abajo
                print("")
            
        return recB 
        
    def cambiando_a_blanco(self, num_nodo_cambiar):
        contador = 0
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    if(contador == num_nodo_cambiar):
                        if(auxi.dato == 'B'):
                            auxi.setDato('W')
                            print('seteado2')
                            return True
                    auxi = auxi.siguiente
                    contador+=1
                aux = aux.abajo
                print("")
        return False

    def cambiando_a_negro(self, num_nodo_cambiar):
        contador = 0
        if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                while auxi != None:
                    if(contador == num_nodo_cambiar):
                        if(auxi.dato == 'W'):
                            auxi.setDato('B')
                            print('seteado2')
                            return True
                    auxi = auxi.siguiente
                    contador+=1
                aux = aux.abajo
                print("")
        return False
    
    def intercambiando(self, num_nodo_cambiar1, num_nodo_cambiar2, difx,dify):
        auxi = self.inicio

    def mover_derecha(self,auxi):
        if(auxi!=None and auxi!=self.inicio):    
            temp = auxi.siguiente
            temp1a = auxi.anterior
            temp1aa = auxi.abajo
            temp1aaa = auxi.arriba
            if(temp!=None):
                tempa = temp.arriba
                tempaa = temp.abajo
                tempaaa = temp.siguiente
            if(tempaaa!=None):
                tempaaa.anterior = auxi
            auxi.anterior = temp
            auxi.abajo = tempaa
            auxi.arriba = tempa
            auxi.siguiente = tempaaa
            if(tempa!=None):
                tempa.abajo = auxi
            if(tempaa!=None):    
                tempaa.arriba = auxi
            if(temp!=None):                                        
                temp.siguiente = auxi
                temp.anterior = temp1a
                temp.abajo = temp1aa
                temp.arriba = temp1aaa
            if(temp1a!=None):
                temp1a.siguiente = temp
            if(temp1aa!=None):    
                temp1aa.arriba = temp
            if(temp1aaa!=None):    
                temp1aaa.abajo = temp
        else:
            init = self.inicio
            auxi = init.siguiente
            t = init.abajo
            t2 = auxi.abajo
            t3 = auxi.siguiente
            init.siguiente = t3
            init.abajo = t2
            init.anterior = auxi
            self.inicio = auxi
            auxi.anterior = None
            auxi.arriba = None
            auxi.siguiente = init
            auxi.abajo = t
            if(t!=None):
                t.arriba = self.inicio
            if(t2!=None):
                t2.arriba = init
            if(t3!=None):
                t3.anterior= init

        return       

    def mover_izquierda(self,aux):
        init = self.inicio
        auxi=aux
        if(auxi!=None and auxi!=init.siguiente): 
            temp = auxi.anterior
            temp1a = auxi.siguiente
            temp1aa = auxi.abajo
            temp1aaa = auxi.arriba
            if(temp!=None):
                tempa = temp.arriba
                tempaa = temp.abajo
                tempaaa = temp.anterior
            else:
                tempa = None
                tempaa = None
                tempaaa = None
                #----
            if(tempaaa!=None):
                tempaaa.siguiente = auxi
            auxi.siguiente = temp
            if(temp1a!=None):
                temp1a.anterior = temp
            auxi.anterior = tempaaa
            auxi.abajo = tempaa
            if(tempaa!=None):    
                tempaa.arriba = auxi
            auxi.arriba = tempa
            if(tempa!=None):
                tempa.abajo = auxi
            
            if(temp!=None):                                        
                temp.siguiente = temp1a
                temp.anterior = auxi
                temp.abajo = temp1aa
                temp.arriba = temp1aaa
            
            if(temp1aa!=None):    
                temp1aa.arriba = temp
            if(temp1aaa!=None):    
                temp1aaa.abajo = temp
        else:
            t = init.abajo
            t2 = auxi.abajo
            t3 = auxi.siguiente
            init.siguiente = t3
            init.abajo = t2
            init.anterior = auxi
            self.inicio = auxi
            auxi.anterior = None
            auxi.arriba = None
            auxi.siguiente = init
            auxi.abajo = t
            if(t3!=None):
                t3.anterior = init
            if(t2!=None):
                t2.arriba = init
            if(t!=None):
                t.arriba = auxi
            

            
        
        return

    def mover_abajo(self,auxi):
        if(auxi!=None and auxi!=self.inicio):
            temp = auxi.abajo
            temp1a = auxi.siguiente
            temp1aa = auxi.anterior
            temp1aaa = auxi.arriba
            if(temp!=None):
                tempa = temp.siguiente
                tempaa = temp.abajo
                tempaaa = temp.anterior
                temp.abajo = auxi
            auxi.anterior = tempaaa
            auxi.abajo = tempaa
            auxi.arriba = temp
            auxi.siguiente = tempa
            if(tempaa!=None):
                tempaa.arriba = auxi
            if(tempaaa!=None):
                tempaaa.siguiente = auxi
            if(tempa!=None):
                tempa.anterior = auxi
            if(temp!=None):
                temp.siguiente = temp1a
                temp.anterior = temp1aa
                temp.abajo = auxi
                temp.arriba = temp1aaa
            if(temp1a!=None):
                temp1a.anterior = temp
            if(temp1aa!=None):
                temp1aa.siguiente = temp
            if(temp1aaa!=None):
                temp1aaa.abajo = temp
        else:
            init = self.inicio
            auxi = init.abajo
            t = init.siguiente
            t2 = auxi.abajo
            t3 = auxi.siguiente
            init.siguiente = t3
            init.abajo = t2
            init.arriba = auxi
            self.inicio = auxi
            auxi.anterior = None
            auxi.arriba = None
            auxi.siguiente = t
            auxi.abajo = init
            if(t!=None):
                t.anterior = self.inicio
            if(t2!=None):
                t2.arriba = init
            if(t3!=None):
                t3.anterior = init
            
        return
    
    def mover_arriba(self,auxi):
        if(auxi!= None and auxi.arriba!=self.inicio):
            temp = auxi.arriba
            temp1a = auxi.siguiente
            temp1aa = auxi.anterior
            temp1aaa = auxi.abajo
            if(temp!=None):
                tempa = temp.siguiente
                tempaa = temp.arriba
                tempaaa = temp.anterior
                temp.arriba = auxi
            auxi.anterior = tempaaa
            auxi.abajo = temp
            auxi.arriba = tempaa
            auxi.siguiente = tempa
            if(tempaa!=None):
                tempaa.abajo = auxi
            if(tempaaa!=None):
                tempaaa.siguiente = auxi
            if(tempa!=None):    
                tempa.anterior = auxi
            if(temp!=None):    
                temp.siguiente = temp1a
                temp.anterior = temp1aa
                temp.abajo = temp1aaa
                temp.arriba = auxi
            if(temp1a!=None):    
                temp1a.anterior = temp
            if(temp1aa!=None):    
                temp1aa.siguiente = temp
            if(temp1aaa!=None):    
                temp1aaa.arriba = temp
        else:
            init = self.inicio
            auxi = init.abajo
            t = init.siguiente
            t2 = auxi.abajo
            t3 = auxi.siguiente
            init.siguiente = t3
            init.abajo = t2
            init.arriba = auxi
            self.inicio = auxi
            auxi.anterior = None
            auxi.arriba = None
            auxi.siguiente = t
            auxi.abajo = init
            if(t!=None):
                t.anterior = self.inicio
            if(t2!=None):
                t2.arriba = init
            if(t3!=None):
                t3.anterior = init
            
            
        return

    def datToInterpolate(self, num_nodo_cambiar1, num_nodo_cambiar2,c1,c2,f1,f2):
        print(num_nodo_cambiar1)
        print(num_nodo_cambiar2)
        cc1=c1
        cc2=c2
        
        if(cc1!=cc2):
            if self.inicio != None:
                print('inicio')
                aux = self.inicio
                y=0
                while aux != None:
                    auxi = aux
                    x=0
                    while auxi != None:
                        if(y==f1 or x==c1):
                            if(x>c2):
                                while(x!=c2):
                                    print('que')
                                    temp = auxi.anterior
                                    temp1a = auxi.siguiente
                                    temp1aa = auxi.abajo
                                    temp1aaa = auxi.arriba
                                    if(temp!=None):
                                        tempa = temp.arriba
                                        tempaa = temp.abajo
                                        tempaaa = temp.anterior
                                    if(tempaaa!=None):
                                        tempaaa.siguiente = auxi
                                    auxi.anterior = tempaaa
                                    auxi.abajo = tempaa
                                    auxi.arriba = tempa
                                    if(tempa!=None):
                                        tempa.abajo = auxi
                                    if(tempaa!=None):    
                                        tempaa.arriba = auxi
                                    if(temp!=None):                                        
                                        temp.siguiente = temp1a
                                        temp.anterior = auxi
                                        temp.abajo = temp1aa
                                        temp.arriba = temp1aaa
                                    if(temp1a!=None):
                                        temp1a.anterior = temp
                                    if(temp1aa!=None):    
                                        temp1aa.arriba = temp
                                    if(temp1aaa!=None):    
                                        temp1aaa.abajo = temp
                                    x-=1
                                    #correccion de filas (pos y)
                                if(y<f2):
                                    while(y!=f2):
                                        temp = auxi.abajo
                                        temp1a = auxi.siguiente
                                        temp1aa = auxi.anterior
                                        temp1aaa = auxi.arriba
                                        if(temp!=None):
                                            tempa = temp.siguiente
                                            tempaa = temp.abajo
                                            tempaaa = temp.anterior
                                            temp.abajo = auxi
                                            auxi.anterior = tempaaa
                                            auxi.abajo = tempaa
                                            auxi.arriba = temp
                                            auxi.siguiente = tempa
                                            tempaa.arriba = auxi
                                            tempaaa.siguiente = auxi
                                            tempa.anterior = auxi
                                        temp.siguiente = temp1a
                                        temp.anterior = temp1aa
                                        temp.abajo = auxi
                                        temp.arriba = temp1aaa
                                        temp1a.anterior = temp
                                        temp1aa.siguiente = temp
                                        temp1aaa.abajo = temp
                                        y+=1
                                if(y>f2):
                                    while(y!=f2):
                                        temp = auxi.arriba
                                        temp1a = auxi.siguiente
                                        temp1aa = auxi.anterior
                                        temp1aaa = auxi.abajo
                                        if(temp!=None):#-------aki
                                            tempa = temp.siguiente
                                            tempaa = temp.arriba
                                            tempaaa = temp.anterior
                                            temp.arriba = auxi
                                        auxi.anterior = tempaaa
                                        auxi.abajo = temp
                                        auxi.arriba = tempaa
                                        auxi.siguiente = tempa
                                        tempaa.abajo = auxi
                                        tempaaa.siguiente = auxi
                                        tempa.anterior = auxi
                                        temp.siguiente = temp1a
                                        temp.anterior = temp1aa
                                        temp.abajo = temp1aaa
                                        temp.arriba = auxi
                                        temp1a.anterior = temp
                                        temp1aa.siguiente = temp
                                        temp1aaa.arriba = temp
                                        y-=1#here

                                return
                            else:
                                while(x!=c2):
                                    
                                    print('qq')
                                    if(x<c2):
                                        temp = auxi.siguiente
                                        temp1a = auxi.anterior
                                        temp1aa = auxi.abajo
                                        temp1aaa = auxi.arriba
                                        if(temp!=None):
                                            tempa = temp.arriba
                                            tempaa = temp.abajo
                                            tempaaa = temp.siguiente
                                        if(tempaaa!=None):
                                            tempaaa.anterior = auxi
                                        auxi.anterior = temp
                                        auxi.abajo = tempaa
                                        auxi.arriba = tempa
                                        if(tempa!=None):
                                            tempa.abajo = auxi
                                        if(tempaa!=None):    
                                            tempaa.arriba = auxi
                                        if(temp!=None):                                        
                                            temp.siguiente = auxi
                                            temp.anterior = temp1a
                                            temp.abajo = temp1aa
                                            temp.arriba = temp1aaa
                                        if(temp1a!=None):
                                            temp1a.siguiente = temp
                                        if(temp1aa!=None):    
                                            temp1aa.arriba = temp
                                        if(temp1aaa!=None):    
                                            temp1aaa.abajo = temp
                                        x+=1
                                return        
                                        

                        auxi = auxi.siguiente
                        x+=1
                    aux = aux.abajo
                    y+=1
                    print("")


        
        return 

    def nodos_intercambiar(self, datos):
         kontador = 0 
         pieza1 = -6
         f1=0 
         f2=0
         f=0
         c1=0
         c2=0
         
         pieza2 =-6
         if self.inicio != None:
            aux = self.inicio
            while aux != None:
                auxi = aux
                c=0
                while auxi != None:
                    
                    if(auxi.getDato()!=datos[kontador] and pieza1==-6):
                        pieza1=kontador
                        f1 = f
                        c1 = c
                    else:
                        if( pieza2==-6 and auxi.getDato()!=datos[kontador] and auxi.getDato()==datos[pieza1]):
                            pieza2=kontador
                            f2 =f
                            c2 =c
                            print('dandole')
                            #moviendo dos cosos en la misma columna de arriba para abajo
                            print('--------')
                            print(c1)#0
                            print(c2)#4
                            print(f1)#0
                            print(f2)#0
                            print('--------')

                            if(f2<f1 and c2==c1):
                                y=f2
                                while(y<f1):
                                    self.mover_abajo(auxi)
                                    y+=1
                                temp = auxi.arriba
                                y-=1
                                while(y>f2):
                                    self.mover_arriba(temp)
                                    y-=1
                                return
                            #moviendo dos cosos en la misma columa de abajo para arriba
                            elif(f2>f1 and c2==c1):
                                y=f2
                                while(y>f1):
                                    self.mover_arriba(auxi)
                                    y-=1
                                temp = auxi.abajo
                                y+=1
                                while(y<f2):
                                    self.mover_abajo(temp)
                                    y+=1
                                return
                            #moviendo dos cosos en la misma fila de derecha a izquierda
                            elif(f1==f2 and c2>c1):
                                x=c2
                                while(x>c1):
                                    self.mover_izquierda(auxi)
                                    print('---')
                                    self.MostrarMat()
                                    x-=1
                                temp = auxi.siguiente
                                x+=1
                                while(x<c2):
                                    self.mover_derecha(temp)
                                    x+=1 
                                return
                            #moviendo dos cosos en la misma fila de izquierda a derecha
                            elif(f1==f2 and c2<c1):
                                x=c2
                                while(x<c1):
                                    self.mover_derecha(auxi)
                                    x+=1
                                temp = auxi.anterior
                                x-=1
                                while(x>c2):
                                    self.mover_izquierda(temp)
                                    x-=1 
                                return
                            #moviendo un coso arriba izquierda y regresando el otro derecha abajo
                            elif(f2>f1 and c2>c1):
                                y=f2
                                x=c2
                                while(y>f1):
                                    self.mover_arriba(auxi)
                                    y-=1
                                while(x>c1):
                                    self.mover_izquierda(auxi)
                                    x-=1
                                temp = auxi.siguiente
                                x+=1
                                while(x<c2):
                                    self.mover_derecha(temp)
                                    x+=1
                                while(y<f2):
                                    self.mover_abajo(temp)
                                    y+=1
                                return
                            #moviendo un coso arriba derecha y regresando el otro izquierda abajo
                            elif(f2>f1 and c2<c1):
                                y=f2
                                x=c2
                                while(y>f1):
                                    self.mover_arriba(auxi)
                                    y-=1
                                while(x<c1):
                                    self.mover_derecha(auxi)
                                    x+=1
                                temp = auxi.anterior
                                x-=1
                                while(x>c2):
                                    self.mover_izquierda(temp)
                                    x-=1
                                while(y<f2):
                                    self.mover_abajo(temp)
                                    y+=1
                                return
                            #moviendo un coso abajo derecha y regresando el otro izquierda arriba
                            elif(f2<f1 and c2<c1):
                                y=f2
                                x=c2
                                while(y<f1):
                                    self.mover_abajo(auxi)
                                    y+=1
                                while(x<c1):
                                    self.mover_derecha(auxi)
                                    x+=1
                                temp = auxi.anterior
                                x-=1
                                while(x>c2):
                                    self.mover_izquierda(temp)
                                    x-=1
                                while(y>f2):
                                    self.mover_arriba(temp)
                                    y-=1
                                return
                            #moviendo un coso abajo izquierda y regresando el otro arriba derecha 
                            elif(f2<f1 and c2>c1):
                                x=c2
                                y=f2
                                while(y<f1):
                                    self.mover_abajo(auxi)
                                    y+=1
                                while(x>c1):
                                    self.mover_izquierda(auxi)
                                    x-=1
                                temp = auxi.siguiente
                                x+=1
                                while(x<c2):
                                    self.mover_derecha(temp)
                                    x+=1
                                while(y>f2):
                                    self.mover_arriba(temp)
                                    y-=1
                                return

                                 
                                
                                












                            
                               
                            return
                    auxi = auxi.siguiente
                    c +=1
                    kontador+=1
                aux = aux.abajo
                f+=1
                print("line")
        
    def imagen2(self,nombre):
        file = open("Reporte2.dot","w")
        file.write("digraph G {node [fontname=\"Arial\"];node_A [shape=record    label=\"")

        p = self.inicio
        i = 1
        file.write("{"+str(nombre)+" mod |")
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
        os.system("dot -Tpng Reporte2.dot -o "+str(nombre)+"mod.png")
        im = Image.open(str(nombre)+"mod.png")
        im.show()

